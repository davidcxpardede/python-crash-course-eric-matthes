class Restaurant:
    
    def __init__(self, restaurant_name, cuisine_type):
        """Initialize name and cuisine type attributes."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        
    def describe_restaurant(self):
        """Display the name and cuisine type of the restaurant."""
        print(f"\nWelcome to {self.restaurant_name} restaurant!")
        print(f"We serve {self.cuisine_type}.")
    
    def open_restaurant(self):
        """Indicate that the restaurant is open."""
        print("We are open!")

restaurant_1 = Restaurant('Pardede', 'Bataknese barbeque')
restaurant_2 = Restaurant('Sadikin', 'the best Indomie in the world')
restaurant_3 = Restaurant('Los Pollos Hermanos', 'fried chicken with methampethamyne')

restaurant_1.describe_restaurant()
restaurant_2.describe_restaurant()
restaurant_3.describe_restaurant()