
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
    update_task_from_schedule,
    display_all_tasks_in_db,
    task_search_by_start_and_end_time_in_db,
    space,
    long_border,
    find_schedule_w_index,
    find_task_w_index,
    find_task_in_schedule_w_index,
    create_schedule_task_table
)


#add backspace and return to home functionalities please for each stage
#and also try to show all of (either task or schedule) after giving the user the choice of add/remove/editting their (task/schedule)

def main():
    while True:
        create_schedule_task_table()
        welcome_screen()

def welcome_screen():
    populate_all_dict()
    space()
    print("WELCOME TO SCHEDULING CLI SOFTWARE")
    input("Press any key to continue ")
    space()
    schedule_or_task_screen()

def schedule_or_task_screen():
    print("PLEASE CHOOSE THE FOLLOWING SCHEDULE OR TASK TO EXPLORE")
    print("SCHEDULE        | PRESS 1")
    print("TASK            | PRESS 2")
    long_border()
    print("PREVIOUS SCREEN | PRESS B")
    print("WELCOME SCREEN  | PRESS H")
    print("EXIT PROGRAM    | PRESS X")
    space()
    user_input = input("Please Choose the Following to Continue: ")
    space()

    if user_input == "1":
        schedule_chooser_screen()
    elif user_input == "2":
        #go to task chooser screen
        search_for_tasks_screen_no_schedule()
    elif user_input.upper() == "B" or user_input.upper() == "H":
        welcome_screen()
    elif user_input.upper() == "X":
        exit_program()
    else:
        schedule_or_task_screen()

def schedule_chooser_screen():
    print("PLEASE CHOOSE THE FOLLOWING METHODS OF SELECTING SCHEDULE")
    print("DISPLAY ALL SCHEDULE(S) IN DB | PRESS 1")
    print("SEARCH SCHEDULE VIA NAME      | PRESS 2")
    print("ADD NEW SCHEDULE TO DATABASE  | PRESS 3")
    long_border()
    print("PREVIOUS SCREEN               | PRESS B")
    print("WELCOME SCREEN                | PRESS H")
    print("EXIT PROGRAM                  | PRESS X")
    space()
    user_input = input("Please Choose the Following to Continue: ")
    space()

    if user_input == "1":

        display_all_schedules()
        print("Enter Schedule Code to View Schedule")
        user_search_value = input("Or do not enter anything to go back: ")
        if user_search_value:
            #make new function to search for index in Schedule
            found_schedule = find_schedule_w_index(user_search_value)
            if found_schedule:
                edit_current_schedule_or_search_for_tasks_screen(found_schedule)
            else:
                schedule_chooser_screen()
        else:
            schedule_chooser_screen()

    elif user_input == "2":

        schedule_name = input("PLEASE ENTER SCHEDULE NAME HERE: ")
        found_schedule = schedule_search_by_name(schedule_name)
        if found_schedule:
            edit_current_schedule_or_search_for_tasks_screen(found_schedule)
        else:
            schedule_chooser_screen()
    elif user_input == "3":
        new_schedule_name = input("PLEASE ENTER NEW SCHEDULE NAME: ")
        add_new_schedule(new_schedule_name)
        schedule_chooser_screen()
    elif user_input.upper() == "B":
        schedule_or_task_screen()
    elif user_input.upper() == "H":
        welcome_screen()
    elif user_input.upper() == "X":
        exit_program()
    else:
        schedule_chooser_screen()

