#9-12 User class stored here

class user:
    """class representing a user"""

    def __init__(self, first_name, last_name, age, race):
        """create user attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.race = race

    def describe_user(self):
        """print all user attributes"""
        full_name = f"{self.first_name} {self.last_name}"
        print(f"\nThe user's name is {full_name}")
        print(f"The user is {self.age} years old.")
        print(f"The user's race is {self.race}")

    def greet_user(self):
        """generating a greet message to the user"""
        full_name = f"{self.first_name} {self.last_name}"
        print(f"Hello {full_name}! Welcome to our place.")
