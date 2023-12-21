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
    
    @classmethod
    def create_table(cls):
        """Creates a new table here"""
        sql = """
            CREATE TABLE IF NOT EXISTS Schedule(
                id INTEGER PRIMARY KEY,
                name TEXT
            )
        """
        CURSOR.execute(sql)
        CONN.commit()
        
    @classmethod
    def drop_table(cls):
        """Deletes table here"""
        sql = """
            DROP TABLE IF EXISTS Schedule
        """
        CURSOR.execute(sql)
        CONN.commit()

        