print("Give me two numbers and I will add them!")
print("Type q to quit.")

while True:
    number_1 = input("Enter your first number. ")
    if number_1.lower() == 'q':
        break
    
    number_2 = input("Enter your second number. ")
    if number_2.lower() == 'q':
        break
    
    try:
        print(f"{int(number_1)} + {int(number_2)} equals {int(number_1) + int(number_2)}")
    
    except ValueError:
        print("You have to enter a number!")
    