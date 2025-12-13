# Date and time operations

from datetime import datetime, date, time, timedelta

# Current date and time
now = datetime.now()
print("Current datetime:", now)
print("Current date:", date.today())
print("Current time:", now.time())

# Creating specific dates and times
specific_date = datetime(2024, 12, 25, 10, 30, 0)
print("Specific datetime:", specific_date)

# Formatting dates
formatted = now.strftime("%Y-%m-%d %H:%M:%S")
print("Formatted:", formatted)

# Common format codes
print("Year:", now.strftime("%Y"))           # 2025
print("Month:", now.strftime("%B"))          # December
print("Day:", now.strftime("%A"))            # Friday
print("Date:", now.strftime("%d/%m/%Y"))     # 13/12/2025
print("Time:", now.strftime("%H:%M:%S"))     # 14:30:45
print("AM/PM:", now.strftime("%I:%M %p"))    # 02:30 PM

# Parsing dates from strings
date_string = "2024-12-25"
parsed_date = datetime.strptime(date_string, "%Y-%m-%d")
print("Parsed date:", parsed_date)

# Date arithmetic with timedelta
today = date.today()
tomorrow = today + timedelta(days=1)
yesterday = today - timedelta(days=1)
next_week = today + timedelta(weeks=1)
next_month = today + timedelta(days=30)

print(f"Today: {today}")
print(f"Tomorrow: {tomorrow}")
print(f"Yesterday: {yesterday}")
print(f"Next week: {next_week}")

# Time difference
date1 = datetime(2024, 1, 1)
date2 = datetime(2024, 12, 31)
difference = date2 - date1
print(f"Days between dates: {difference.days}")
print(f"Total seconds: {difference.total_seconds()}")

# Comparing dates
if datetime.now() > datetime(2024, 1, 1):
    print("We are past 2024")

# Getting date components
today = datetime.now()
print(f"Year: {today.year}")
print(f"Month: {today.month}")
print(f"Day: {today.day}")
print(f"Hour: {today.hour}")
print(f"Minute: {today.minute}")
print(f"Second: {today.second}")
print(f"Weekday: {today.weekday()}")  # Monday is 0

# Calculate age
def calculate_age(birth_date):
    today = date.today()
    age = today.year - birth_date.year
    # Adjust if birthday hasn't occurred this year
    if (today.month, today.day) < (birth_date.month, birth_date.day):
        age -= 1
    return age

birthdate = date(1990, 5, 15)
print(f"Age: {calculate_age(birthdate)} years")

# Working days calculation (excluding weekends)
def count_working_days(start_date, end_date):
    days = 0
    current = start_date
    while current <= end_date:
        if current.weekday() < 5:  # Monday to Friday
            days += 1
        current += timedelta(days=1)
    return days

start = date(2024, 12, 1)
end = date(2024, 12, 31)
print(f"Working days in December: {count_working_days(start, end)}")

# Time zones (basic awareness)
from datetime import timezone

utc_now = datetime.now(timezone.utc)
print(f"UTC time: {utc_now}")

# ISO format
iso_format = now.isoformat()
print(f"ISO format: {iso_format}")

# Timestamp (seconds since epoch)
timestamp = now.timestamp()
print(f"Timestamp: {timestamp}")

# Convert timestamp back to datetime
from_timestamp = datetime.fromtimestamp(timestamp)
print(f"From timestamp: {from_timestamp}")
