from model.Schedule import Schedule
from model.Task import Task
import sys, os

def exit_program():
    print("Good bye!")
    sys.exit()

def populate_all_dict():
    Schedule.no_return_get_all()
    Task.no_return_get_all()

def display_all_schedules():
    all_schedule = Schedule.get_all()
    border()
    for index, schedule in enumerate(all_schedule):
        space()
        display_schedule(schedule, index+1)
        if schedule == all_schedule[-1]:
            space()
    border()

def add_new_schedule(name):
    try:
        new_schedule = Schedule.create(name)
        print("ADDED NEW SCHEDULE: ")
        space()
        print(new_schedule)
    except Exception as error:
        space()
        print("AN ERROR HAS OCCURRED: ", error)
        space()

def delete_schedule(schedule):
    user_input = input("ARE YOU SURE YOU WANT TO DELETE THIS? (y/n): ")
    if user_input.lower() == 'y':
        try:
            print("DELETION SUCCESSFUL: ")
            space()
            print(schedule)
            schedule.delete()
        except Exception as error:
            space()
            print(f"AN ERROR HAS OCCURRED: {error}")
            space()

def edit_schedule(schedule):
    #need property values for this class again
    print("UPDATE SCHEDULE: ")
    space()
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
        print("SCHEDULE HAS BEEN SUCCESSFULLY UPDATED: ")
        space()
        print(schedule)
    except Exception as error:
        space()
        print(f"AN ERROR HAS OCCURRED: {error}")
        space()

def schedule_search_by_name(name):
    try:
        found_schedule = Schedule.find_by_name(name)
        print("1 RESULT FOUND ")
        space()
        print(f"FOUND SCHEDULE WITH NAME: {found_schedule.name}")
        space()
        return found_schedule
    except Exception as error:
        space()
        print("AN ERROR HAS OCCURRED: ", error)
        space()

def schedule_search_by_id(id):
    try:
        found_schedule = Schedule.find_by_id(id)
        print("1 RESULT FOUND ")
        space()
        print(f"FOUND SCHEDULE WITH SCHEDULE CODE: {found_schedule.id}")
        space()
        return found_schedule 
    except Exception as error:
        space()
        print("AN ERROR HAS OCCURRED: ", error)
        space()

def display_all_tasks_in_schedule(schedule):
    print(schedule)
    all_tasks = schedule.tasks()
    border()
    for index, task in enumerate(all_tasks):
        display_task(task, index+1)
    border()

def task_search_by_name(name):
    try:
        found_task = Task.find_by_name(name)
        print(found_task, name)
        print("1 RESULT FOUND ")
        space()
        print(f"FOUND TASK WITH NAME: {found_task.name}")
        space()
        return found_task
    except Exception as error:
        space()
        print("AN ERROR HAS OCCURRED: ", error)
        print("FOUND 0 RESULTS")
        space()

def task_search_by_id(id):
    try:
        found_task = Task.find_by_id(id)
        print(found_task, id)
        print("1 RESULT FOUND ")
        space()
        print(f"FOUND TASK WITH TASK CODE: {found_task.id}")
        space()
        return found_task
    except Exception as error:
        space()
        print("AN ERROR HAS OCCURRED: ", error)
        print("FOUND 0 RESULTS")
        space()


def task_search_by_start_and_end_time(start_time, end_time, schedule_id):
    try:
        found_tasks = Task.find_by_start_and_end_time_ind(start_time, end_time, schedule_id)
        print(f"{len(found_tasks)} RESULT(S) FOUND ")
        space()
        border()
        for task in found_tasks:
            print(task)
        border()
        return found_tasks
    except Exception as error:
        space()
        print("AN ERROR HAS OCCURRED: ", error)
        print("FOUND 0 RESULTS")
        space()

def add_new_task_to_schedule(selected_schedule):
    from model.Task import Task
    #schedule id should come from task.schedule_id
    task_name = input("Enter Task Name: ")
    task_date = input("Enter Task Date (MM/DD/YYYY format): ")
    task_time = input("Enter Task Start Time (##:##am/pm format): ")
    task_duration = input("Enter Task Duration (in hours): ")
    task_description = input("Enter Task Description: ")

    task_dict = {
        "name": task_name,
        "date": task_date,
        "time": task_time,
        "duration": task_duration,
        "description": task_description
    }

    try:
        for key in task_dict:
            if not task_dict[key]:
                raise ValueError(f"{key} must have a value")
            
        task_duration = float(task_duration)
        new_task = Task.create(task_name, task_date, task_time, task_duration, task_description, selected_schedule.id)
        print("TASK ADDED SUCCESSFULLY: ")
        space()
        print(new_task)
    except Exception as error:
        space()
        print(f"AN ERROR HAS OCCURRED: {error}")
        space()

