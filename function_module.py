# Example: functions for greeting and reading time

import datetime  # module from Python standard library

def greet_user(name):
    """
    Return a greeting string for given name.
    """
    return f"Hello, {name}!"

def days_until_birthday(birth_month, birth_day):
    """
    Calculate days until next birthday from today (month, day).
    """
    today = datetime.date.today()
    # build this year's birthday
    this_year_bday = datetime.date(today.year, birth_month, birth_day)
    if this_year_bday < today:
        # birthday already passed this year — use next year
        this_year_bday = datetime.date(today.year + 1, birth_month, birth_day)
    delta = this_year_bday - today
    return delta.days

# Using the functions
print(greet_user("Asha"))
print("Days until birthday:", days_until_birthday(10, 25))
