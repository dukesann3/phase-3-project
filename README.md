# Task-Schedule CLI

Task-Schedule CLI is an interface for Task-Schedule database. 

## Description

The Task-Schedule CLI allows the user to add, edit, and remove tasks and schedules. 
It also allows the user to display various tasks and schedules. 

Each task will belong to a schedule with a one to one relationship. Meaning, a task cannot belong to multiple schedules.

## Usage

There is one thing the client/user has to do to start using this product.

Please type in the command line...
```bash
python lib/debug.py
```
This command populates the schedule and task database.

To run the Task-Schedule CLI, type in command line...
```bash
python lib/cli.py
```

## How to Use

When first firing up the CLI, the user will be taken to a screen with 2 main options: Schedule and Task.

Selecting Schedule will allow the user to display all schedules in the database or search for a particular schedule.

When searching for a schedule, if the schedule exists in the database, it will take the user to a new screen where now the user will have the option to:
1. Add new schedule to database
2. Remove this schedule from database
3. Edit this schedule
4. Ddisplay all tasks in this schedule
5. Add new task to schedule
6. Search tasks in schedule via task name
7. Search tasks in schedule via start and end dates.

Options 1 to 5 is self explanatory.
For option 6, it is a similar method as searching for schedules but this time it is searching for a particular task by its name.
For option 7, the CLI will take in a range of start date and end date, and it will find all tasks that are within that range. 

Through options 6 and 7, once a particular task is selected, it will take the user to a new screen prompting for actions to be taken on that task. The the user will have the option to:
1. Remove Task
2. Edit Task

...

Now if the user selects Task instead of Schedule in the beginning, it will take the user to a screen that gives the options:
1. Display all Tasks in database
2. Search tasks in schedule via task name
3. Search tasks in schedule via start and end dates.

The only notable difference from the previous example is that the first option gets all tasks in the database instead of all tasks in a specific schedule.

...

Note, the user has the ability to:
1. Go back to previous screen
2. Go back to welcome screen
3. Exit program
At all points in the CLI.

# Rules

When adding new schedules, the name of the schedule cannot interfere with any schedule names in the database.
This is also the same for tasks as well. Task and Schedule cannot have duplicates.

When adding a new task, the task name cannot be previously used, start date of task must be in MM/DD/YYYY format, start time of task must be in ##:##am/pm format, and duration must be a number.













