from model.Schedule import Schedule
from model.Task import Task
import ipdb


def create_init_table():
    Schedule.create_table()
    Task.create_table()

    #creating seed data
    schedule = Schedule.create("Art Class")
    Task.create("Meeting@10am", "12/21/2023","10:00am",2,"Meeting with Steve the art class TA", schedule.id)
    Task.create("Convention@12am", "12/25/2023", "12:00am", 0.5, "Art convention meeting with Santa", schedule.id)
    Task.create("ArtOrientation9am", "01/09/2024", "09:00am", 3, "Orientation for Art Program", schedule.id)
    cooking_schedule = Schedule.create("Cooking Class")
    Task.create("CookingClass@12pm", "04/03/2025", "12:00pm", 1, "Cooking orientation at 12pm", cooking_schedule.id)
    Task.create("CookingEggs@4am", "05/02/2025", "04:00am", 3, "Cooking eggs at 4am", cooking_schedule.id)

def create_tables():
    Schedule.create_table()
    Task.create_table()

def drop_tables():
    Task.drop_table()
    Schedule.drop_table()

def drop_task_table():
    Task.drop_table()

def drop_schedule_table():
    Schedule.drop_table()

def create_schedule(name):
    try:
        Schedule.create(name)
    except Exception as error:
        print("AN ERROR HAS OCCURRED: ", error)

def create_task(name, date, time, duration, description, schedule_id):
    try:
        Task.create(name, date, time, float(duration), description, int(schedule_id))
    except Exception as error:
        print("AN ERROR HAS OCCURRED: ",error)

def show_all_schedules():
    all_schedule = Schedule.get_all()
    for schedule in all_schedule:
        print(schedule)

def show_all_tasks():
    all_task = Task.get_all()
    for task in all_task:
        print(task)


def debugger():
    create_tables()
    print(f"\n"
          f"*************Debugger Commands********************************************\n"
          f"\n"
          f"create_init_table():-------------Creates arbiturary tables for task and schedule\n"
          f"drop_tables():-------------------Drops both schedule and task tables\n"
          f"drop_task_table():---------------Drops only task table\n"
          f"drop_schedule_table():-----------Drops only schedule table\n"
          f"show_all_schedules():------------Displays all schedules in database\n"
          f"show_all_tasks():----------------Displays all tasks in database\n"
          f"create_schedule(name):-----------Creates new schedule\n"
          f"create_task(name, date, time, duration, description, schedule_id):-----------Creates new task\n"
          f"\n"
          f"**************************************************************************\n")
    ipdb.set_trace()

debugger()



