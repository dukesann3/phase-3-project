import re

def time_setter_test(time):
    time = time.lower()

    global_pattern = r"(0[1-9]|1[0-2]|[1-9]):[0-5][0-9](a|p)m"
    no_front_zero = r"[1-9]:[0-5][0-9](a|p)m"

    global_pattern_regex = re.compile(global_pattern)
    no_front_zero_regex = re.compile(no_front_zero)

    if isinstance(time, str) and bool(global_pattern_regex.fullmatch(time)):
        if bool(no_front_zero_regex.fullmatch(time)):
            time = "0" + time
        return time
    else:
        raise ValueError("Time is not in correct format")
    
def date_setter_test(date):
    global_pattern = r"(0[1-9]|1[0-2]|[1-9])/(0[1-9]|1[0-9]|2[0-9]|3[0-1]|[1-9])/20[0-9][0-9]"
    global_pattern_regex = re.compile(global_pattern)

    date_list = re.split(r"/", date)
    index_of_non_zero_front = [count for count, component in enumerate(date_list) if len(component) < 2]

    if isinstance(date, str) and global_pattern_regex.fullmatch(date):
        if len(index_of_non_zero_front) > 0:
            for index in index_of_non_zero_front:
                date_list[index] = "0" + date_list[index]
            date = '/'.join(date_list)
        #replace date with self._date = date 
        return date
    else:
        raise ValueError("Date must be a string and be in MM/DD/YYYY format")
    
def error_1():
    raise TypeError("This is incorrect type")

def error_2():
    raise ValueError("This is incorrect value")

def error_tester():
    try:
        error_1()
    except Exception as error:
        print("An error occurred: ", error)
    
    try:
        error_2()
    except Exception as error:
        print("An error occurred: ", error)



    








    
    






