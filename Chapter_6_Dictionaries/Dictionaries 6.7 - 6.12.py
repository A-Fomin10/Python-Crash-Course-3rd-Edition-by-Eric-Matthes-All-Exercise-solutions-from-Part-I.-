# #6-7 People


# friend_0 = {'first': 'Deamor', 'last': 'Bleg', 
#           'location':'sky_island', 'age':'unknown', }

# friend_1 = {'first': 'stanislav',
#             'last': 'honcharenko',
#             'location': 'zbarazh',
#             'age': '21'}

# friend_2 = {'first': 'volodymyr',
#             'last': 'studiynkiy',
#             'location': 'zbarazh',
#             'age': '25'}

# people = [friend_0, friend_1, friend_2]

# for person in people:
#     print(f'\n',person)

# #6-8 Pets

# pet_0 = {'animal': 'dog',
#          'owner': 'stanislav'}

# pet_1 = {'animal': 'cat',
#          'owner': 'volodymyr'}

# pet_2 = {'animal': 'parrot',
#          'owner': 'yaroslav'}

# pet_3 = {'animal': 'cat',
#          'owner': 'deamor'}

# pets = [pet_0, pet_1, pet_2, pet_3]

# for pet in pets:
#     print(f'\n',pet)

#6-9 Places

# favourite_places = {'deamor': ['bedroom','kitchen'],
#                     'stavislav':['living room',],
#                     'volodymyr':['forest','zolochivskiy castle', 
#                                  'pidhoretskyi castle'],
#                     }


# for name, places in favourite_places.items():
#     if len(places) == 1:
#         print(f"\n{name.title()}'s favourite place is:")
#         for place in places:
#             print(f"{place.title()}")
#     else:
#         print(f"\n{name.title()}'s favourite places are:")
#         for place in places:
#             print(f"{place.title()}")

# #6-10 Favorite Numbers 


# fav_numbers = {'igor': [13,7], 
#                 'deamor': [0,100,99], 
#                 'stas': [5,6], 
#                 'yarik': [7,4],}


# for name, numbers in fav_numbers.items():
#     print(f"\n{name.title()}'s favourite numbers are:")
#     for number in numbers:
#         print(f"{number}")

#6-11 Cities

# cities = {
#         'vermillion': {
#                     'country': 'the united states', 
#                     'population':'low', 
#                     'fact':'this is the city where I will study.'
#                     },
          
#         'zbarazh': {
#                     'country': 'ukraine', 
#                     'population':'low', 
#                     'fact':'this city is older than the united states',
#                     },
          
#         'warsaw': {
#                     'country': 'poland', 
#                     'population':'high', 
#                     'fact':'this is the city where I got my visa'
#                     },
#           }

# for city_name, city_info in cities.items():
#     print(f"\nCity name: {city_name.title()}")
#     location = city_info['country']
#     population = city_info['population']
#     fact = city_info['fact']
#     print(f"It is located in {location.title()}.")
#     print(f"Its population is {population.title()}." )
#     print(f"And also {fact.title()}." )

#6-12 Extensions

#In this task I must choose any program from the charapter

favorite_languages = {
                        'jen':['python','rust'],
                        'sarah':['c'],
                        'adriana': ['swift'],
                        'edward': ['rust','go'],
                        'phil': ['python','haskell']
                        }
#I will modyfy this program from the page 109 by adding if, and the I will
#also add how many languages were mentioned.

for name, languages in favorite_languages.items():
    if len(languages) == 1:
        print(f"\n{name.title()}'s favourite language is:")
        for language in languages:
            print(f"{language.title()}")
    else:
        print(f"\n{name.title()}'s favourite languages are:")
        for language in languages:
            print(f"{language.title()}")


# print(f'\f The following languages were mentioned:')
# for language in (favorite_languages.values()):
#     if ['python'] in favorite_languages.items()[:1]:
#         print(f"{'python'} was mentioned once")
#     else:
#         print(f"{'python'} more than once")

#I tried to do the 'mentioned' thing, but it's so late and I still got much
# to do. I guess, I'll stop here and start the new chapter tomorrow.
#Besdies I did indeed figure out how to use len and if statements as the book
#suggested, so I did bare minimum to compplete the exercise.
# and I couln't figure out how to do this second part, because my current
#fav languages thing has a list as a value, and python doesn't consider list
#for a value