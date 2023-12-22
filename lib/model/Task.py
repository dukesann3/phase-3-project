# lib/model/Task.py
import re
from model.Schedule import Schedule
from model.__init__ import CURSOR, CONN

class Task:

    all = {}

    def __init__(self, date, time, duration, description, schedule_id):
        self.date = date
        self.time = time
        self.duration = duration
        self.description = description
        self.schedule_id = schedule_id

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
            raise TypeError("Date must be a string and be in MM/DD/YYYY format")
    
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
    def schedule_id(self):
        return self._schedule_id
    
    @schedule_id.setter
    def schedule_id(self, schedule_id):
        if isinstance(schedule_id, int):
            self._schedule_id = schedule_id
        else:
            raise TypeError("Schedule must be a Schedule object")
        
    @classmethod
    def create_table(cls):
        """Creates new table here"""
        sql = """
            CREATE TABLE IF NOT EXISTS Task(
                id PRIMARY KEY,
                date TEXT,
                time TEXT,
                duration INTEGER,
                description TEXT,
                schedule_id INTEGER,
                FOREIGN KEY (schedule_id) REFERENCES Schedule(id)
            );
        """
        CURSOR.execute(sql)
        CONN.commit()
    
    @classmethod
    def drop_table(cls):
        """Drops table here"""
        sql = """
            DROP TABLE IF EXISTS Task;
        """
        CURSOR.execute(sql)
        CONN.commit()

    # It is self instead of class because this is each row is specific to each instance
    def save(self):
        """add new rows into Task table"""
        sql = """
            INSERT INTO Task (date, time, duration, description, schedule_id)
            VALUES (?, ?, ?, ?, ?);
        """
        CURSOR.execute(sql, (self.date, self.time, self.duration, self.description, self.schedule_id))
        CONN.commit()

        #the last row's id is extracted from here
        self.id = CURSOR.lastrowid
        #last row id is now being used to index all={} and the key is the object instance itself.
        type(self).all[self.id] = self
        #This is a very good way of linking the id of the database instance with the object instance of the class

    @classmethod
    def create(cls, date, time, duration, description, schedule_id):
        new_task = cls(date, time, duration, description, schedule_id)
        new_task.save()
        return new_task
    
    @classmethod
    def instance_from_db(cls, row):
        #This is a method that ensures everything is consistent between Python and DB
        task = cls.all.get(row[0])
        if task:
            task._date = row[1]
            task._time = row[2]
            task._duration = row[3]
            task._description = row[4]
            task._schedule_id = row[5]
        else:
            task = cls(row[1], row[2], row[3], row[4], row[5])
            task.id = row[0]
            cls.all[task.id] = task
        return task
    
    @classmethod
    def get_all(cls):
        sql = """
            SELECT * FROM Task;
        """

        all_tasks = CURSOR.execute(sql).fetchall()

        return [cls.instance_from_db(task) for task in all_tasks]
    
    def update(self):
        sql = """
            UPDATE Task 
            SET date = ?, time = ?, duration = ?, description = ?, schedule_id = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.date, self.time, self.duration, self.description, self.schedule_id, self.id))
        CONN.commit()
        #if I update thru here, I will update the database and not the python class
        #that is where instance_from_db come in handy
        #because it will search for any values that do not match with python class and updates it on the spot.
        #the caveat is that the instance_from_db must be used every time the CLI is being called to SHOW the results 

    def delete(self):
        sql = """
            DELETE FROM Task
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()

    @classmethod
    def find_by_id(cls, id):
        sql = """
            SELECT * FROM Task
            WHERE id = ?
        """
        retrieved_task = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(retrieved_task) if retrieved_task else None
    
    @classmethod
    def find_by_name(cls, name):
        sql = """
            SELECT * FROM Task
            WHERE name = ?
        """
        retrieved_task = CURSOR.execute(sql, (name,)).fetchone()
        return cls.instance_from_db(retrieved_task) if retrieved_task else None

    @classmethod
    def find_by_date(cls, date):
        sql = """
            SELECT * FROM Task
            WHERE date = ?
        """
        retrieved_tasks = CURSOR.execute(sql, (date,)).fetchall()
        return [cls.instance_from_db(task) for task in retrieved_tasks if retrieved_tasks]
    

    








