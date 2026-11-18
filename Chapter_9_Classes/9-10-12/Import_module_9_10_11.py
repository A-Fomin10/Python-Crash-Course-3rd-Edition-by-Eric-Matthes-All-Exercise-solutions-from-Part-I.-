#9-10 Imported Restaurant

class restaurant:
    """restaurant and it's functions"""

    def __init__(self, restaurant_name, cuisine_type):
        """initialize name and attributes"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """description of a restaurant"""
        print(f"\nThis restaurant is called {self.restaurant_name}.")
        print(f"It is specialized in {self.cuisine_type} cuisine.")

    def open_restaurant(self):
        "simulate a restaurtant being open"
        print(f"\nThe {self.restaurant_name} is now open!")

class IceCreamStand(restaurant):
    """Child class of the restaurant class"""

    def __init__(self, restaurant_name, cuisine_type,):
        """Functions that initializes the attributes for this class"""
        super().__init__(restaurant_name, cuisine_type,)
        self.flavors = ['mango','pineapple','gum']

    def describe_flavors(self):
        """Function which displays flavors when called on""" 
        print(f"\nThe ice cream machine has {self.flavors} avalible!")

#9-11 Imported admin

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

class admin(user):
    """Type of a user with more priviliges"""

    def __init__(self, first_name, last_name, age, race):
        """Initializing all parent class attributes"""
        super().__init__(first_name, last_name, age, race)
        self.admin_priviliges = alluser_priviliges()

class alluser_priviliges:
    """class for priviliges"""

    def __init__ (self, admin_priviliges =  ["can add users","can ban users",
                                             "can post"]):
        """initializing class attributes"""
        self.admin_priviliges = admin_priviliges # the thing that concerns me is
        #that rn list is a paramter, and in the ex it's required to be an attribute
        #however for some reason it just dosen't work as an attribute.
        # so that's why I putted it into a parameter.

    def dispay_priviliges(self):
        """Function that displays all admin priviliges"""
        print("Admin has these priviliges:")
        for privilige in self.admin_priviliges:
            print(privilige)