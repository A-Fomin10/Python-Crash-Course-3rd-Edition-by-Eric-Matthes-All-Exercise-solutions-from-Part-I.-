#6-1 Intro to what a dictionary is.

friend = {'first_name': 'Deamor', 'last_name': 'Bleg', 
          'city':'sky_island', 'age':'20', }

#6-2 Favourite numbers

fav_numbers = {'igor': 13, 'deamor': 0, 'stas': 5, 'yarik': 7,'diana':7,}
print(fav_numbers)

#6-3 Glossary
#range, String, sort, tuple, inequality_operator

glossary = {'range': 'calls for a range of numbers', 
            'string':'any letter or word here',
            'sort': 'sorts item in the list in an alphabetical order',
            'tuple':'list that cannot be modified, only redefined', 
            'inequality_operator':'matches if the values are Not equall'}

definition_0 = glossary['range']
definition_1 = glossary['string']
definition_2 = glossary['sort']
definition_3 = glossary['tuple']
definition_4 = glossary['inequality_operator']

print('\nrange:', definition_0)
print('\nstring:', definition_1)
print('\nsort:', definition_2)
print('\ntuple:', definition_3)
print('\ninequality-operator:', definition_4)
#this one took me a while, I wanted to make the output automated, but not
#sure how atp.