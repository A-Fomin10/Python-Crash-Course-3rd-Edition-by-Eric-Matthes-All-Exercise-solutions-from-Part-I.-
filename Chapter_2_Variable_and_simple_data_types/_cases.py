person = "eRic"
print(f"Hello {person.title()}, would you like to learn some Python today?")
print(f"{person.upper()}")
print(f"{person.lower()}")
print(f"{person.title()}")

print('Volodymyr Zelenskiy had said not long ago, "The future of the world is being decided right now, on the battlefield in Ukraine"')

first_name = "volodymyr"
last_name = "zelenskiy"
famous_person = f"{first_name} {last_name}"
print(f'{famous_person.title()} had said not long ago, "The fututre of the world is being decided right now, on the battlefield in Ukraine"')

person2 = "\n\tStanislave\tlave"
#\n goes for row down, \t goes for white space. Also if I put \n or \t inside
# of a print("\n\tmessage")like this - \t\n won't appear in the output.
print(person2)
print(f"{person2.strip()}") 
print(f"{person2.lstrip()}")
print(f"{person2.rstrip().lstrip()}")
#I've also added some white space in between person2 and I'm not sure how to get rid of it with simple strips.

# filename = "python_notes.txt"
# print(filename)
# print(f"{filename.removesuffix('.txt')}")
#And you can see the 'removesuffix' it's for the end of the value, while removesuffix is for the begining.

#In these programs I've been experimenting with python. The date of this comment is 11.08.2025
#This is a message from 18.04.2026 where I am looking at my old code and adding notes.
                                                            