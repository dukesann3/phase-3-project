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

def add_new_schedule(name):
    try:
        new_schedule = Schedule.create(name)
        print("Added New Schedule: \n")
        print(new_schedule)
    except Exception as error:
        print("An error has occurred: ", error)

def delete_schedule(schedule_name):
    schedule = Schedule.find_by_name(schedule_name)
    user_input = input("Are you sure you want to delete this? (y/n): ")
    if user_input.lower() == 'y':
        try:
            print("Successfully deleted Schedule: \n")
            print(schedule)
            schedule.delete()
        except Exception as error:
            print(f"\nAn error occurred: {error}\n")

def edit_schedule(schedule_name):
    #need property values for this class again
    schedule = Schedule.find_by_name(schedule_name)
    print("Update task: \n")
    print(schedule)
    print("Press Enter to copy values from task" )

    user_input_list = []
    user_input = ""

    for property, value in vars(schedule).items():
        if property.startswith("_") and not property == "id":
            clean_property = property[1:]
            user_input = input(f"Enter Task {clean_property}: ")
            if not user_input:
                user_input_list.append(value)
            else:
                user_input_list.append(user_input)

    try:
        schedule.update(user_input_list[0])
        print("Schedule has been successfully updated: \n")
        print(schedule)
    except Exception as error:
        print(f"\nAn error occurred: {error}\n")









    








