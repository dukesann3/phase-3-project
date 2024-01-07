
from helpers import (
    exit_program,
    display_all_schedules,
    add_new_schedule,
    delete_schedule,
    edit_schedule,
    schedule_search_by_name,
    display_all_tasks_in_schedule,
    task_search_by_name,
    task_search_by_start_and_end_time,
    populate_all_dict,
    add_new_task_to_schedule,
    remove_task_from_schedule,
    update_task_from_schedule
)

#add backspace and return to home functionalities please for each stage
#and also try to show all of (either task or schedule) after giving the user the choice of add/remove/editting their (task/schedule)

def main():
    while True:
        welcome_screen()

def welcome_screen():
    populate_all_dict()
    print("\nWELCOME TO SCHEDULING CLI SOFTWARE")
    input("Press any key to continue ")
    schedule_or_task_screen()

def schedule_or_task_screen():
    print("\nPLEASE CHOOSE THE FOLLOWING SCHEDULE OR TASK TO EXPLORE")
    print("SCHEDULE        | PRESS 1")
    print("TASK            | PRESS 2")
    print("=====================================================================")
    print("PREVIOUS SCREEN | PRESS B")
    print("WELCOME SCREEN  | PRESS H\n")
    user_input = input("Please Choose the Following to Continue: ")

    if user_input == "1":
        schedule_chooser_screen()
    elif user_input == "2":
        #go to task chooser screen
        pass
    elif user_input.upper() == "B" or "H":
        welcome_screen()
    else:
        schedule_or_task_screen()

def schedule_chooser_screen():
    print("\nPLEASE CHOOSE THE FOLLOWING METHODS OF SELECTING SCHEDULE")
    print("DISPLAY ALL SCHEDULE(S) IN DB | PRESS 1")
    print("SEARCH SCHEDULE VIA NAME      | PRESS 2")
    print("=====================================================================")
    print("PREVIOUS SCREEN               | PRESS B")
    print("WELCOME SCREEN                | PRESS H\n")
    user_input = input("Please Choose the Following to Continue: ")

    if user_input == "1":

        display_all_schedules()
        input("PRESS ANY BUTTON TO CONTINUE CHOOSING SCHEDULE")
        schedule_chooser_screen()

    elif user_input == "2":

        schedule_name = input("PLEASE ENTER SCHEDULE NAME HERE: ")
        found_schedule = schedule_search_by_name(schedule_name)
        if found_schedule:
            edit_current_schedule_or_search_for_tasks_screen(found_schedule)
        else:
            schedule_chooser_screen()

    elif user_input.upper() == "B":
        schedule_or_task_screen()
    elif user_input.upper() == "H":
        welcome_screen()
    else:
        schedule_chooser_screen()

def edit_current_schedule_or_search_for_tasks_screen(schedule):
    print(f"\nSCHEDULE {schedule.name} OPTION BELOW")
    print("ADD NEW SCHEDULE TO DATABASE                    | PRESS 1")
    print("REMOVE (THIS) SCHEDULE                          | PRESS 2")
    print("EDIT (THIS) SCHEDULE                            | PRESS 3")
    print("=====================================================================")
    print("TASK SEARCH OPTION BELOW")
    print("SEE ALL TASKS IN SCHEDULE                       | PRESS 4")
    print("ADD NEW TASK TO SCHEDULE                        | PRESS 5")
    print("SEARCH TASKS IN SCHEDULE VIA TASK NAME          | PRESS 6")
    print("SEARCH TASKS IN SCHEDULE VIA START AND END TIME | PRESS 7")
    print("=====================================================================")
    print("PREVIOUS SCREEN                                 | PRESS B")
    print("WELCOME SCREEN                                  | PRESS H\n")
    user_input = input("Please Choose the Following to Continue: ")

    if user_input == "1":

        new_schedule_name = input("PLEASE ENTER NEW SCHEDULE NAME: ")
        add_new_schedule(new_schedule_name)
        edit_current_schedule_or_search_for_tasks_screen(schedule)

    elif user_input == "2":
        
        delete_schedule(schedule)
        edit_current_schedule_or_search_for_tasks_screen(schedule)

    elif user_input == "3":

        edit_schedule(schedule)
        edit_current_schedule_or_search_for_tasks_screen(schedule)

    elif user_input == "4":

        display_all_tasks_in_schedule(schedule)
        input("PLEASE PRESS ANY BUTTON TO CONTINUE")
        edit_current_schedule_or_search_for_tasks_screen(schedule)

    elif user_input == "5":

        add_new_task_to_schedule(schedule)
        edit_current_schedule_or_search_for_tasks_screen(schedule)

    elif user_input == "6":

        task_name = input("PLEASE ENTER TASK NAME HERE: ")
        found_task = task_search_by_name(task_name)
        if found_task:
            task_editor_screen(schedule, found_task)
            edit_current_schedule_or_search_for_tasks_screen(schedule)
        else:
            edit_current_schedule_or_search_for_tasks_screen(schedule)

    elif user_input == "7":

        task_start_time = input("PLEASE ENTER SEARCH START DATE HERE IN (MM/DD/YYYY) FORMAT: ")
        task_end_time = input("PLEASE ENTER SEARCH END DATE HERE IN (MM/DD/YYYY) FORMAT: ")

        found_task = task_search_by_start_and_end_time(task_start_time, task_end_time, schedule.id)
        if len(found_task) <= 0:
            task_editor_screen(schedule, found_task)
            edit_current_schedule_or_search_for_tasks_screen(schedule)

    elif user_input.upper() == "B":
        schedule_chooser_screen()
    elif user_input.upper() == "H":
        welcome_screen()
    else:
        edit_current_schedule_or_search_for_tasks_screen(schedule)

def task_chooser_screen(schedule):
    #should exclusively be used on every task chooser except for find by name
    print("SELECT TASK        | PRESS 1")
    print("EXIT TASK SELECTOR | PRESS ANY")

    user_input = input("Please Choose the Following to Continue: ")

    if user_input == "1":
        task = input("Please Enter Task Name to Edit Task")
        found_task = task_search_by_name(task)
        if found_task:
            task_editor_screen(schedule, task)
            edit_current_schedule_or_search_for_tasks_screen(schedule)
        else:
            task_chooser_screen(schedule)
    else:
        edit_current_schedule_or_search_for_tasks_screen(schedule)

def task_editor_screen(schedule, task):
    print(f"\nTASK {task.name} OPTION BELOW")
    print("REMOVE (THIS) SCHEDULE                          | PRESS 1")
    print("EDIT (THIS) SCHEDULE                            | PRESS 2")
    print("=====================================================================")
    print("PREVIOUS SCREEN                                 | PRESS B")
    print("WELCOME SCREEN                                  | PRESS H\n")

    user_input = input("Please Choose the Following to Continue: ")

    if user_input == "1":
        remove_task_from_schedule(task)
        edit_current_schedule_or_search_for_tasks_screen(schedule)
    elif user_input == "2":
        update_task_from_schedule(task)
        task_editor_screen(schedule, task)
    elif user_input.upper() == "B":
        edit_current_schedule_or_search_for_tasks_screen(schedule)
    elif user_input.upper() == "H":
        welcome_screen()
    else:
        task_editor_screen(schedule, task)


##############################################################################################


if __name__ == "__main__":
    main()