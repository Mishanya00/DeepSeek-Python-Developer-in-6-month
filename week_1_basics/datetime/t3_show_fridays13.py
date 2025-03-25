from datetime import datetime

DAY_NUMBER = 13

year = int(input('Year: '))

if year < 1 or year > 9999:
    print('Incorrect year!')
else:
    for month in range(1,13):
        temp = datetime(year, month, DAY_NUMBER)
        if temp.weekday() == 4:
            print('Friday 13! ' + temp.strftime("%d-%m-%Y"))
