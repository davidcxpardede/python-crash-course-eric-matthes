class Employee():
    def __init__(self, first_name, last_name, annual_salary):
        """Initialize the class attributes."""
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = annual_salary
        
    def give_raise(self, raises=5000):
        """Raise the annual salary of employee."""
        self.annual_salary += raises