# Task Scheduler - Non-Postponeable and Postponeable Versions
This repository contains two Python programs for scheduling tasks in a sprint. The first version handles tasks that must be completed on their assigned start date (non-postponeable). The second version introduces flexibility, allowing tasks to be postponed to a later start date if they cannot be started on the originally assigned day.

## Features
### Common Features
Handles scheduling of tasks based on start date and duration.
Filters out tasks that cannot be completed within the sprint.
Compares the actual completed tasks with the expected output.
Provides detailed logs to track progress and transformations of tasks.
### Non-Postponeable Version (task_scheduler_no_postpones.py)
Tasks must be completed within the originally assigned start date.
Tasks are selected based on start and end dates to ensure no overlap, and only the tasks that can fit within the sprint are scheduled.
### Postponeable Version (task_scheduler_with_postpones.py)
Tasks can be postponed to a later start task_scheduler_with_postpones if their originally scheduled date conflicts with previously completed tasks.
Tasks are adjusted to start on the earliest available day, with the goal of completing as many tasks as possible within the sprint.
Input and Output File Format
Both programs read input tasks from a text file and compare the result with the expected output stored in another text file.

### Input Format (incomeTasksXX.txt)
First line: Test name or description (this is ignored in the code).
Each subsequent line: Two integers representing the task's start day and duration.

Example:

* Test 01
* 1 3
* 3 2
* 4 3

This defines:

Task 1 starts on day 1 and lasts for 3 days.
Task 2 starts on day 3 and lasts for 2 days.
Task 3 starts on day 4 and lasts for 3 days.
### Output Format (outcomeTasksXX.txt)
First line: Expected number of tasks completed.
Each subsequent line: Two integers representing the start day and end day of each completed task.

Example:

* 3
* 1 3
* 4 5
* 7 9

This means that 3 tasks were completed, starting and ending on the given days.

### Example Usage
Place the test data files (incomeTasksXX.txt and outcomeTasksXX.txt) in their respective folders (noPostpones for the non-postponeable version, and withPostpones for the postponeable version).

### Run the program:

#### For the non-postponeable version
python task_scheduler_no_postpones.py

#### For the postponeable version
python task_scheduler_with_postpones.py

The programs will print the processed task list, removed tasks, sorted tasks, and finally the completed tasks. If the result doesn't match the expected output, an assertion error will be raised.
### File Structure
* task_scheduler_no_postpones.py - Handles non-postponeable tasks.
* task_scheduler_with_postpones.py - Handles tasks that can be postponed.

test_data/noPostpones/incomeTasksXX.txt - Input task data for the non-postponeable scheduler.
test_data/noPostpones/outcomeTasksXX.txt - Expected output for the non-postponeable scheduler.
test_data/withPostpones/incomeTasksXX.txt - Input task data for the postponeable scheduler.
test_data/withPostpones/outcomeTasksXX.txt - Expected output for the postponeable scheduler.
### Error Handling
If the input task list is empty, the program will terminate with a message stating there are no tasks to process.
If the actual output doesn’t match the expected output, the program will raise an assertion error detailing the mismatch.
