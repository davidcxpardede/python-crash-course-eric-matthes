'''
Using the list sandwich_orders from Exercise 7_8, make sure the sandwich 'pastrami' appears in the list at least three times. Add code near the beginning of your program to pring a message saying the deli has run out of pastrami, and then use a while loop to remove all occurences of 'pastrami' from sandwich_orders. Make sure no pastrami sandwiches end up in finished_sandwiches.
'''

sandwich_orders = ['tuna', 'pastrami',  'chicken', 'beef', 'pork', 'vegan', 'pastrami', 'egg', 'duck', 'pastrami',  'mackarel', 'snake', 'salmon']
sandwich_orders.sort(reverse=True)

print("\nWe're sorry to inform you that we have run out of pastrami and we would have to cancel all pastrami sandwich orders.\n")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

finished_sandwiches = []

while sandwich_orders:
    current_order = sandwich_orders.pop()
    print(f"I made your {current_order.title()} Sandwich.")
    finished_sandwiches.append(current_order)

print("\nAll the sandwiches has been made:")
for sandwich in finished_sandwiches:
    print(f"\t{sandwich.title()} Sandwich")