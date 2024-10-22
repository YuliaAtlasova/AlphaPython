
if __name__ == '__main__':
    test_number = '01'
    sprint_duration = 10

    with open(f'test_data/withPostpones/incomeTasks{test_number}.txt') as file:
        income_tasks = file.read().splitlines()
        test_name = income_tasks[0]
        tasks = [[int(x) for x in line.split()] for line in income_tasks[1:] if line.strip()]
    print(f'{tasks} - Initial tasks list')

    with open(f'test_data/withPostpones/outcomeTasks{test_number}.txt') as file:
        outcome_tasks = file.read().splitlines()
    expected_tasks_count = int(outcome_tasks[0])
    expected_tasks = [[int(x) for x in line.split()] for line in outcome_tasks[1:]]

    if not tasks:
        assert expected_tasks_count == 0, f"Expected 0 tasks, but got {expected_tasks_count}"
        print("No tasks to process")
        exit(0)

    tasks = [task for task in tasks if task[0] + task[1] - 1 <= sprint_duration]
    print(f'{tasks} - large tasks that are coming too late to be completed are removed')

    for current_task in tasks:
        current_task.append(current_task[0] + current_task[1] - 1)
    print(f'{tasks} - tasks converted to startDate -duration - endDate')

    tasks = sorted(tasks, key=lambda task: (task[2], task[0]))
    print(f'{tasks} - tasks, sorted by endDate and startDate')

    completed_tasks = []
    if tasks:
        first_task = tasks[0]
        first_start_date = first_task[0]
        first_end_date = first_start_date + first_task[1] - 1
        completed_tasks.append([first_start_date, first_end_date])
    for current_task in tasks[1:]:
        last_added_task = completed_tasks[len(completed_tasks)-1]
        first_empty_day = last_added_task[1] + 1

        # Adjust current task start date if it begins before the first empty day
        curr_task_end_date = current_task[2]
        if current_task[0] <= first_empty_day:
            current_task[0] = first_empty_day
            curr_task_end_date: int = current_task[0] + current_task[1] - 1
        # Check if current task can be completed during the sprint
        if curr_task_end_date < sprint_duration + 1:
            completed_tasks.append([current_task[0], curr_task_end_date])
    actual_tasks_count = len(completed_tasks)

    print(f'test description: {test_name}')
    print(f'{expected_tasks_count} - expected tasks count')
    print(f'{actual_tasks_count} - actual tasks count')
    print(f'{expected_tasks} - expected tasks list')
    print(f'{completed_tasks} - actual completed tasks list')

    assert expected_tasks_count == actual_tasks_count, f"Expected {expected_tasks_count}, got {actual_tasks_count}"
    for i, (expected, actual) in enumerate(zip(expected_tasks, completed_tasks)):
        assert expected == actual, f"Mismatch at index {i}: expected {expected}, got {actual}"
