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









    








