'''
Start with the program you wrote for Exercise 6-1. Make two new dictionaries representing different people, and store all three dictionaries in a list called people. Loop through your list of people. As you loop through the list, print everything you know about each person.
'''

dika = {'first_name': 'Immanuel',
          'last_name':'Ompusunggu',
          'age': 20,
          'city': 'Batam'}

ojo = {'first_name': 'Jonathan',
          'last_name':'Saragi',
          'age': 20,
          'city': 'Medan'}

gio = {'first_name': 'Giovani',
          'last_name':'Simangunsong',
          'age': 20,
          'city': 'Pematang Siantar'}

friends = [dika, ojo, gio]

for friend in friends:
    print(f"{friend['first_name']} {friend['last_name']} is {friend['age']} years old. He is from {friend['city']}.")