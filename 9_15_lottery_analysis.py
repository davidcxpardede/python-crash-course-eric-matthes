from random import randint

combination = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 'A', 'B', 'C', 'D', 'E']

my_ticket = ['A', 'E', 1, 2]
number_of_spin = 0

while True:
    
    length = 4
    lottery = []
    choices = combination[:]
    
    while length > 0:
        index = randint(0, len(choices)-1)
        lottery.append(choices.pop(index))
        length -= 1
        number_of_spin += 1
    
    if lottery == my_ticket:
        print(number_of_spin)
        break