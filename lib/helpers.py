from model.Schedule import Schedule
from model.Task import Task

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
    task_id = input("Choose the following tasks: ")
    what_to_do_with_tasks()
    pass

def what_to_do_with_tasks():
    print("1. Add Task")
    print("2. Delete Task")
    print("3. Edit Task")

    user_input = input("Please choose task action: ")

    if user_input == 1:
        pass
    elif user_input == 2:
        pass
    elif user_input == 3:
        pass
    else:
        exit_program()

    exit_program()