def remove_task_from_schedule(task):
    user_input = input("Are you sure you want to delete this? (y/n): ")
    if user_input == 'y':
        try:
            print("Successfully deleted Task: ")
            space()
            print(task)
            task.delete()
        except Exception as error:
            space()
            print(f"AN ERROR HAS OCCURRED: {error}")
            space()

def update_task_from_schedule(task):
    #need to update the task.update function so it actually updates both database and python
    print("Update task: ")
    space()
    print(task)
    print("Press Enter to copy original values from task" )

    user_input_list = []
    user_input = ""

    #this part is the vetting process of the user's proposed parameters
    for property, value in vars(task).items():
        if property.startswith("_") and not property == "id" and not property == "_schedule_id":
            clean_property = property[1:]
            user_input = input(f"Enter Task {clean_property}: ")
            if not user_input:
                user_input_list.append(value)
            elif clean_property == "name" and user_input:
                try:
                    Task.name_checker(clean_property)
                    user_input_list.append(user_input)
                except Exception as error:
                    print(f"An error occurred: {error}")
            else:
                user_input_list.append(user_input)
    
    try:
        is_valid = Task.start_end_time_comparator(vars(task)["id"],user_input_list[1], user_input_list[2], float(user_input_list[3]),vars(task)["_schedule_id"])
        if is_valid:
            try:
                print("creating new task instance")
                task.update(user_input_list[0], user_input_list[1], user_input_list[2], float(user_input_list[3]), user_input_list[4])
                print("Task has been successfully updated: ")
                space()
                print(task)
            except Exception as error:
                space()
                print(f"An error occurred: {error}")
                space()
    except Exception as error:
        space()
        print(f"An error occurred: {error}")
        space()



def display_all_tasks_in_db():
    all_tasks = Task.get_all()
    border()
    for index, task in enumerate(all_tasks):
        display_task(task, index+1)
    border()

def task_search_by_start_and_end_time_in_db(start_time, end_time):
    try:
        found_tasks = Task.find_by_start_and_end_time(start_time, end_time)
        print(f"{len(found_tasks)} RESULT(S) FOUND ")
        space()
        border()
        for task in found_tasks:
            print(task)
        border()
        return found_tasks
    except:
        space()
        print("FOUND 0 RESULTS")
        space()

#Finds schedule in index
def find_schedule_w_index(index):
    #index is incremented by one.  Make sure to subtract it by one
    try:
        index = int(index)
        all_schedule = Schedule.get_all()
        chosen_schedule = all_schedule[index-1]
        space()
        display_schedule(chosen_schedule, index)
        space()
        return chosen_schedule
    except Exception as error:
        print("AN ERROR HAS OCCURRED: ", error)
        space()
        return False
    
#Finds task in index
def find_task_w_index(index):
    #index is incremented by one.  Make sure to subtract it by one
    try:
        index = int(index)
        all_tasks = Task.get_all()

        chosen_task = all_tasks[index-1]
        space()
        display_task_details(chosen_task)
        space()
        return chosen_task
    except Exception as error:
        space()
        print("AN ERROR HAS OCCURRED: ", error)
        space()
        return False
    
def find_task_in_schedule_w_index(schedule, index):
    try:
        index = int(index)
        all_tasks = schedule.tasks()

        chosen_task = all_tasks[index-1]
        space()
        display_task_details(chosen_task)
        space()
        return chosen_task
    except Exception as error:
        space()
        print("AN ERROR HAS OCCURRED: ", error)
        space()
        return False
        
#When viewing all tasks. Only show name and Task Code
def display_task(task, index):
    print(f"TASK CODE: {index}\n"
          f"TASK NAME: {task.name}\n")
    
#When viewing all schedules. Only show name and Schedule Code
def display_schedule(schedule, index):
    print(f"SCHEDULE CODE: {index}\n"
          f"SCHEDULE NAME: {schedule.name}")
    
#When viewing detailed tasks...
def display_task_details(task):
    print(f"TASK NAME: {task.name}\n"
          f"TASK DATE: {task.date}\n"
          f"TASK TIME: {task.time}\n"
          f"TASK DURATION: {task.duration}\n"
          f"TASK DESCRIPTION: {task.description}")

def space():
    print("")

def border():
    print("============================")

def long_border():
    print("=====================================================================")















    








