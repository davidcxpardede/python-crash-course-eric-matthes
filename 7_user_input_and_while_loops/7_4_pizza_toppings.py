'''
Write a loop that prompts the user to enter a series of pizze toppings until they enter a 'quit' value. As they enter each topping, print a message saying you will add that topping to their pizza.
'''

prompt = "Please enter the topping you would like in your pizza.\nEnter 'quit' when you are finished. "

while True:
    toppings = input(prompt).lower()
    
    if toppings == 'quit':
        break
    
    print(f"{toppings.title()} will be added to your pizza.")
    
    