def edit_current_schedule_or_search_for_tasks_screen(schedule):
    print(f"SCHEDULE {schedule.name} OPTION BELOW")
    print("REMOVE (THIS) SCHEDULE                          | PRESS 1")
    print("EDIT (THIS) SCHEDULE                            | PRESS 2")
    long_border()
    print("TASK SEARCH OPTION BELOW")
    print("SEE ALL TASKS IN SCHEDULE                       | PRESS 3")
    print("ADD NEW TASK TO SCHEDULE                        | PRESS 4")
    print("SEARCH TASKS IN SCHEDULE VIA TASK NAME          | PRESS 5")
    print("SEARCH TASKS IN SCHEDULE VIA START AND END TIME | PRESS 6")
    long_border()
    print("PREVIOUS SCREEN                                 | PRESS B")
    print("WELCOME SCREEN                                  | PRESS H")
    print("EXIT PROGRAM                                    | PRESS X")
    space()
    user_input = input("Please Choose the Following to Continue: ")
    space()

    if user_input == "1":
        
        delete_schedule(schedule)
        schedule_chooser_screen()

    elif user_input == "2":

        edit_schedule(schedule)
        edit_current_schedule_or_search_for_tasks_screen(schedule)

    elif user_input == "3":
        display_all_tasks_in_schedule(schedule)
        print("Enter Task Code to view task")
        task_code = input("Or do not enter anything to go back: ")
        found_task = find_task_in_schedule_w_index(schedule, task_code)
        if found_task:
            task_editor_screen(schedule, found_task)
            edit_current_schedule_or_search_for_tasks_screen(schedule)
        else:
            edit_current_schedule_or_search_for_tasks_screen(schedule)
        edit_current_schedule_or_search_for_tasks_screen(schedule)

    elif user_input == "4":

        add_new_task_to_schedule(schedule)
        edit_current_schedule_or_search_for_tasks_screen(schedule)

    elif user_input == "5":

        task_name = input("PLEASE ENTER TASK NAME HERE: ")
        found_task = task_search_by_name(task_name)
        if found_task:
            task_editor_screen(schedule, found_task)
            edit_current_schedule_or_search_for_tasks_screen(schedule)
        else:
            edit_current_schedule_or_search_for_tasks_screen(schedule)

    elif user_input == "6":

        task_start_time = input("PLEASE ENTER SEARCH START DATE HERE IN (MM/DD/YYYY) FORMAT: ")
        task_end_time = input("PLEASE ENTER SEARCH END DATE HERE IN (MM/DD/YYYY) FORMAT: ")

        found_task = task_search_by_start_and_end_time(task_start_time, task_end_time, schedule.id)
        if found_task:
            task_chooser_screen(schedule)
            edit_current_schedule_or_search_for_tasks_screen(schedule)
        else:
            edit_current_schedule_or_search_for_tasks_screen(schedule)
    elif user_input.upper() == "B":
        schedule_chooser_screen()
    elif user_input.upper() == "H":
        welcome_screen()
    elif user_input.upper() == "X":
        exit_program()
    else:
        edit_current_schedule_or_search_for_tasks_screen(schedule)

def task_chooser_screen(schedule):
    #should exclusively be used on every task chooser except for find by name
    print("SELECT TASK        | PRESS 1")
    print("EXIT PROGRAM       | PRESS X")
    print("EXIT TASK SELECTOR | PRESS ANY")
    space()
    user_input = input("Please Choose the Following to Continue: ")
    space()

    if user_input == "1":
        task = input("Please Enter Task Name to Edit Task: ")
        found_task = task_search_by_name(task)
        if found_task:
            task_editor_screen(schedule, found_task)
            edit_current_schedule_or_search_for_tasks_screen(schedule)
        else:
            task_chooser_screen(schedule)
    elif user_input.upper == "X":
        exit_program()
    else:
        edit_current_schedule_or_search_for_tasks_screen(schedule)

def task_chooser_screen_no_schedule():
    print("SELECT TASK        | PRESS 1")
    print("EXIT PROGRAM       | PRESS X")
    print("EXIT TASK SELECTOR | PRESS ANY")
    space()
    user_input = input("Please Choose the Following to Continue: ")
    space()

    if user_input == "1":
        task = input("Please Enter Task Name to Edit Task: ")
        found_task = task_search_by_name(task)
        if found_task:
            task_editor_screen_no_schedule(found_task)
            search_for_tasks_screen_no_schedule()
        else:
            search_for_tasks_screen_no_schedule()
    elif user_input.upper() == "X":
        exit_program()
    else:
        search_for_tasks_screen_no_schedule()

