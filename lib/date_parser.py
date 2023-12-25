import re

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
    
    print(f"{month_}/{day_}/{year_}")

add_day("11/03/2000", 75)





