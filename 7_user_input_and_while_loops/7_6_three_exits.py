'''
Write different versions of either Exercise 7-4 or 7-5 that do each of the following at least once:
- Use a conditional test in the while statement to stop the loop.
- Use an active variable to control how long the loop runs.
- Use a break statement to exit the loop when the user enters a 'quit' value.'''

people = int(input("How many tickets would you like to buy? "))

active = people
order = 1
price = 0
broken = False

while active > 0:
    
    ui = input(f"What is the number {order} person's age? ").lower()
    
    if ui == 'quit':
        broken = True
        break
    else:
        age = int(ui)
    
    if age > 75:
        print("Person over 75 years old cannot buy the ticket. Please try again.")
        broken = True
        break 
    
    if age < 3:
        price += 0
    elif age >= 3 and age <= 12:
        price += 10
    else:
        price += 15
    
    active -= 1
    order += 1

if broken:
    print(f"Please run the program again.")
else:    
    print(f"Your tickets' price is ${price}.")