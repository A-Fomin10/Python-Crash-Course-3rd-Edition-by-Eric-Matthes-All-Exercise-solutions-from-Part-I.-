# car = 'subaru'
# print('Is car == "subaru"? I predict True.')
# print(car == 'subaru')

# print("\nIs car == 'audi'? I predict False ")
# print( car =='audi')



# #1
car = 'Audi'
# print(car == 'audi')

car = 'bmw'
# print(car.upper() == 'BMW')

# #2

age_0 = 18 
age_1 = 20
age_3 = 21
age_2 = 22

# print(age_0 >= 21 and age_2 >= 21) #according to the book if one of 'and' tests
# # #fails, the overall test returns False

# print((age_2 <= 21) or (age_3 <= 21))#this or test returns True because 
# # #One test passes

# #3
# For this T/F test I'll use inequality operator != so if values won't match it
# # would return True, (But as a text) and if they will, it'll return False

# answer = 17
# if answer != 17:
#     print("Incorrect")
# else:
#     print("Correct")

# answer = 42
# if answer != 17:
#     print("Incorrect")
# else:
#     print("Correct")

# #4 
#Now let's try to search something in the list
# pizza_toppings = ['pepperoni','pineapple','onions']
# print('mushrooms' in pizza_toppings)

# if 'pepperoni' in pizza_toppings:
    # print(True)
# print('pepperoni' in pizza_toppings) 
# in num4 we checked if Value EXISTS in the list

# #5 
# # Now let's check if a value DOSEN'T exist in a list
# banned_users = ['samara','aireen', 'suzu','bella']
# user = 'Sofie'
# if user not in banned_users:
#     print(f'{user.title()}, you are good to go.')
# #I know that keyword NOT returned True for us, because user is not in the list.

# #6
# #Tests for strings
# string_0 = 'Test'
# print(string_0 == 'test')

# string_0 = 'test'
# print(string_0.title() == 'Test')#In this line I call on title method, so that
# #original string is written with title and compated to Test. But if I change to
# #upper, it will faul the test.

#7
#Lets do another string test but this time with lower instead of title
# emotions = 'ANGER'
# print(emotions.lower() == 'anger')

# #Don't forget that == is EQUALITY operator, so if value of ANGER(with lower
# #method) is the same as value of anger (and it is, it returns true.)
#Meaning that if I change == to != the output will be false, because it matched.

# car = 'BMW'
# print(car.lower() == 'BMW')#Now this one return false because we called a lower
# #method upon car string but equaled it with an upper case string 

#8
#for this we'll use ages from a previous test

# age_0 = 25
# age_1 = 20
# age_2 = 22
# age_3 = 21
# age_4 = 23
# age_5 = 19

# print((age_0 >= 21) or (age_1 <= 21))
# print((age_1 <= 21) and (age_5 <= 21))
# print((age_2 <= 21) and (age_3 <= 21) and (age_5 <= 21))
# print((age_1 <= 21) and (age_5 >= 21) or (age_4 <= 21))
# # #In this section I learned more on how to do numerical tests, I feel like
# # # it's been pretty helpful.

# #9
cars = ['subaru', 'bmw', 'honda', 'cintroen','toyota','Chevrolet']
# for car in cars:
#     if car == 'bmw':
#         print(car.upper())
#     else:
#      print(car.title()) #This section is not for the task. 

# car_of_choice = 'ferrari'
# if car_of_choice not in cars:
#     print('True')
# car_of_choice_0 = 'chevrolet'
# if car_of_choice_0.title() not in cars:
#     print('True')
# else:
#     print('False')

#10 
print('chevrolet'.title() in cars)
print('BMW'.lower() in cars)#I played around with BMW and methods to 
#memorise the logic

#11
print(age_0 >= 15)
print(age_0 <= 15)
print(age_1 != 21)
print(age_2 == 21)

