#9-4 Number Served

class restaurant:
    """restaurant and it's functions"""

    def __init__(self, restaurant_name, cuisine_type):
        """initialize name and attributes"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """description of a restaurant"""
        print(f"\nThis restaurant is called {self.restaurant_name}.")
        print(f"It is specialized in {self.cuisine_type} cuisine.")

    def open_restaurant(self):
        "simulate a restaurtant being open"
        print(f"\nThe {self.restaurant_name} is now open!")

    def read_served_customers(self):
        """A fucntion which simulates how many customers we've served"""
        print(f"Today we served already {self.number_served} customers!")

    def set_number_served(self,customers_served):
        """Sets a number of how many customers were served""" 
        self.number_served = customers_served

    def incriment_customer_number(self, cus_num):
        """Incrementing a number"""
        self.number_served += cus_num




green_mexican = restaurant("The Green Mexican", "Mexican")
# green_mexican.number_served = 5 #v1 # this one sets

# green_mexican.set_number_served(5) #v2 # this one aslo sets
# green_mexican.read_served_customers()

# green_mexican.incriment_customer_number(10) #this one adds
# green_mexican.read_served_customers()

#9-5 Login Attemnpts

class user:
    """class representing a user"""

    def __init__(self, first_name, last_name, age, race):
        """create user attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.race = race
        self.login_attempts = 0

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

    def print_login_attempts(self):
        """Method that prints the amount of login attemts"""
        print(f"\nThis user has attempted {self.login_attempts} logins.")

    def incriment_login_attempts(self,attempts):
        """Method that adds login attempts"""
        self.login_attempts += attempts 

    def reset_login_attempts(self,attempts):
        """Method that resents login attempts"""
        self.login_attempts = 0

    

user_1 = user("Anton","Fomin","21","White")
user_1.describe_user()
user_1.incriment_login_attempts(1)
user_1.incriment_login_attempts(1)
user_1.incriment_login_attempts(1)
user_1.print_login_attempts()
user_1.reset_login_attempts(0)
user_1.print_login_attempts()

#I think this task wanted me to reset login attempts in the function itself.
#but I', really now sure how to do it, but i does work when I cann the function.