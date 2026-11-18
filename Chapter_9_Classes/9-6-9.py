#9-6 Ice cream stand

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

# green_mexican = IceCreamStand("The Green Mexican", "Mexican")
# green_mexican.describe_restaurant()
# green_mexican.describe_flavors()

#9-7 Admmin


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
    
#9-8 Priviliges 

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

# user_admin = admin("admin","admin","admin","admin")
# user_admin.admin_priviliges.dispay_priviliges()

#9-9 Battery upgrade

class car:

    def __init__(self,make,model,year):
        """function that launches car attributes"""
        self.make = make
        self.model = model
        self.year = year

    def describe_car(self):
        """function that describes a car"""
        print(f"This car is made by {self.make}, it's model is{self.model} and it was make in {self.year}")

class ElectricCar(car):
    """Child class for an electric car"""

    def __init__(self, make, model, year):
        """Function that initialized car attributes"""
        super().__init__(make, model, year)
        self.battery = Battery()

class Battery:
    "Battery for an electric car"

    def __init__(self, battery_size=40):
        """Function that initializes battery attributes"""
        self.battery_size = battery_size

    def describe_battery(self):
        """function that dispays battery size"""
        print(f"\nThis car has a {self.battery_size}-kWh battery")

    def get_range(self):
        """Test battery range"""
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 225

        print(f"This car can go about {range} miles on a full charge")

    def upgrade_battery(self):
        """checks the size of the battery and modifys it"""
        if self.battery_size <= 65 or self.battery_size >= 65:
            self.battery_size = 65
           



my_leaf = ElectricCar('nissan', 'leaf','2024')
my_leaf.describe_car()

my_leaf.battery.describe_battery()
my_leaf.battery.get_range()

my_leaf.battery.upgrade_battery()

my_leaf.battery.describe_battery()
my_leaf.battery.get_range()
        
