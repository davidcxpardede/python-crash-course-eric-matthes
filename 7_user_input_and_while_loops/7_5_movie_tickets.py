'''
A movie theater charges different ticket prices depending on a person's age. If a person is under the age of 3, the ticket is free; if they're between 3 and 12, the ticket is $10; and if they are over 12, the ticket is $15. Write a loop in which you ask users their age, and then tell them the cost of their movie tickets.
'''

people = int(input("How many tickets would you like to buy? "))

loop = people
order = 1
price = 0

while loop > 0:
    age = int(input(f"What is the number {order} person's age? "))
    
    if age < 3:
        price += 0
    elif age >= 3 and age <= 12:
        price += 10
    else:
        price += 15
    
    loop -= 1
    order += 1
    
print(f"Your tickets' price is ${price}.")