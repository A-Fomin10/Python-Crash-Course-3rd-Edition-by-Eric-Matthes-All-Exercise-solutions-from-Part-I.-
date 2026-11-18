from pathlib import Path
import json

#10-11 Favorite number

#This exercise is moved to 10-11_A and 10-11_B.

#------------------------------------------------------------------------------#
# Note that this program will create the .json file in the Coding directory    # 
# if you move that file in this program's directory, it will create a new one. #
#------------------------------------------------------------------------------#

#10-12 Favorite number Remembered

# fav = int(input("What is your favourite number?"))


# path = Path('fav.json')
# contents = json.dumps(fav)
# path.write_text(contents)

# contents = path.read_text()
# fav_num = json.loads(contents)

# print(f"I know that your favourite number is {fav_num}!")

#------------------------------------------------------------------------------#
# Note that this program will create the .json file in the Coding directory    # 
# if you move that file in this program's directory, it will create a new one. #
#------------------------------------------------------------------------------#

#10-13 User Dictionary
# favs = {'number': '', 'color': '', 'food': ''}

# favs['number'] = int(input("What is your favourite number?"))
# favs['color'] = input("What is your favorite color?")
# favs['food'] = input("What is your favorite fast food?")

# path = Path('favorites.json')

# contents = json.dumps(favs)
# path.write_text(contents)

# contents = path.read_text()
# favourite_items = json.loads(contents)

# print(favourite_items)

#10-14 Verify User

"""
This is authrors code for 'remember_me.py' found on his GutHub
This exercise wants me to modify the program.
"""

from pathlib import Path
import json


def get_stored_username(path):
    """Get stored username if available."""
    if path.exists():
        contents = path.read_text()
        username = json.loads(contents)
        return username
    else:
        return None

def get_new_username(path):
    """Prompt for a new username."""
    username = input("What is your name? ")
    contents = json.dumps(username)
    path.write_text(contents)
    return username

def greet_user():
    """Greet the user by name."""
    path = Path('username.json')
    username = get_stored_username(path)
    if username:
        cor_name = input(f"Is this your username? '{username}' y/n?")
        if cor_name == 'y':
            print(f"Welcome back, {username}!")
        else:
            username = get_new_username(path)
            print(f"We'll remember you when you come back, {username}!")
    else:
        username = get_new_username(path)
        print(f"We'll remember you when you come back, {username}!")

greet_user()