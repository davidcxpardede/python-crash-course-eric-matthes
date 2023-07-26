class User:
    def __init__(self, first_name, last_name, nim, faculty, major):
        """Initialize the User class attributes."""
        self.first_name = first_name
        self.last_name = last_name
        self.nim = nim
        self.faculty = faculty
        self.major = major
        self.login_attempts = 0
    
    def describe_user(self):
        """Display information about the user."""
        print(f"\n\nName: {self.first_name.title()} {self.last_name.title()}")
        print(f"NIM: {self.nim}")
        print(f"Faculty: {self.faculty.upper()}")
        print(f"Major: {self.major.title()}")
    
    def greet_user(self):
        """Display greeting message to the user."""
        print(f"\nWelcome, {self.first_name.title()} {self.last_name.title()} ({self.nim})!")
    
    def increment_login_attempts(self):
        """Increment the number the user attempts to login."""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Rest the login attempt to 0."""
        self.login_attempts = 0
    
user_1 = User('david', 'pardede', 13618012, 'ftmd', 'aerospace engineering')

user_1.increment_login_attempts()
user_1.increment_login_attempts()
user_1.increment_login_attempts()
print(user_1.login_attempts)

user_1.reset_login_attempts()
print(user_1.login_attempts)
