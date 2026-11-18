#7-1 Rental car

# message = input("Hi! What kind of car would you like to own? ")
# print(f"{message} is a nice car!")

#7-2 Restaurant Seating

# message = input("Good evening! how many people are in your group?")
# message = int(message)
# if message > 8: 
#     print(f"Please esxcuse us, would you mind  waiting for a table?")
# else:
#     print(f"Your table is ready! Follow me, please!")

#I think with a while loop I could try to write a second version of this
#program, where if user enters a string of letters and not int, it can repeat
#until he does.

#7-3 Multiples of ten

number = input("Enter a number, and I'll tell you if it's a multiple of ten:")
number = int(number)

if number % 10 == 0:
    print(f"\nThis number is a multiple of ten.")
else:
    print(f"\nThis number is not a multiple of ten.")
