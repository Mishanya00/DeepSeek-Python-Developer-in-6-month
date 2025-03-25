import time
from datetime import date
from datetime import datetime
from datetime import timedelta
import re


def is_valid_date_format(date_string):
    # Date format: dd.mm.yyyy
    pattern = r"^\d{2}\.\d{2}\.\d{4}$"
    return bool(re.match(pattern, date_string))


def is_valid_date(date_string):
    if not is_valid_date_format(date_string):
        return False
    try:
        pass
        # datetime.strptime
    except ValueError:
        pass
    return False


today = date.today()
start_year = date(today.year-30, 1, 1)

print("New Year:", start_year)
print("Today:", today)

print(today - start_year)
# tmdt = timedelta(start_year.)
# print(tmdt)
