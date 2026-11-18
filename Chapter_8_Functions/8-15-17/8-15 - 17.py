#8-15 Printing models
# import printing_functions

# unprinted_designs = ['phone_case', 'robot pendant', 'dedecahedron']
# completed_models = []

# printing_functions.print_models(unprinted_designs, completed_models)
# printing_functions.show_completed_models(completed_models)

#8-16
#1
# import printing_functions

# user_profile = printing_functions.build_profile("Anton","Fomin",
#                             location = "Zbarazh",
#                             field = "CompSci") 

# print(user_profile)

2
from printing_functions import build_cars

car_profile = build_cars(model='sUv',manufacturer='mercedez',color='blue',
                        tow_package=True)

print(car_profile)

#3
# from printing_functions import build_profile as bp

# user_profile = bp('Stas','menthapipireta',
#                   location='ohtyrka',
#                   field='medicine')

# print(user_profile)

#4

# import printing_functions as pf

# car_profile = pf.build_cars('foltswagen','sedan', color='black',towpackage=False)
# print(car_profile)

#5 
# from printing_functions import *

# car_profile = build_cars('foltswagen','sedan', color='black',towpackage=False)
# print(car_profile)


# user_profile = build_profile('Stas','menthapipireta',
#                   location='ohtyrka',
#                   field='medicine')
# print(f"\n{user_profile}")


#8-17
#I will not write it in this specific file, because this esercise is about
#eiditng programs i wrote earlier.