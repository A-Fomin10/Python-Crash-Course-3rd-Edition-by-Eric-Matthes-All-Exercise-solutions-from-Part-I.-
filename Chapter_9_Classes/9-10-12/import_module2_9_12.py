#9-12 Admin and priviliges stoed here
from import_module1_9_12 import user 

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