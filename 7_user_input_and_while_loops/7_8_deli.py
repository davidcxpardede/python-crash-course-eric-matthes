'''
Make a list called sandwich_orders and fill it with the names of various sandwiches. Then make an empty list called finished_sandwiches. Loop through the list of sandwich orders and print a message for each order, such as I made your tuna sandwich. As each sandwich is maed, move it to the list of finished sandwiches. After all the sandwiches have been made, print a message listing each sandwich that was made.
'''

sandwich_orders = ['tuna', 'chicken', 'beef', 'pork', 'vegan', 'egg', 'duck', 'mackarel', 'snake', 'salmon']
sandwich_orders.sort(reverse=True)

finished_sandwiches = []

while sandwich_orders:
    current_order = sandwich_orders.pop()
    print(f"I made your {current_order.title()} Sandwich.")
    finished_sandwiches.append(current_order)

print("All the sandwiches has been made:")
for sandwich in finished_sandwiches:
    print(f"\t{sandwich.title()} Sandwich")