dinner_guests = ['Bob','Joe','John']

print(dinner_guests[0], "join us for dinner.")
print(dinner_guests[1], "join us for dinner.")
print(dinner_guests[2], "join us for dinner")

not_coming = 'John'
dinner_guests.remove(not_coming)
print(f'{not_coming}, will not be joining us.')
print(dinner_guests)#this is how i applied remove. To use pop in the same way I'd need pop(-1)

dinner_guests.append('Isabelle')
print(f'Dear {dinner_guests[2]}, join us for dinner.')
print(dinner_guests)

print(f"{dinner_guests[1]}, {dinner_guests[0]}, {dinner_guests[2]}, we just found a bigger table, let's go.")

dinner_guests.insert(0, 'Michael')
dinner_guests.insert(0,'Kayden')
dinner_guests.append('Skylir')
print(dinner_guests)

print(f" {dinner_guests[0]}, {dinner_guests[1]}, {dinner_guests[-1]}, join our table!")

print("Sorry guys, can only invite two of y'all.")
dinner_guests.pop(0)
dinner_guests.pop(0)
dinner_guests.pop(0)
dinner_guests.pop(0)
print(dinner_guests)
print(f"{dinner_guests[0]}, {dinner_guests[1]}, you can stil join")
print("Or actually nah, f y'all.")
del dinner_guests[0]
del dinner_guests[0]
print(dinner_guests)

#This one is just applying all the knowledge I got from chap 3.