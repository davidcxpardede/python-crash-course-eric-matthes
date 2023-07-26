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

user_1 = User('david', 'pardede', 13618012, 'ftmd', 'aerospace engineering')
user_2 = User('timothy', 'simbolon', 13118086, 'ftmd', 'mechanical engineer')
user_3 = User('luiz', 'sinaga', 12112093, 'fttm', 'mining engineering')
user_4 = User('giovani', 'simangunsong', 13421068, 'fti', 'industrial engineering')
user_5 = User('hans', 'simanjorang', 10218004, 'fmipa', 'physics')

user_1.describe_user()
user_1.greet_user()

user_2.describe_user()
user_2.greet_user()

user_3.describe_user()
user_3.greet_user()

user_4.describe_user()
user_4.greet_user()

user_5.describe_user()
user_5.greet_user()
    