#7-4 Pizza Toppings

# prompt = "\nTell us what kind of toppings would you like to order?"
# prompt += "\n(When you are done - enter 'quit')"

# while True: 
#     order = input(prompt)

#     if order == 'quit':
#         break
#     else:
#         print(f"\n\tThank you for your order we'll add {order.title()}, to your pizza")  

#So ideally, I think, the best way to do this would be to make an empty list
#of pizza toppings, and call it smh like customer order, and every time he
# wrties something - we add it to the list

#7-5 Moive tickets 

# prompt = "\nHow old are you?"


# while True: 
#     age = input(prompt)
#     age = int(age)

#     if age <= 3: 
#         print(f"\nYour ticket is free")
#     elif age >= 3 and age <= 12:#if there would be 'or' this wouldn't work
#         print(f"\nYour ticket would be 10$.")
#     elif age >= 12:
#         print(f"\nYour ticket will be 15$.")

#     break

#7-6 Three exists

#toppings exit 1 conditional


prompt = "\nTell us what kind of toppings would you like to order?"
prompt += "\n(You may add only 3 toppings)"

current_number = 1
while current_number <= 3: 
    order = input(prompt)
    current_number +=1
    print(f"\n\tThank you for your order we'll add {order.title()}, to your pizza")  

#toppings exit 2 flag

# prompt = "\nTell us what kind of toppings would you like to order?"
# prompt += "\n(Enter 'quit' when you are ready to order.)"

# active = True

# while active: 
#     order = input(prompt)

#     if order == 'quit':
#         active = False
#     else:
#         print(f"\n\tThank you for your order we'll add {order.title()}, to your pizza")  

#toppings exit 3  break


# prompt = "\nTell us what kind of toppings would you like to order?"
# prompt += "\n(Enter 'quit' when you are ready to order.)"


# while True: 
#     order = input(prompt)

#     if order == 'quit':
#         break
#     else:
#         print(f"\n\tThank you for your order we'll add {order.title()}, to your pizza")  

#7-7 Infinity 


prompt = "\nHow old are you?"


while True: 
    age = input(prompt)
    age = int(age)

    if age <= 3:  
        print(f"\nYour ticket is free")
    elif age >= 3 and age <= 12:#if there would be 'or' this wouldn't work
        print(f"\nYour ticket would be 10$.")
    elif age >= 12:
        print(f"\nYour ticket will be 15$.")

#funny, cuz to make this one infinite, just have to remove a break statement.

#While reading through the last section of chap 7, I recalled about duplicate
#values in a dictionary, and how could you print them without these duplicants
#I return a chapter back and read again about how to work with sets
#so you can wrap a dictionary into a set and use .values() and it will print
#those values without any duplicants.







