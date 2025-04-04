from datetime import datetime, timedelta

def read_date():
    date_str = input("Enter a date (YYYY-MM-DD): ")
    date_obj = datetime.strptime(date_str, "%Y-%m-%d").date()
    return date_obj

dates = []
for _ in range(4):
    date = read_date()
    while date in dates:
        print("Date already entered. Please enter a unique date.")
        date = read_date()
    dates.append(date)

formatted_dates = [date.strftime("%m/%d/%Y") for date in dates]
print("List of dates:")
print("\n".join(formatted_dates))

sorted_dates = sorted(dates)
formatted_sorted_dates = [date.strftime("%m/%d/%Y") for date in sorted_dates]
print("Sorted dates:")
print("\n".join(formatted_sorted_dates))

formatted_dates = [date.strftime("%m/%d/%y") for date in sorted_dates]
print("Formatted sorted dates:")
print("\n".join(formatted_dates))

days_between = abs((sorted_dates[-1] - sorted_dates[-2]).days)
print("Number of days between the last two dates:", days_between)

most_recent_date = sorted_dates[-1]
date_in_3_weeks = most_recent_date + timedelta(weeks=3)
print("Date 3 weeks from the most recent date:", date_in_3_weeks.strftime("%B %d, %Y"))

earliest_date = sorted_dates[0]
day_of_week = earliest_date.strftime("%A")
print("Day of the week of the earliest date:", day_of_week)