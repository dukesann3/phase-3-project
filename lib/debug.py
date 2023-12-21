from model.Schedule import Schedule
from model.Task import Task

def testing_create_table():
    Schedule.create_table()
    Task.create_table()

    #creating seed data