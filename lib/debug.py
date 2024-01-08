from model.Schedule import Schedule
from model.Task import Task

def testing_create_table():
    Schedule.create_table()
    Task.create_table()

    #creating seed data
    schedule = Schedule.create("Art Class")
    Task.create("Meeting@10am", "12/21/2023","10:00am",2,"Meeting with Steve the art class TA", schedule.id)
    Task.create("Convention@12am", "12/25/2023", "12:00am", 0.5, "Art convention meeting with Santa", schedule.id)
    schedule.add_new_task("ArtOrientation9am", "01/09/2024", "09:00am", 3, "Orientation for Art Program")
    cooking_schedule = Schedule.create("Cooking Class")
    Task.create("CookingClass@12pm", "04/03/2025", "12:00pm", 1, "Cooking orientation at 12pm", cooking_schedule.id)
    Task.create("CookingEggs@4am", "05/02/2025", "04:00am", 3, "Cooking eggs at 4am", cooking_schedule.id)


testing_create_table()
