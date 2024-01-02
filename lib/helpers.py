from model.Schedule import Schedule
from model.Task import Task
from test import (print_all_property_of_obj)

def exit_program():
    print("Good bye!")
    exit()

def display_all_schedules():
    all_schedule = Schedule.get_all()
    for schedule in all_schedule:
        print("\n")
        print(schedule)
        if schedule == all_schedule[-1]:
            print("\n")


def select_schedule():
    #select individual schedule by name
    schedule_name = input("Please type in schedule to select: ")
    selected_schedule = Schedule.find_by_name(schedule_name)

    if selected_schedule:
        show_details_in_schedule(selected_schedule)
    else:
        exit_program()

def show_details_in_schedule(selected_schedule):
    #show pretty much everything that is in the schedule
    
    all_tasks = selected_schedule.tasks()
    for task in all_tasks:
        print(task)
        #try to print task as a table
    
    #add code that asks if user wants to delete task, add task, or edit task.
    #need task id for this
    select_specific_task(all_tasks)

def select_specific_task(all_tasks):
    task_name = input("Please enter task name to select task: ")
    for task in all_tasks:
        if task_name == task.name:
            what_to_do_with_tasks(task)

    print(f"Task name {task_name} has not been found")
    select_specific_task(all_tasks)

def what_to_do_with_tasks(task):
    print("Choose the following: ")
    print("1. Add New Task To Schedule")
    print("2. Delete Task From Schedule")
    print(f"3. Edit Selected Task: {task.name}")
    print("Any other key to exit")

    user_input = input("Please choose task action: ")

    if user_input == "1":
        add_new_task_to_schedule(task)
    elif user_input == "2":
        remove_task_from_schedule(task)
    elif user_input == "3":
        update_task_from_schedule(task)
    elif user_input == "test":
        print_all_property_of_obj(task)
    else:
        exit_program()

    exit_program()

def add_new_task_to_schedule(task):
    #schedule id should come from task.schedule_id
    task_name = input("Enter Task Name: ")
    task_date = input("Enter Task Date: ")
    task_time = input("Enter Task Start Time: ")
    task_duration = input("Enter Task Duration: ")
    task_description = input("Enter Task Description: ")

    task_duration = float(task_duration)

    new_task = Task.create(task_name, task_date, task_time, task_duration, task_description, task.schedule_id)
    print("Added New Task: ")
    print(new_task)
    what_to_do_with_tasks(task)

def remove_task_from_schedule(task):
    if task:
        print("Successfully deleted Task: \n")
        print(task)
        task.delete()
    else:
        print("Task cannot be deleted")
        what_to_do_with_tasks(task)
    
def update_task_from_schedule(task):
    #need to update the task.update function so it actually updates both database and python
    print("Update task: \n")
    print(task)
    print("Press Enter to copy values from task" )

    user_input_list = []
    user_input = ""

    for property, value in vars(task).items():
        if property.startswith("_") and not property == "id" and not property == "_schedule_id":
            clean_property = property[1:]
            user_input = input(f"Enter Task {clean_property}: ")
            if not user_input:
                user_input_list.append(value)
            else:
                user_input_list.append(user_input)

    if task.update(user_input_list[0], user_input_list[1], user_input_list[2], float(user_input_list[3]), user_input_list[4]):
        print("Task has been successfully updated: \n")
        print(task)
    
    what_to_do_with_tasks(task)




    








