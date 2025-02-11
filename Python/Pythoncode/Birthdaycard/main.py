import datetime, bday_messages

today = datetime.date.today()

 # get you birthday from the user
birth_month = int(input("Enter your birth month (1-12): "))
birth_day = int(input("Enter your birth day (1-31): "))

current_year = today.year

try:
    this_year_bday = datetime.date(current_year, birth_month, birth_day)
except ValueError:
    this_year_bday = datetime.date(current_year, birth_month, birth_day - 1)

if today > this_year_bday:
    next_birthday = datetime.date(current_year + 1, birth_month, birth_day)
else:
    next_birthday = this_year_bday

days_away = (next_birthday - today).days

if today == next_birthday:
    print(bday_messages.random_message)
else:
    print(f"Your birthday is {days_away} days away.")