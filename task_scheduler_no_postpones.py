
if __name__ == '__main__':
    test_number = '01'
    sprint_duration = 10

    with open(f'test_data/noPostpones/incomeTasks{test_number}.txt') as file:
        income_tasks = file.read().splitlines()
        test_name = income_tasks[0]
        tasks = [[int(x) for x in line.split()] for line in income_tasks[1:] if line.strip()]
    print(f'{tasks} - Initial tasks list')

    with open(f'test_data/noPostpones/outcomeTasks{test_number}.txt') as file:
        outcome_tasks = file.read().splitlines()
    expected_tasks_count = int(outcome_tasks[0])
    expected_tasks = [[int(x) for x in line.split()] for line in outcome_tasks[1:]]

    if not tasks:
        assert expected_tasks_count == 0, f"Expected 0 tasks, but got {expected_tasks_count}"
        print("No tasks to process")
        exit(0)

    tasks = [task for task in tasks if task[0] + task[1] - 1 <= sprint_duration]
    print(f'{tasks} - large tasks that are coming too late to be completed are removed')

    tasks_dict = {}
    for k, v in tasks:
        tasks_dict.setdefault(k, []).append(v)
        tasks_dict = dict(sorted(tasks_dict.items()))
    print(f'{tasks_dict} - task durations, grouped and sorted by startDate')

    easier_tasks = []
    for start_date in tasks_dict:
        easier_tasks.append([start_date, min(tasks_dict[start_date])])
    print(f'{easier_tasks} pick smaller tasks for current startDate')

    for current_task in easier_tasks:
        current_task[1] = current_task[0] + current_task[1] - 1
    print(f'{easier_tasks} - tasks converted to startDate - endDate')

    easier_tasks.sort(key = lambda et: et[1])
    print(f'{easier_tasks} - tasks, sorted by endDate')

    completed_tasks = []
    if easier_tasks: completed_tasks = [easier_tasks[0]]
    for task in easier_tasks[1:]:
        if task[0] > completed_tasks[len(completed_tasks)-1][1]:
            completed_tasks.append(task)
    actual_tasks_count = len(completed_tasks)

    print(f'test description: {test_name}')
    print(f'{expected_tasks_count} - expected tasks count')
    print(f'{actual_tasks_count} - actual tasks count')
    print(f'{expected_tasks} - expected tasks list')
    print(f'{completed_tasks} - actual completed tasks list')

    assert expected_tasks_count == actual_tasks_count, f"Expected {expected_tasks_count}, got {actual_tasks_count}"
    for i, (expected, actual) in enumerate(zip(expected_tasks, completed_tasks)):
        assert expected == actual, f"Mismatch at index {i}: expected {expected}, got {actual}"
