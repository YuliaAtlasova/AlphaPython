
if __name__ == '__main__':
    income_tasks = open('test_data/incomeTasks01.txt').read().split('\n')
    sprint_duration = 10
    tasks = []
    for line in income_tasks:
        curr_line = [int(x) for x in line.split()]
        tasks.append(curr_line)
    print(tasks, ' - Initial tasks list')
    for i in range(len(tasks)-1, -1, -1):
        if tasks[i][0] + tasks[i][1] > sprint_duration:
            del(tasks[i])
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
        curr_task[1] = curr_task[0]-1 + curr_task[1]
    print(easier_tasks, ' - tasks converted to startDate - endDate')
    easier_tasks.sort(key = lambda et: et[1])
    print(easier_tasks, ' - tasks, sorted by endDate')
    completed_tasks = []
    for task in easier_tasks:
        if len(completed_tasks) == 0:
            completed_tasks.append(task)
        else:
            if task[0] > completed_tasks[len(completed_tasks)-1][1]: 
                completed_tasks.append(task)
    print(completed_tasks, ' - completed tasks')
    outcome_tasks = open('test_data/outcomeTasks01.txt').read().split('\n')
    expected_tasks_number = int(outcome_tasks[0])
    expected_tasks = []
    for line in range (1, len(outcome_tasks)):
        curr_line = [int(x) for x in line.split()]
        expected_tasks.append(curr_line)
    print(expected_tasks_number, ' - expected_tasks_number')
    print(expected_tasks)
