from random import randint

combination = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 'A', 'B', 'C', 'D', 'E']

lottery = []
length = 4
choices = combination[:]

while length > 0:
    index = randint(0, len(choices)-1)
    lottery.append(choices.pop(index))
    length -= 1

print(lottery)