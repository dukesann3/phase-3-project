#lib/model/Schedule.py
from model.__init__ import CURSOR, CONN
from model.Task import Task

class Schedule:

    all = {}

    def __new__(cls, name):
        new_obj = super().__new__(cls)

        for key in cls.all:
            if cls.all[key].name == name:
                raise ValueError("This name has already been used. Cannot have duplicate")
        
        return new_obj

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Schedule Name: {self.name} {self.id}"
    
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
            );
        """
        CURSOR.execute(sql)
        CONN.commit()
        
    @classmethod
    def drop_table(cls):
        """Deletes table here"""
        sql = """
            DROP TABLE IF EXISTS Schedule;
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        """Creates new row for Schedule table"""
        sql = """
            INSERT INTO Schedule (name)
            VALUES (?);
        """
        CURSOR.execute(sql, (self.name,))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    @classmethod
    def create(cls, name):
        new_schedule = cls(name)
        new_schedule.save()
        return new_schedule
    
    @classmethod
    def instance_from_db(cls, rows):
        #This is a method that ensures everything is consistent between Python and DB
        #rows is recieved from the database
        #code below grabs the specific schedule that is saved within the all dict by calling its self.id = rows[0]
        schedule = cls.all.get(rows[0])
        if schedule:
            #if this instance exists, then let's make sure that the name of it is consistent with the db value
            schedule.name = rows[1]
        else:
            #if this instance does not exist, 
            schedule = cls(rows[1])
            schedule.id = rows[0]
            #need to add this to the all dictionary. Very important
            cls.all[schedule.id] = schedule
        return schedule

    @classmethod
    def get_all(cls):
        sql = """
            SELECT * FROM Schedule;
        """
        all_schedules = CURSOR.execute(sql).fetchall()

        #iterates over all the rows in the schedule table and makes sure every instance/row is up-to-date
        return [cls.instance_from_db(schedule) for schedule in all_schedules]
        
    def update(self):
        sql = """
            UPDATE Schedule 
            SET name = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.name, self.id))
        CONN.commit()

    def delete(self):
        sql = """
            DELETE FROM Schedule
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()

    @classmethod
    def find_by_id(cls, id):
        sql = """
            SELECT * FROM Schedule
            WHERE id = ?
        """
        retrieved_schedule = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(retrieved_schedule) if retrieved_schedule else None
    
    @classmethod
    def find_by_name(cls, name):
        sql = """
            SELECT * FROM Schedule
            WHERE name = ?
        """
        retrieved_schedule = CURSOR.execute(sql, (name,)).fetchone()
        return cls.instance_from_db(retrieved_schedule) if retrieved_schedule else None

    def tasks(self):
        from model.Task import Task
        sql = """
            SELECT * FROM Task
            WHERE schedule_id = ?
        """
        retrieved_tasks = CURSOR.execute(sql, (self.id,)).fetchall()
        return [Task.instance_from_db(task) for task in retrieved_tasks if retrieved_tasks]

    def add_new_task(self, date, time, duration, description):
        new_task = Task(date, time, duration, description, self.id)
        new_task.save()
        return new_task
    
    #need to create function that doesn't allow same name schedule to be created

    

