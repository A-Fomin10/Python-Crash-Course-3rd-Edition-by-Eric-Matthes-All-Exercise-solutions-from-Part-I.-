#8-15 Printing Functions 
#This is a file from which I will import the functions.

def print_models(unprinted_designs, completed_models):
    """Simulate printing each desgn, until none are left.
    Move each design to colmpleted_models after printing."""

    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)

def show_completed_models(completed_models):
    """Show all the models that were printed"""
    print(f"\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

#8-16 Imports


def build_profile(first, last, **user_info):
    """Builds a profile of a user"""
    user_info["first_name"] = first
    user_info["last_name"] = last
    return user_info

def build_cars(manufacturer, model, **car_info):
    """Builds a car"""
    car_info["manufacturer_name"] = manufacturer
    car_info["model_name"] = model
    return car_info