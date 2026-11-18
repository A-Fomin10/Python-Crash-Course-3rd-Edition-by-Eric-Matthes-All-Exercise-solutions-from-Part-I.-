#Hello Admin Ex. 5-8

# users = ['deamor bleg','xgb','rataskor','statsun','dophamin adikt','admin']
# for user in users:
#     if user == 'admin':
#         print(f"Hello {user.title()}! Would you like to see staatus report?")
#     elif user == 'xgb':
#         print(f"Hello {user.upper()}, thank you for joining!")
#     else:
#         print(f"Hello {user.title()}, thank you for joining!")

#No users Ex. 5-9

# users = []

# #Don't forget that when nmae of the list is put into an if test, it cheks, if
# # the list is empty.

# if users: 
#     for user in users:
#         if user == 'admin':
#             print(f"Hello {user.title()}! Would you like to see staatus report?")
#         elif user == 'xgb':
#             print(f"Hello {user.upper()}, thank you for joining!")
#         else:
#             print(f"Hello {user.title()}, thank you for joining!")
# else:
#     print("We need to find more users!")

#Checking Usernames Ex.5-10

# current_users = ['Deamor Bleg','xgb','rataskor','statsun','dophamin adikt',
#                  'admin','MASKOTIK']#I added all cases to the list for test

# new_users = ['DEAMOR BLEG','Dophamin Adikt','pavlo','maskotik','zorelit',
#              'miriam krips']

# for new_user in new_users:
#     if new_user.lower() in current_users:
#         print(f"\nSorry {new_user.title()}, you have to think of a different name")
#     elif new_user.upper() in current_users:
#         print(f"\nSorry {new_user.title()}, you have to think of a different name")
#     elif new_user.title() in current_users:
#         print(f"\nSorry {new_user.title()}, you have to think of a different name")
#     else:
#         print(f"\nHello {new_user.title()}! Thank you for registering!")

#Took me  a while but I made it case sensitive too, maybe there is a better way 
# for it idk

#Ordinal number Ex.5-11

# numbers = ['1','2','3','4','5','6','7','8','9']

# for number in numbers:
#     if number == '1':
#         print(f"{number}st")
#     elif number == '2':
#         print(f'{number}nd')
#     elif number == '3':
#         print(f'{number}rd')
#     else:
#         print(f'{number}th')


#test code from one of my python discuss posts

# cars = ['subaru', 'bmw', 'honda', 'cintroen','toyota','chevrolet ']

# car_of_choice_0 = 'chevrolet'

# result = 'False'

# for i in cars:

#     if car_of_choice_0 in i:

#         result = 'True'
#         break

# print(result)