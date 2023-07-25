'''
Ask the user for a number, and then report whether the number is a multiple of 10 or not.
'''

number = int(input("Please enter a whole number. "))

if number%10 == 0:
    print(f"Your number is a multiple of 10.")
else:
    print(f"Your number is not a multiple of 10.")

