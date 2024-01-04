from model.Schedule import Schedule
from model.Task import Task
from test import (print_all_property_of_obj)

def exit_program():
    print("Good bye!")
    exit()

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

def schedule_search_by_name(name):
    try:
        found_schedule = Schedule.find_by_name(name)
        print("1 RESULT FOUND \n")
        print(f"FOUND SCHEDULE WITH NAME: {found_schedule.name}\n")
        return found_schedule
    except Exception as error:
        print(f"\nAN ERROR OCCURRED: {error}\n")









    








