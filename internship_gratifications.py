# import os
import sys
from datetime import datetime
from datetime import date
from datetime import timedelta

if not len(sys.argv) >= 6:
    print("Command format is incorrect.")
    print("Example command : py internship_gratifications.py 13/07/2021 20/10/2021 5 7 3.9")
    exit()

try:
    date_begin_str = sys.argv[1]
    # date_begin_str = "28/09/2020"
    date_begin = datetime.strptime(date_begin_str, '%d/%m/%Y')
except Exception as e:
    print("Date format is incorrect, use DD/MM/YYYY")
    exit()

try:
    date_end_str = sys.argv[2]
    # date_end_str = "15/01/2021"
    date_end = datetime.strptime(date_end_str, '%d/%m/%Y')
except Exception as e:
    print("Date format is incorrect, use DD/MM/YYYY")
    exit()

if date_begin > date_end:
    print("End date must be after begin date")
    exit()

try:
    # days_per_week = 35
    days_per_week = int(sys.argv[3])
    if days_per_week < 0:
        raise Exception("NotPositive")
except Exception as e:
    print("Days per week should be a positive integer")
    exit()

try:
    # hours_per_day = 7
    hours_per_day = int(sys.argv[4])
    if hours_per_day < 0:
        raise Exception("NotPositive")
except Exception as e:
    print("Hours per day should be a positive integer")
    exit()

try:
    gratification = float(sys.argv[5])
    if gratification < 0:
        raise Exception("NotPositive")
except Exception as e:
    print("Gratification should be a positive float")
    exit()


not_working_days = ["saturday", "sunday"]
if days_per_week < 5:
    try:
        days_str = sys.argv[6].split(",")
        for day in days_str:
            if day.startswith("-"):
                not_working_days.append(day[1:])
            elif day.startswith("+") and day[1:].lower() in not_working_days:
                del not_working_days[day[1:]]
    except Exception as e:
        print("Days per week < 5 but not working days not specified or wrong format. Add \"+Saturday,-Monday\" at end line for example if you work on Saturdays and not on Mondays ")

# gratification = 3.9

all_days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]

working_days_name = []
for day in all_days:
    if not day in not_working_days:
        working_days_name.append(day)

working_days = 0
hours = 0

for i in range((date_end - date_begin).days + 1):
    day = date(date_begin.year, date_begin.month, date_begin.day) + timedelta(days=i)
    day_name = day.strftime("%A")
    # print(day_name)
    if not day_name.lower() in not_working_days :
        hours += hours_per_day
        working_days += 1
        # print(hours)

working_hours_count = working_days*hours_per_day
gratification_count = working_days*hours_per_day*gratification

days_off = 0 if working_hours_count <=44*7 else working_hours_count/(22*7)*2.5


print(f"\n==== FROM {date_begin_str} TO {date_end_str}")
print(f"==== {hours_per_day} hours a day | {gratification}€ per hour")
print(f"==== Working days  : {','.join(working_days_name)}\n")
print(f"> Working days count            : {working_days}")
print(f"> Working hours count           : {working_hours_count}")
print(f"> Estimated gratification total : {gratification_count:.1f}")
print(f"> Estimated days off count      : {days_off:.1f}")
print("\nDisclaimer: Gratification and days off counts are estimations, and might differs depending on your employer")