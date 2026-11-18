#7-8 Deli

# sandwich_orders = ["ceasar","ham&cheese","daily special","chicken - pesto"]
# finished_sandwiches = []

# while sandwich_orders:
#     sandwich_prep = sandwich_orders.pop()

#     print(f"Preparing a {sandwich_prep.title()} order!")
#     finished_sandwiches.append(sandwich_prep)

# print(f"\n---ORDERS-READY---")
# for finished_sandwich in finished_sandwiches:
#     print(f"{finished_sandwich.title()} is ready!")

#7-9 No pastrami


# sandwich_orders = ["pastrami","ceasar","ham&cheese","pastrami","daily special",
#                    "chicken - pesto","pastrami"]
# finished_sandwiches = []

# print(f"\nDeli is currently out of pastrami!")

# while 'pastrami' in sandwich_orders:
#     sandwich_orders.remove('pastrami')

# while sandwich_orders:    
#     sandwich_prep = sandwich_orders.pop()

#     print(f"Preparing a {sandwich_prep.title()} order!")
#     finished_sandwiches.append(sandwich_prep)

# print(f"\n---ORDERS-READY---")
# for finished_sandwich in finished_sandwiches:
#     print(f"{finished_sandwich.title()} is ready!")

#7-10 Dream Vacation

responses = {}

polling_active = True


while polling_active:

    name = input("\nWhat is your name?")
    response = input("\nWhere would you like to travel?")

    responses[name] = response

    repeat = input("Would you like to give anyone else a try?(yes/no)")
    if repeat == 'no':
        polling_active = False
    
print(f"\n---POLL RESULTS---")
for name, response in responses.items():
    print(f"{name} wants to go to {response}.")

#This is kinda of just a coopied version of the last prog in the chapter. 
#and honsetly, I can't understand some things in it yet FE how line 50 works
#I do have a better idea of how to do it, but not gonna do it just yet atm
#got big things planned ahead.
#good luck future me. 