def search_for_tasks_screen_no_schedule():
    print("SEE ALL TASKS IN DATABASE           | PRESS 1")
    print("SEARCH TASK VIA TASK NAME           | PRESS 2")
    print("SEARCH TASK VIA START AND END DATES | PRESS 3")
    long_border()
    print("PREVIOUS SCREEN                     | PRESS B")
    print("WELCOME SCREEN                      | PRESS H")
    print("EXIT PROGRAM                        | PRESS X")
    space()
    user_input = input("Please Choose the Following to Continue: ")
    space()

    if user_input == "1":
        display_all_tasks_in_db()
        print("Enter Task Code to view task")
        task_code = input("Or do not enter anything to go back: ")
        found_task = find_task_w_index(task_code)
        if found_task:
            task_editor_screen_no_schedule(found_task)
            search_for_tasks_screen_no_schedule()
        else:
            search_for_tasks_screen_no_schedule()
        search_for_tasks_screen_no_schedule()
    elif user_input == "2":
        task_name = input("PLEASE ENTER TASK NAME HERE: ")
        found_task = task_search_by_name(task_name)
        if found_task:
            task_editor_screen_no_schedule(found_task)
            search_for_tasks_screen_no_schedule()
        else:
            search_for_tasks_screen_no_schedule()
    elif user_input == "3":
        task_start_time = input("PLEASE ENTER SEARCH START DATE HERE IN (MM/DD/YYYY) FORMAT: ")
        task_end_time = input("PLEASE ENTER SEARCH END DATE HERE IN (MM/DD/YYYY) FORMAT: ")

        found_task = task_search_by_start_and_end_time_in_db(task_start_time, task_end_time)
        if found_task:
            task_chooser_screen_no_schedule()
            search_for_tasks_screen_no_schedule()
    elif user_input.upper() == 'B':
        schedule_or_task_screen()
    elif user_input.upper() == "H":
        welcome_screen()
    elif user_input.upper() == "X":
        exit_program()
    else:
        search_for_tasks_screen_no_schedule()

def task_editor_screen_no_schedule(task):
    print(f"TASK {task.name} OPTION BELOW")
    print("REMOVE (THIS) TASK                              | PRESS 1")
    print("EDIT (THIS) TASK                                | PRESS 2")
    long_border()
    print("PREVIOUS SCREEN                                 | PRESS B")
    print("WELCOME SCREEN                                  | PRESS H")
    print("EXIT PROGRAM                                    | PRESS X")

    space()
    user_input = input("Please Choose the Following to Continue: ")
    space()

    if user_input == "1":
        remove_task_from_schedule(task)
        task_editor_screen_no_schedule(task)
    elif user_input == "2":
        update_task_from_schedule(task)
        task_editor_screen_no_schedule(task)
    elif user_input.upper() == "B":
        search_for_tasks_screen_no_schedule()
    elif user_input.upper() == "H":
        welcome_screen()
    elif user_input.upper() == "X":
        exit_program()
    else:
        task_editor_screen_no_schedule(task)


def task_editor_screen(schedule, task):
    print(f"TASK {task.name} OPTION BELOW")
    print("REMOVE (THIS) TASK                              | PRESS 1")
    print("EDIT (THIS) TASK                                | PRESS 2")
    long_border()
    print("PREVIOUS SCREEN                                 | PRESS B")
    print("WELCOME SCREEN                                  | PRESS H")
    print("EXIT PROGRAM                                    | PRESS X")

    space()
    user_input = input("Please Choose the Following to Continue: ")
    space()

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
    elif user_input.upper() == "X":
        exit_program()
    else:
        task_editor_screen(schedule, task)


##############################################################################################


if __name__ == "__main__":
    main()