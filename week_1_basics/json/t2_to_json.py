import json
from random import randint, choice

names = 'James, Lora, Michael, Verden, Molly, Tristan de Mortar, Golumn'.split(', ')

def generate_person():
    name = choice(names)
    email = name + '@qmail.net'
    age = randint(1,99)
    person = {
        'name': name,
        'email': email,
        'age': age
    }
    return person

filename = input('Filename: ')
filename += '.json'

with open(filename, 'w', encoding='utf-8') as f:
    json.dump(generate_person(), f, indent=4)

print(filename, 'file is generated!')
