
from helpers import (
    exit_program,
    display_all_schedules,
    select_schedule
)
#download getch or msvcrt when you have internet


def main():
    while True:
        welcome_screen()

def welcome_screen():
    print("WELCOME TO SCHEDULING CLI SOFTWARE")
    input("Press any key to continue ")
    schedule_task_screen()

def schedule_task_screen():
    print("Please choose the following:")
    print("1. Schedule")
    print("2. Task")
    user_input = input("Please choose the following to continue. ")
    user_input = int(user_input)

    if user_input == 1:
        #create a table or interface that allows users to interact with the schedule database
        schedule_screen()
    elif user_input == 2:
        #create a table or interface that allows users to interact with the task database
        exit_program()
    else:
        #print(f"{user_input} is type: {type(user_input)}")
        exit_program()
        #add new function here

def schedule_screen():
    print("Please choose the following: ")
    print("1. See All Schedules")
    print("2. Search for Schedule")

    user_input = input("Please choose the following to continue. ")
    user_input = int(user_input)

    if user_input == 1:
        display_all_schedules()
        select_schedule()
    elif user_input == 2:
        exit_program()
    else:
        exit_program()


if __name__ == "__main__":
    main()