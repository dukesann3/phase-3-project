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
    
print(time_setter_test("9:00am"))
print(time_setter_test("9:00AM"))
print(time_setter_test("09:00AM"))
print(time_setter_test("12:00PM"))
print(time_setter_test("13:40pm"))
print(time_setter_test("3:30aM"))





