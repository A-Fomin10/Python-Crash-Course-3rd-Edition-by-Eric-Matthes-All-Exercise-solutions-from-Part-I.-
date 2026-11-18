#8-12 Sandwiches 

def make_sandwiches(*ingredients):
    """Fuction which tells us what ingreadients user wants in their sandwich"""
    for ingredient in ingredients:
        print(f"The user wants {ingredient.title()} in their sandwich.")

# make_sandwiches("salami")

# make_sandwiches("salami","mozarella cheese")

# make_sandwiches("tomatoes","onions","pesto sauce")

#To make a more clear output, it would be better to put another print call 
# above the for loop, and then print each ingredient as a seperate word after
# the for loop.
# 
#Also the '*' before the ingredients word in line 3 creates us a tuple.

#8-13 User Profile

def build_profile(first, last, **user_info):
    """Builds a profile of a user"""
    user_info["first_name"] = first
    user_info["last_name"] = last
    return user_info

user_profile = build_profile("Anton","Fomin",
                            location = "Vermillion",
                            field = "CompSci") 
                                # - Idk if the book covered this earlier, but
                                # apperantly, when you pass an argument to a 
                                #function, you first pass the ones, which the
                                #fuction already has, and only afterwards
                                #create new ones. Not sure how this workds.

# print(user_profile)

#8-14 Cars

def build_cars(manufacturer, model, **car_info):
    """Builds a car"""
    car_info["manufacturer_name"] = manufacturer
    car_info["model_name"] = model
    return car_info

car_profile = build_cars("Mercedez","SUV", color="blue", tow_package=True)

print(car_profile)