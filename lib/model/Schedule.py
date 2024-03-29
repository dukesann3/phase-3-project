#lib/model/Schedule.py
from model.__init__ import CONN, CURSOR
from model.Task import Task

class Schedule:

    all = {}

    def __new__(cls, name):
        new_obj = super().__new__(cls)

        for key in cls.all:
            current_self = cls.all[key]
            name_ = current_self.name
            if name_.lower() == name.lower():
                raise ValueError(f"This name: {name} has already been used. Cannot have duplicate")
        
        return new_obj

    def __init__(self, name):
        self.name = name
    
    def __repr__(self):
        return (f"Schedule Id:   {self.id}\n"
                f"Schedule Name: {self.name}")

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
            CREATE TABLE IF NOT EXISTS schedule(
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
            DROP TABLE IF EXISTS schedule;
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        """Creates new row for schedule table"""
        sql = """
            INSERT INTO schedule (name)
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
            SELECT * FROM schedule;
        """
        all_schedules = CURSOR.execute(sql).fetchall()

        #iterates over all the rows in the schedule table and makes sure every instance/row is up-to-date
        return [cls.instance_from_db(schedule) for schedule in all_schedules]

    #CHECK AND DELETE 
    @classmethod
    def no_return_get_all(cls):
        sql = """
            SELECT * FROM schedule;
        """
        all_schedules = CURSOR.execute(sql).fetchall()
        for schedule in all_schedules:
            cls.instance_from_db(schedule)
        
    def update(self, name):
        #loops through all dictionary to see if the name has already been used in the past
        for key in type(self).all:
            current_self = type(self).all[key]
            name_ = current_self.name
            if name == name_:
                raise ValueError(f"This name: {name} has already been used. Cannot have duplicate")
    
        sql = """
            UPDATE schedule 
            SET name = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (name, self.id))
        CONN.commit()
        sql_fetch = """
            SELECT * FROM schedule
            WHERE id = ?
        """
        updated_task = CURSOR.execute(sql_fetch, (self.id, )).fetchone()
        return type(self).instance_from_db(updated_task) 

    def delete(self):
        sql = """
            DELETE FROM schedule
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()
        del type(self).all[self.id]
    
    @classmethod
    def find_by_name(cls, name):
        sql = """
            SELECT * FROM schedule
            WHERE name = ?
        """
        retrieved_schedule = CURSOR.execute(sql, (name,)).fetchone()
        if retrieved_schedule:
            return cls.instance_from_db(retrieved_schedule) if retrieved_schedule else None
        else: 
            raise NameError(f"\"{name}\" DOES NOT EXIST IN DATABASE")


    def tasks(self):
        from model.Task import Task
        sql = """
            SELECT * FROM task
            WHERE schedule_id = ?
        """
        retrieved_tasks = CURSOR.execute(sql, (self.id,)).fetchall()
        return [Task.instance_from_db(task) for task in retrieved_tasks if retrieved_tasks]


    




    

