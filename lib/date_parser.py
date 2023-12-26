import re
import math

last_date_of_month = {"01": 31, "02": 28, "03": 31, "04": 30, "05": 31, 
                    "06": 30, "07": 31, "08": 31, "09": 30, "10": 31, "11": 30, "12": 31}

def parse_date(date):
    #this should return {month, date, year} dicitonary object
    date_pattern = r"\d+"
    date_pattern_regex = re.compile(date_pattern)

    date_list = re.findall(date_pattern_regex, date)
    month = date_list[0]
    day = date_list[1]
    year = date_list[2]

    if not last_date_of_month[month] or int(day) > last_date_of_month[month] or int(day) <= 0:
        raise ValueError(f"Invalid day and month combination or Invalid month")
    
    return {"month": int(month), "day": int(day), "year": int(year)}


def add_day(date, days_to_add):
    if not isinstance(days_to_add, int):
        raise TypeError("Days must be an integer")
    
    date_ = parse_date(date)
    month_ = date_["month"]
    day_ = date_["day"]
    year_ = date_["year"]

    days_remaining_in_month = last_date_of_month[str(month_)] - day_
    key = True

    while key:
        if days_to_add > days_remaining_in_month:
            days_to_add = days_to_add - (last_date_of_month[str(month_)] - day_)
            month_ = month_ + 1
            day_ = 0
            if month_ > 12:
                month_ = 1
                year_ = year_ + 1
        else:
            day_ = day_ + days_to_add
            key = False
    
    new_date = date_combiner(month_, day_, year_)
    return new_date

def date_combiner(month, day, year):
    if month < 10:
        month = f"0{month}"
    if day < 10:
        day = f"0{day}"

    combined_date = f"{month}/{day}/{year}" 
    return combined_date

#come back to this
def add_time(date, time, duration):
    #time must be in 24 hours format
    
    date_ = parse_date(date)
    month_ = date_["month"]
    day_ = date_["day"]
    year_ = date_["year"]

    time_ = parse_time(time)
    hour_ = time_["hour"]
    minute_ = time_["minute"]

    key = True
    while key:
        if duration > (24 - time):
            duration = duration - (24 - 11)
            day_ = day_ + 1
            time = 0
            if day_ > last_date_of_month[str(month_)]:
                day_ = last_date_of_month[str(month_)]
                combined_date = date_combiner(month_, day_, year_)
                new_date = parse_date(add_day(combined_date, 1))
                month_ = new_date["month"]
                day_ = new_date["day"]
                year_ = new_date["year"]
        else:
            time = duration
    
    print(f"{month_}/{day_}/{year_} at {time}")

def parse_time(time):
    #time is in 09:00am or pm format
    time_pattern = r"\d+"
    time_regex = re.compile(time_pattern)

    time_list = re.findall(time_regex, time)
    #returns first index of hours and second index of minutes
    hour = time_list[0]
    minute = time_list[1]

    return {"hour": int(hour), "minute": int(minute)}

def convert_duration_to_minutes(duration):
    #duration is in hours. What to do if it is in minutes?
    whole_duration = math.floor(duration)
    minutes_in_decimals = duration - whole_duration

    minutes = math.floor(minutes_in_decimals * 60)
    return {"hour": whole_duration, "minute": minutes}

def convert_time_to_twentyfour(time):
    parsed_time = parse_time(time)
    hour_ = parsed_time["hour"]
    minute_ = parsed_time["minute"]

    ampm = r"(am|pm)"
    ampm_regex = re.compile(ampm)
    ampm_list = re.findall(ampm_regex, time)
    
    if ampm_list[0] == 'pm' and not hour_ == 12:
        hour_ = hour_ + 12
    elif ampm_list[0] == 'am' and hour_ == 12:
        hour_ = 0
    elif ampm_list[0] == 'pm' and hour_ == 12:
        hour_ = 12
    
    if len(str(minute_)) < 2:
        minute_ = f"0{minute_}"
    if len(str(hour_)) < 2:
        hour_ = f"0{hour_}"

    return f"{hour_}:{minute_}"



























