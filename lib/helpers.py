from model.Schedule import Schedule
from model.Task import Task
from test import (print_all_property_of_obj)

def exit_program():
    print("Good bye!")
    exit()

def populate_all_dict():
    Schedule.no_return_get_all()
    Task.no_return_get_all()


def display_all_schedules():
    all_schedule = Schedule.get_all()
    print("============================")
    for schedule in all_schedule:
        print("\n")
        print(schedule)
        if schedule == all_schedule[-1]:
            print("\n")
    print("============================")

def add_new_schedule(name):
    try:
        new_schedule = Schedule.create(name)
        print("ADDED NEW SCHEDULE: \n")
        print(new_schedule)
    except Exception as error:
        print("AN ERROR HAS OCCURRED: ", error)

def delete_schedule(schedule):
    user_input = input("ARE YOU SURE YOU WANT TO DELETE THIS? (y/n): ")
    if user_input.lower() == 'y':
        try:
            print("DELETION SUCCESSFUL: \n")
            print(schedule)
            schedule.delete()
        except Exception as error:
            print(f"\nAN ERROR HAS OCCURRED: {error}\n")

def edit_schedule(schedule):
    #need property values for this class again
    print("UPDATE SCHEDULE: \n")
    print(schedule)
    print("PRESS ENTER TO COPY ORIGINAL VALUE OF SCHEDULE" )
    print("INPUT NEW VALUE TO REPLACE ORIGINAL VALUE")

    user_input_list = []
    user_input = ""

    for property, value in vars(schedule).items():
        if property.startswith("_") and not property == "id":
            clean_property = property[1:]
            user_input = input(f"ENTER SCHEDULE {clean_property}: ")
            if not user_input:
                user_input_list.append(value)
            else:
                user_input_list.append(user_input)

    try:
        schedule.update(user_input_list[0])
        print("SCHEDULE HAS BEEN SUCCESSFULLY UPDATED: \n")
        print(schedule)
    except Exception as error:
        print(f"\nAN ERROR HAS OCCURRED: {error}\n")

def schedule_search_by_name(name):
    try:
        found_schedule = Schedule.find_by_name(name)
        print("1 RESULT FOUND \n")
        print(f"FOUND SCHEDULE WITH NAME: {found_schedule.name}\n")
        return found_schedule
    except Exception as error:
        print("AN ERROR HAS OCCURRED: ", error)

def display_all_tasks_in_schedule(schedule):
    all_tasks = schedule.tasks()
    print("============================")
    for task in all_tasks:
        print(task)
    print("============================")

def task_search_by_name(name):
    try:
        found_task = Task.find_by_name(name)
        print("1 RESULT FOUND \n")
        print(f"FOUND TASK WITH NAME: {found_task.name}\n")
        return found_task
    except:
        print("FOUND 0 RESULTS")


def task_search_by_start_and_end_time(start_time, end_time, schedule_id):
    try:
        found_tasks = Task.find_by_start_and_end_time_ind(start_time, end_time, schedule_id)
        print(f"{len(found_tasks)} RESULT(S) FOUND \n")
        print("============================")
        for task in found_tasks:
            print(task)
        print("============================")
        return found_tasks
    except:
        print("FOUND 0 RESULTS")

def add_new_task_to_schedule(selected_schedule):
    from model.Task import Task
    #schedule id should come from task.schedule_id
    task_name = input("Enter Task Name: ")
    task_date = input("Enter Task Date: ")
    task_time = input("Enter Task Start Time: ")
    task_duration = input("Enter Task Duration: ")
    task_description = input("Enter Task Description: ")

    task_duration = float(task_duration)

    try:
        new_task = Task.create(task_name, task_date, task_time, task_duration, task_description, selected_schedule.id)
        print("Added New Task: \n")
        print(new_task)
    except Exception as error:
        print(f"\nAn error occurred: {error}\n")













    








