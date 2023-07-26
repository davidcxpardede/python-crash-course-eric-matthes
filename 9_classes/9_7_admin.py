class User:
    def __init__(self, first_name, last_name, nim, faculty, major):
        """Initialize the User class attributes."""
        self.first_name = first_name
        self.last_name = last_name
        self.nim = nim
        self.faculty = faculty
        self.major = major
    
    def describe_user(self):
        """Display information about the user."""
        print(f"\n\nName: {self.first_name.title()} {self.last_name.title()}")
        print(f"NIM: {self.nim}")
        print(f"Faculty: {self.faculty.upper()}")
        print(f"Major: {self.major.title()}")
    
    def greet_user(self):
        """Display greeting message to the user."""
        print(f"\nWelcome, {self.first_name.title()} {self.last_name.title()} ({self.nim})!")

class Admin(User):
    def __init__(self, first_name, last_name, nim, faculty, major, privileges):
        """Initialize the Admin subclass attributes."""
        super().__init__(first_name, last_name, nim, faculty, major)
        self.privileges = privileges
    
    def show_privileges(self):
        """Display the privileges of an Admin."""
        print(f"{self.first_name.title()} is an admin, therefore he can: ")
        for privilege in self.privileges:
            print(privilege.title())

admin_1 = Admin('david', 'pardede', 13618012, 'ftmd', 'aerospace engineering', ['can add post', 'can delete post', 'can edit post', 'can add and remove users'])
admin_1.show_privileges()
        
            