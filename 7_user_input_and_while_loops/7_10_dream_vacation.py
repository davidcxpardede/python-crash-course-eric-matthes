'''
Write a program that polls users about their dream vacation. Write a prompt similar to If you could visit one place in the world, where would you go? Include a block of code that prints the results of the poll.
'''

pollers = int(input("How many pollers are there? "))

loop_active = pollers
dream_vacation = {}

while loop_active > 0:
    
    name = input("What is your name? ")
    vacation = input("If you could visit one place in the world, where would you go? ")
    
    dream_vacation[name] = vacation
    loop_active -= 1

for name, vacation in dream_vacation.items():
    print(f"{name.title()} would love to go to {vacation.title()}.")