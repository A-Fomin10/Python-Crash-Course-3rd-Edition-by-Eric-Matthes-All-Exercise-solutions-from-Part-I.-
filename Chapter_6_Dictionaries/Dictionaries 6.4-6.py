# 6.4 Glossary 2


# glossary = {'range': 'calls for a range of numbers.', 
#             'string':'any letter or word here.',
#             'sort': 'sorts item in the list in an alphabetical order.',
#             'tuple':'list that cannot be modified, only redefined.', 
#             'inequality_operator':'matches if the values are Not equall.', 
#             'items() method': 'means keys and values in the dictionary.',
#             'set': 'is basicly a dictionary, but without key-value pairs.',
#             'key': 'is the name of a data snip in the dictionary.',
#             'value': 'something that data snip means.',
#             'loop': 'a way to search for items in lits and dictionaries.'}

# for key, value in glossary.items():
#     print(f'\nKey:{key}'.title())
#     print(f'Value:{value}')

#6-5 Rivers

# rivers = {'egypt': 'nyle',
#           'ukraine': 'dnipro',
#           'united states': 'missuori'}

# for k,v in rivers.items():
#     print(f'{v.title()} is a river, that runs through {k.title()}.')

# for v in rivers.values():
#     print(v.title())

# for k in rivers: #I could also use key() after rivers but it calls for key on default. 
#     print(f'{k.title()}')

#Polling 6-6

favouritve_languages = {
                        "jen": 'python',
                        "sarah": 'c',
                        "edward": 'rust',
                        "phill": 'python', "test": 'test'
                        }

people = ['jen','adriana','sarah','stas','yarik','edward','sviatoslav','phill','test']

for name in favouritve_languages.keys():
    if name in people:
        print(f'Hi {name.title()}, thank you for taking a poll!')

for name in people:
    if name not in favouritve_languages.keys():
        print(f'\tHi {name.title()}, you should take our poll!')

#So this code looks sloppy and I can't get why, so I added 'test' to both dic,
#and list, to see how its gonna go. Seems to me that it works just the way
#I think it does.
