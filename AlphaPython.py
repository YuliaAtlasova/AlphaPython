
if __name__ == '__main__':
    test_number = '05'
    sprint_duration = 10

    with open(f'test_data/noPostpones/incomeTasks{test_number}.txt') as file:
        income_tasks = file.readlines()[1:]
        tasks = [[int(x) for x in line.split()] for line in income_tasks if line.strip()]
    print(tasks, ' - Initial tasks list')

    with open(f'test_data/noPostpones/outcomeTasks{test_number}.txt') as file:
        outcome_tasks = file.read().splitlines()
    expected_tasks_number = int(outcome_tasks[0])
    expected_tasks = [[int(x) for x in line.split()] for line in outcome_tasks[1:]]

    if not tasks:
        assert expected_tasks_number == 0, f"Expected 0 tasks, but got {expected_tasks_number}"
        print("No tasks to process")
        exit(0)

    tasks = [task for task in tasks if task[0] + task[1] - 1 <= sprint_duration]
    print(tasks, ' - large tasks that are coming too late to be completed are removed')

    tasks_dict = {}
    for k, v in tasks:
        tasks_dict.setdefault(k, []).append(v)
        tasks_dict = dict(sorted(tasks_dict.items()))
    print(tasks_dict, ' - task durations, grouped and sorted by startDate')

    easier_tasks = []
    for start_date in tasks_dict:
        easier_tasks.append([start_date, min(tasks_dict[start_date])])
    print(easier_tasks, ' smaller tasks')

    for curr_task in easier_tasks:
        curr_task[1] = curr_task[0] + curr_task[1] - 1
    print(easier_tasks, ' - tasks converted to startDate - endDate')

    easier_tasks.sort(key = lambda et: et[1])
    print(easier_tasks, ' - tasks, sorted by endDate')

    completed_tasks = []
    if easier_tasks: completed_tasks = [easier_tasks[0]]
    for task in easier_tasks[1:]:
        if task[0] > completed_tasks[len(completed_tasks)-1][1]:
            completed_tasks.append(task)

    print(expected_tasks_number, ' - expected complete tasks number')
    print(expected_tasks, ' - expected_tasks')
    print(completed_tasks, ' - actual completed tasks')

    assert expected_tasks_number == len(completed_tasks), f"Expected {expected_tasks_number}, but got {len(completed_tasks)}"
    assert completed_tasks == expected_tasks, "Completed tasks do not match expected output"
