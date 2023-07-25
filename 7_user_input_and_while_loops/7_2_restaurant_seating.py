'''
Write a program that asks the user how many people are in their dinner group. If the answer is more than eight, print a message saying they will have to wait for a table. Otherwise, report that their table is ready.
'''

print("WELCOME TO PARDEDE RESTAURANT!")

number = int(input("How many of you are having dinner? "))

if number > 8:
    print(f"Thank you for coming!\nUnfortunately, we do not have seats for {number} people available right now. Please wait and we will notify you when it is ready.")
else:
    print(f"Thank you for coming! We will get a table for {number} people right away!")