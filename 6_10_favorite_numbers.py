'''
Modify your program from Exercise 6-2 so each person can have more than one favorite number. Then print each person's name along with their favorite numbers.
'''

favorite_numbers = {'Thalia': [2, 16],
                    'Ryandika': [1, 2],
                    'Giovani': [6, 9],
                    'Marcellino': [23, 120],
                    'Jonathan': [101, 14],}

for name, numbers in favorite_numbers.items():
    print(f"\n{name}'s favorite numbers are: ")
    for number in numbers:
        print(f"\t{number}")