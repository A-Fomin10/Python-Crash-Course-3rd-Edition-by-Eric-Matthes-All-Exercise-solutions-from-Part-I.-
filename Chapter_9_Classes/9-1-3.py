#9-1 Restaurant 

# class restaurant:
#     """restaurant and it's functions"""

#     def __init__(self, restaurant_name, cuisine_type):
#         """initialize name and attributes"""
#         self.restaurant_name = restaurant_name
#         self.cuisine_type = cuisine_type

#     def describe_restaurant(self):
#         """description of a restaurant"""
#         print(f"\nThis restaurant is called {self.restaurant_name}.")
#         print(f"It is specialized in {self.cuisine_type} cuisine.")

#     def open_restaurant(self):
#         "simulate a restaurtant being open"
#         print(f"\nThe {self.restaurant_name} is now open!")

# green_mexican = restaurant("The Green Mexican", "Mexican")
# green_mexican.describe_restaurant()
# green_mexican.open_restaurant()

#9-2Three Restaurants 

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

# uno = restaurant("UNO","Multinational")
# puzata_hata = restaurant("Puzata Hata", "Ukrainian")
# georgian_bakery = restaurant("Georgian bakery","Georgian")

# georgian_bakery.describe_restaurant()
# puzata_hata.describe_restaurant()
# uno.describe_restaurant()

#9-3 Users

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

user_1 = user("Anton","Fomin","21","White")
user_1.describe_user()
user_1.greet_user()

user_2 = user("Stanislav","Honcharenko","21","White")
user_2.describe_user()
user_2.greet_user()

user_3 = user("Barack","Obama","Unknown","African-American")
user_3.describe_user()
user_3.greet_user()