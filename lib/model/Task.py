# lib/model/Task.py

import re
from model.__init__ import CURSOR, CONN
from date_parser import start_time_to_int, end_time_to_int

class Task:

    all = {}

    def __new__(cls, name, date, time, duration, description, schedule_id):
        #need comparison function in here

        new_obj = super().__new__(cls)

        new_start_time = start_time_to_int(date, time)
        new_end_time = end_time_to_int(date, time, duration)

        for key in cls.all:
            current_self = cls.all[key]
            date_ = current_self.date
            time_ = current_self.time
            duration_ = current_self.duration
            name_ = current_self.name

            start_time = start_time_to_int(date_, time_)
            end_time = end_time_to_int(date_, time_, duration_)

            if start_time <= new_start_time <= end_time or start_time <= new_end_time <= end_time or (new_start_time < start_time and new_end_time > end_time):
                raise ValueError("This combination of date, time, and duration cannot be processed because it interferes with other schedules")
            if name_ == name:
                raise ValueError("This name has been used already. Please choose a different name")
            
        return new_obj


    def __init__(self, name, date, time, duration, description, schedule_id):
        self.name = name
        self.date = date
        self.time = time
        self.duration = duration
        self.description = description
        self.schedule_id = schedule_id
    
    def __repr__(self):
        return (f"\nTASK NAME: {self.name}\n"
                f"TASK DATE: {self.date}\n"
                f"TASK START TIME: {self.time}\n"
                f"TASK DURATION: {self.duration}\n"
                f"TASK DESCRIPTION: {self.description}\n")

    @classmethod
    def start_end_time_comparator(cls, name, date, time, duration, schedule_id):
        #need to exclude search of current id...
        new_start_time = start_time_to_int(date, time)
        new_end_time = end_time_to_int(date, time, duration)

        for key in cls.all:
            if cls.all[key].name == name and cls.all[key].schedule_id == schedule_id:
                #ignores loop if loop is at current id.
                continue
            current_self = cls.all[key]
            date_ = current_self.date
            time_ = current_self.time
            duration_ = current_self.duration
            name_ = current_self.name

            start_time = start_time_to_int(date_, time_)
            end_time = end_time_to_int(date_, time_, duration_)

            if start_time <= new_start_time <= end_time or start_time <= new_end_time <= end_time or (new_start_time < start_time and new_end_time > end_time):
                raise ValueError("This combination of date, time, and duration cannot be processed because it interferes with other schedules")
            if name_ == name:
                raise ValueError("This name has been used already. Please choose a different name")
            
        return True

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name) > 0:
            self._name = name
        else:
            raise TypeError("Name must be a string longer than 0 characters")

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
                id INTEGER PRIMARY KEY,
                name TEXT,
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
            INSERT INTO Task (name, date, time, duration, description, schedule_id)
            VALUES (?, ?, ?, ?, ?, ?);
        """
        CURSOR.execute(sql, (self.name, self.date, self.time, self.duration, self.description, self.schedule_id))
        CONN.commit()

        #the last row's id is extracted from here
        self.id = CURSOR.lastrowid
        #last row id is now being used to index all={} and the key is the object instance itself.
        type(self).all[self.id] = self
        #This is a very good way of linking the id of the database instance with the object instance of the class

    @classmethod
    def create(cls, name, date, time, duration, description, schedule_id):
        new_task = cls(name, date, time, duration, description, schedule_id)
        new_task.save()
        return new_task
    
    @classmethod
    def instance_from_db(cls, row):
        #This is a method that ensures everything is consistent between Python and DB
        #Also want to make sure that schedule and tasks do not interfere in the calendar
        task = cls.all.get(row[0])
        if task:
            task._name = row[1]
            task._date = row[2]
            task._time = row[3]
            task._duration = row[4]
            task._description = row[5]
            task._schedule_id = row[6]
        else:
            task = cls(row[1], row[2], row[3], row[4], row[5], row[6])
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
    
    @classmethod
    def no_return_get_all(cls):
        sql = """
            SELECT * FROM Task;
        """

        all_tasks = CURSOR.execute(sql).fetchall()
        for task in all_tasks:
            cls.instance_from_db(task)

    
    def update(self, name, date, time, duration, description):
        #should compare variables first then update the thing right? Pretty stupid if I didn't??????

        type(self).start_end_time_comparator(name, date, time, duration, self.schedule_id)
        sql = """
            UPDATE Task 
            SET name = ?, date = ?, time = ?, duration = ?, description = ?, schedule_id = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (name, date, time, duration, description, self.schedule_id, self.id))
        CONN.commit()
        sql_fetch = """
            SELECT * FROM Task
            WHERE id = ? AND schedule_id = ?
        """
        updated_task = CURSOR.execute(sql_fetch, (self.id, self.schedule_id)).fetchone()
        return type(self).instance_from_db(updated_task) 


    def delete(self):
        sql = """
            DELETE FROM Task
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()
        del type(self).all[self.id]

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

    @classmethod
    def find_by_time(cls, time):
        sql = """
            SELECT * FROM Task
            WHERE time = ?
        """
        retrieved_tasks = CURSOR.execute(sql, (time,)).fetchall()
        return [cls.instance_from_db(task) for task in retrieved_tasks if retrieved_tasks]
    
    @classmethod
    def find_by_start_and_end_time_ind(cls, start_time, end_time, schedule_id):

        task_bucket = []

        start = start_time_to_int(start_time, "12:00am")
        end = start_time_to_int(end_time, "12:00am")

        for key in cls.all:
            current_self = cls.all[key]
            date_ = current_self.date
            time_ = current_self.time
            duration_ = current_self.duration

            A = start_time_to_int(date_, time_)
            B = end_time_to_int(date_, time_, duration_)

            if current_self.schedule_id == schedule_id:
                if start <= A <= end or start <= B <= end or (A < start and B > end):
                    task_bucket.append(cls.all[key])

        return task_bucket




    
    

    








