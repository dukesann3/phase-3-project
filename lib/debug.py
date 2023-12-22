from model.Schedule import Schedule
from model.Task import Task

def testing_create_table():
    Schedule.create_table()
    Task.create_table()

    #creating seed data
    schedule = Schedule.create("Art Class")
    Task.create("12/21/2023","10:00am",2,"Meeting with Steve the art class TA", schedule.id)
    Task.create("12/25/2023", "12:00am", 0.5, "Art convention meeting with Santa", schedule.id)


testing_create_table()