
from helpers import (
    exit_program,
    display_all_schedules,
    add_new_schedule,
    delete_schedule,
    edit_schedule
)


#add backspace and return to home functionalities please for each stage
#and also try to show all of (either task or schedule) after giving the user the choice of add/remove/editting their (task/schedule)


def main():
    while True:
        welcome_screen()

def welcome_screen():
    print("\nWELCOME TO SCHEDULING CLI SOFTWARE")
    input("Press any key to continue ")
    schedule_screen()

def schedule_screen():
    print("\nPlease choose the following: ")
    print("1. Add Schedule")
    print("2. Remove Schedule")
    print("3. Edit Schedule")
    print("4. Display all Schedule")
    print("5. Add/Remove/Edit Tasks in Schedule\n")

    user_input = input("Please choose the following to continue. ")
    user_input = int(user_input)

    if user_input == 1:
        schedule_name = input("\nPlease Enter New Schedule Name: ")

        add_new_schedule(schedule_name)
        schedule_screen()
    elif user_input == 2:
        print("All Schedules Listed Below: \n")

        display_all_schedules()
        user_input_2 = input("Enter Schedule Name Here: ")

        delete_schedule(user_input_2)
        schedule_screen()
    elif user_input == 3:
        print("All Schedules Listed Below: \n")

        display_all_schedules()
        user_input_2 = input("Enter Schedule Name Here: ")

        edit_schedule(user_input_2)
        schedule_screen()
    elif user_input == 4:
        display_all_schedules()
        print("Press \"H\" to Return Home")

        print("Press any other Key to go back to Pick Schedule Screen\n")

        user_input_2 = input("Please Choose Action: ")
        
        if user_input_2.upper() == "H":
            welcome_screen()
        else:
            schedule_screen()
    elif user_input == 5:
        display_all_schedules()
        select_schedule()
        
def select_schedule():
    #select individual schedule by name
    from model.Schedule import Schedule
    schedule_name = input("Please type in schedule to select: ")
    selected_schedule = Schedule.find_by_name(schedule_name)

    if selected_schedule:
        show_details_in_schedule(selected_schedule)
    else:
        print(f"Schedule: {schedule_name} cannot be found in database")
        #need a backspace or return to home after this
        exit_program()

def show_details_in_schedule(selected_schedule):
    #show pretty much everything that is in the schedule
    
    all_tasks = selected_schedule.tasks()
    print("======================================\n")
    for task in all_tasks:
        print(task)
        #try to print task as a table
    print("======================================")
    
    select_specific_task(all_tasks, selected_schedule)

def select_specific_task(all_tasks, selected_schedule):
    task_name = input("Please enter task name to select task: ")
    for task in all_tasks:
        if task_name == task.name:
            what_to_do_with_tasks(task, selected_schedule)

    print(f"Task name {task_name} has not been found")
    select_specific_task(all_tasks, selected_schedule)

def what_to_do_with_tasks(task, selected_schedule):
    print("\nChoose the following: ")
    print("1. Add New Task To Schedule")
    print(f"2. Delete Selected Task: {task.name}")
    print(f"3. Edit Selected Task: {task.name}")
    print("Press \"H\" to Return Home")
    print("Press any other Key to go back to Pick Schedule Screen\n")

    user_input = input("Please Choose Action: ")
    if user_input == "1":
        add_new_task_to_schedule(task, selected_schedule)
    elif user_input == "2":
        remove_task_from_schedule(task, selected_schedule)
    elif user_input == "3":
        update_task_from_schedule(task, selected_schedule)
    elif user_input.upper() == "H":
        welcome_screen()
    else:
        schedule_screen()


def add_new_task_to_schedule(task, selected_schedule):
    from model.Task import Task
    #schedule id should come from task.schedule_id
    task_name = input("Enter Task Name: ")
    task_date = input("Enter Task Date: ")
    task_time = input("Enter Task Start Time: ")
    task_duration = input("Enter Task Duration: ")
    task_description = input("Enter Task Description: ")

    task_duration = float(task_duration)

    try:
        new_task = Task.create(task_name, task_date, task_time, task_duration, task_description, task.schedule_id)
        print("Added New Task: \n")
        print(new_task)
    except Exception as error:
        print(f"\nAn error occurred: {error}\n")

    what_to_do_with_tasks(task, selected_schedule)

def remove_task_from_schedule(task, selected_schedule):
    user_input = input("Are you sure you want to delete this? (y/n): ")
    if user_input == 'y':
        try:
            print("Successfully deleted Task: \n")
            print(task)
            task.delete()
        except Exception as error:
            print(f"\nAn error occurred: {error}\n")

    what_to_do_with_tasks(task, selected_schedule)
    
def update_task_from_schedule(task, selected_schedule):
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
    
    try:
        task.update(user_input_list[0], user_input_list[1], user_input_list[2], float(user_input_list[3]), user_input_list[4])
        print("Task has been successfully updated: \n")
        print(task)
    except Exception as error:
        print(f"\nAn error occurred: {error}\n")
    
    what_to_do_with_tasks(task, selected_schedule)












if __name__ == "__main__":
    main()