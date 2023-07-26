class Restaurant:
    
    def __init__(self, restaurant_name, cuisine_type):
        """Initialize name and cuisine type attributes."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
        
    def describe_restaurant(self):
        """Display the name and cuisine type of the restaurant."""
        print(f"Welcome to {self.restaurant_name} restaurant!")
        print(f"We serve {self.cuisine_type}.")
    
    def open_restaurant(self):
        """Indicate that the restaurant is open."""
        print("We are open!")
    
    def set_number_served(self, serve_update):
        """Set the number of customers that have been served."""
        self.number_served = serve_update
    
    def increment_number_served(self, serve_increment):
        """Increment the number of customers that have been served."""
        self.number_served += serve_increment

restaurant = Restaurant('Pardede', 'Bataknese food')
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)

restaurant.describe_restaurant()
restaurant.open_restaurant()

print(f"\nYesterday, the restaurant has served {restaurant.number_served} people.")

restaurant.number_served = 10
print(f"Today, we serve {restaurant.number_served} people.")

restaurant.set_number_served(20)
print(f"\nThe next day, we served {restaurant.number_served} people.")

restaurant.increment_number_served(25)
print(f"\nAt the end of the week, we have served a total of {restaurant.number_served} people.")