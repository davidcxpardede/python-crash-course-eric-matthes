'''
Write a function that accepts a list of items a person wants on a sandwich. The function should have one parameter that collects as many items as the function call provides, and it should print a summary of the sandwich that's being ordered. Call the function three times, using a different number of arguments each time.
'''

def sandwiches(*fillings):
    """Display the filling in the sandwich a person orders."""
    print("\nYou ordered a sandwich with the following fillings: ")
    for filling in fillings:
        print(filling)

sandwiches('tomatoes', 'meat', 'cheese')
sandwiches('cucumber', 'porks')
sandwiches('chicken', 'eggs', 'mayonnaise', 'sausage', 'fillet', 'beef', 'fish')