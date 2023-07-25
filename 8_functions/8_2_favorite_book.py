'''
Write a function called favorite_book() that accepts one parameter, title. The function should print a message. Call the function, making sure to include a book title as an argument in the function call.
'''

def favorite_book(title):
    """Displaying the favorite book based on the argument."""
    print(f"One of my favorite books is {title.title()}.")

favorite_book("project hail mary")