class Restaurant:
    
    def __init__(self, restaurant_name, cuisine_type):
        """Initialize name and cuisine type attributes."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        
    def describe_restaurant(self):
        """Display the name and cuisine type of the restaurant."""
        print(f"Welcome to {self.restaurant_name} restaurant!")
        print(f"We serve {self.cuisine_type}.")
    
    def open_restaurant(self):
        """Indicate that the restaurant is open."""
        print("We are open!")