from helpers import (
    exit_program
)

def main():
    while True:
        welcome_screen()

def welcome_screen():
    print("WELCOME TO SCHEDULING CLI SOFTWARE")
    user_input = input("Press any key to continue ")
    if len(user_input) > 0:
        pass

def schedule_task_screen():
    print("Please choose the following:")
    print("1. Schedule")
    print("2. Task")
    user_input = input("Please choose the following to continue. ")
    if len(user_input) > 0 and not user_input == "0":
        print("yo it worked")
        exit_program()
    else:
        exit_program()
        #add new function here