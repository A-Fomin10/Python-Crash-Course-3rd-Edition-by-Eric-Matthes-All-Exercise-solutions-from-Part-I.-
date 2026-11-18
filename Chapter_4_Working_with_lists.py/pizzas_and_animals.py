favourite_pizza = ['kaprichosa', 'pepperoni','4cheeses','tomatoe','proshutto']
# for pizza in favourite_pizza:
#     print(f"I like {pizza.title()} pizza")
# # A simple for loop, that runs through a list of pizzas and an indented print 
# # statement which prints it out

# print("I really love pizza!\n")
# print(f"The first three pizzas in the list are: {favourite_pizza[:3]}")
# print(f"Three pizzas in the middle of the list are: {favourite_pizza[1:-1]}")
# print(f"Last three pizzas in the list are: {favourite_pizza[-3:]}")

friend_pizzas = favourite_pizza[:]#Idk why I added [:] here because it runs through the entire list anyway.
# favourite_pizza = friend_pizzas
#Interesting, so if I put line 13 above 12, it will give an error, because it dosen't know what is friend_pizzas
#But since I kinda = them both, the're gonna be similar


favourite_pizza.append('americana')
friend_pizzas.append('margarita')
print(f"\nMy favourite pizzas are:",favourite_pizza)
print(f"\nMy friend's favourite pizzas are:",friend_pizzas)

# for pizza in favourite_pizza:
#     print(f"My favourite pizzas are {pizza.title()}!")
# for pizza in friend_pizzas:
#     print(f"My friend's favourite pizzas are {pizza.title()}!")
#lines 20 - 26 basicly do the same thing, but second one is  in a loop I guess, I could modify this loop by adding an if
# statement and make only the first sentance full, and the next ones will go "and also 'pizza'"

# animals_for_milk = ['cow', 'goat', 'sheep']
# for animal in animals_for_milk:
#     print(f"A {animal.title()} gives you milk.")
# print("Any of these animals give you milk.")

#I've commended out every previous task to do task 4-12

# my_foods = ['pizza','falafel','burger','chips']
# for food in my_foods[:]:#Again, there is really no point in [:] here it returns the same output atp.
#     print("My favourite food is", food.title())

# for food2 in my_foods[: :2]:#I told python to skip falafel and chips because burger and pizza are my most  favourite.
#     print("My most favourite food is:", food2.title())
