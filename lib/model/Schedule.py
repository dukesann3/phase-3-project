#lib/model/Schedule.py
from model.Task import Task
from model.__init__ import CURSOR, CONN

class Schedule:

    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):   
        if isinstance(name, str) and len(name) > 0:
            self._name = name
        else:
            raise TypeError("Name must be a string and not empty")
    
    def tasks(self):
        return [task for task in Task.all if task.schedule == self]
        
