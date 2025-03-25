import sys
from datetime import datetime
from datetime import date


def is_valid_date(date_string):
    try:
        res = datetime.date((datetime.strptime(date_string, "%d.%m.%Y")))
        return res
    except ValueError:
        pass
    return False


if len(sys.argv) < 3:
    print("Usage: py -3 t1_difference_in_days.py <date_1> <date_2>")
    sys.exit(1)

first_date = is_valid_date(sys.argv[1])
second_date = is_valid_date(sys.argv[2])

if not first_date:
    print("First date is incorrect (format: dd.mm.yyyy)")
if not first_date:
    print("Second date is incorrect (format: dd.mm.yyyy)")

print("Operation:", first_date, "-", second_date)
print("Difference between two dates:", (first_date - second_date).days, "days!")
