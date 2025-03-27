from itertools import groupby
from random import choice, randint
from pprint import pprint

def classify_person(person):
    ''' ages: 0-18, 19-30, 31-50, 51-70, 70+ '''
    if person[1] <= 18:
        return '0-18'
    elif person[1] <= 30:
        return '19-30'
    elif person[1] <= 50:
        return '31-50'
    elif person[1] <= 70:
        return '51-70'
    else:
        return '70+'

names = 'Johannes, John, Michael, Robin, Claus, Marina, Alice, Siri, Sara, Kolin, Kolyan, Max, Muhammad'.split(', ')

people = []

people_count = int(input('People count: '))

for i in range(people_count):
    people.append( (choice(names), randint(0, 90)) )

people.sort(key=lambda x: x[1])

if (people_count <= 20):
    for person in people:
        print(f'{person[0]} {person[1]} y.o.')
else:
    print(f'Generated {people_count} people!')

classified_people = {}

for key, group in groupby(people, classify_person):
    classified_people[key] = list(group)

print(classified_people)





