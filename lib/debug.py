from model.Schedule import Schedule
from model.Task import Task
import ipdb


def create_tables():
    Schedule.create_table()
    Task.create_table()

def reset_database():
    Task.drop_table()
    Schedule.drop_table()

def debugger():
    create_tables()
    print(f"\n"
          f"*************Debugger Commands********************************************\n"
          f"\n"
          f"reset_database():----------------Drops both schedule and task tables\n"
          f"\n"
          f"**************************************************************************\n")
    ipdb.set_trace()

debugger()



