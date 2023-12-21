# lib/model/Task.py
import re
from model.Schedule import Schedule
from model.__init__ import CURSOR, CONN

class Task:

    all = []

    def __init__(self, date, time, duration, schedule, description=""):
        self.date = date
        self.time = time
        self.duration = duration
        self.schedule = schedule
        self.description = description

    def __repr__(self):
        return f"Task Information: \nDate: {self.date}\nTime: {self.time}\nDuration: {self.duration} hours\nDescription: {self.description}"

    @property
    def date(self):
        return self._date
    
    @date.setter
    def date(self, date):
        allowable_date_pattern = r"(0[1-9]|1[0-2])/(0[1-9]|1[0-9]|2[0-9]|3[0-1])/20[0-9][0-9]"
        allowable_date_regex = re.compile(allowable_date_pattern)

        if isinstance(date, str) and bool(allowable_date_regex.fullmatch(date)):
            self._date = date
        else:
            raise TypeError("Date must be a string and be in MM/DD/YY format")
    
    @property
    def time(self):
        return self._time
    
    @time.setter
    def time(self, time):
        allowable_time_pattern = r"(0[1-9]|1[0-2]):[0-5][0-9](a|p)m"
        allowable_time_regex = re.compile(allowable_time_pattern)

        if isinstance(time, str) and allowable_time_regex.fullmatch(time):
            self._time = time
        else:
            raise TypeError("Time must be a string and be in ##:##am/pm format")
    
    @property
    def duration(self):
        return self._duration
    
    @duration.setter
    def duration(self, duration):
        if isinstance(duration, (int,float)):
            self._duration = duration
        else:
            raise TypeError("Duration must be an integer or float in terms of hours")
        
    @property
    def description(self):
        return self._description
    
    @description.setter
    def description(self, description):
        if isinstance(description, str):
            self._description = description
        else:
            raise TypeError("Description must be a string")
    
    @property
    def schedule(self):
        return self._schedule
    
    @schedule.setter
    def schedule(self, schedule):
        if isinstance(schedule, Schedule):
            self._schedule = schedule
        else:
            raise TypeError("Schedule must be a Schedule object")
        



