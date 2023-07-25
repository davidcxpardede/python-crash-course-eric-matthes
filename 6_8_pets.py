'''
Make several dictionaries, where each dictionary represents a different pet. In each dictionary, include the kind of animal and the owner's name. Store these dictionaries in a list called pets. Next, loop through your list and as you do, print everything you know about each pet.
'''

tengu = {'name': 'Tengu',
       'kind': 'dog',
       'color': 'white',
       'hobby': 'chasing people',}

hero = {'name': 'Hero',
       'kind': 'cat',
       'color': 'brown',
       'hobby': 'sleeping',}

hermes = {'name': 'Hermes',
       'kind': 'Suzuki GSX R-150',
       'color': 'black',
       'hobby': 'speeding in a highway',}

pets = [tengu, hero, hermes]

for pet in pets:
    print(f"{pet['name']} is a {pet['color']} {pet['kind']} who loves {pet['hobby']}.")