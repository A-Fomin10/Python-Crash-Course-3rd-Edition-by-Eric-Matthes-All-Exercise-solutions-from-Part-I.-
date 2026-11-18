#9-13 Dice

from random import randint

class Dice:
    """A class that reprecents a d_any dice"""

    def __init__(self, sides=0):#so if I add anything here, and then 
        """function that initializes a dice with a fixed amount of sides"""
        self.sides = 10#and then fix a number here, this one will be the max
        #kinda forgot about that 

    def roll_dice(self):
        """function that rolls dice"""
        print(f"{randint(1,self.sides)}")

# d_any = Dice()
# d_any.roll_dice()

#9-14 Lottery 

from random import choice

letters_numbers = ['a','b','c','d','e','1','2','3','4','5','6','7','8','9','10']
first = choice(letters_numbers)
second = choice(letters_numbers)
third = choice(letters_numbers)
fourth = choice(letters_numbers)
lottery_winner = (first,second,third,fourth)
print(f"Any ticket matching these four symbols: {lottery_winner}, wins a free pizza!")

#9-15 Lottery analysis

#I couln't make it on my own so I read about it on reddit forums and will 
#try to implemet a few changes to the code from the ideas given on the python 

from random import choice

def get_winning_ticket(possibilities):
    """Return a winning ticket from a set of possibilities."""
    winning_ticket = []

    # We don't want to repeat winning numbers or letters, so we'll use a
    #   while loop.
    while len(winning_ticket) < 4:
        pulled_item = choice(possibilities)

        # Only add the pulled item to the winning ticket if it hasn't
        #   already been pulled.
        if pulled_item not in winning_ticket:
            winning_ticket.append(pulled_item)

    return winning_ticket

"""This is variant that one of the other programmers suggests to update"""
#Authors ver
# def check_ticket(played_ticket, winning_ticket):
#     # Check all elements in the played ticket. If any are not in the 
#     #   winning ticket, return False.
#     for element in played_ticket:
#         if element not in winning_ticket:
#             return False

#     # We must have a winning ticket!
#     return True

#programmers ver
def check_ticket(played_ticket: list, winning_ticket: list):
      # Are all the numbers (or letters) of the played ticket 
      # also in winning_ticket? Return True if that is so.
      return all(x in winning_ticket for x in played_ticket)

def make_random_ticket(possibilities):
    """Return a random ticket from a set of possibilities."""
    ticket = []
    # We don't want to repeat numbers or letters, so we'll use a while loop.
    while len(ticket) < 4:
        pulled_item = choice(possibilities)

        # Only add the pulled item to the ticket if it hasn't already
        #   been pulled.
        if pulled_item not in ticket:
            ticket.append(pulled_item)

    return ticket


possibilities = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'a', 'b', 'c', 'd', 'e']
winning_ticket = get_winning_ticket(possibilities)

plays = 0
won = False

# Let's set a max number of tries, in case this takes forever!
max_tries = 1_000_000

while not won:
    new_ticket = make_random_ticket(possibilities)
    print("Winning Ticket: ", winning_ticket)
    print("New Ticket: ", new_ticket)

    won = check_ticket(new_ticket, winning_ticket)
    plays += 1
    if plays >= max_tries:
        break

if won:
    print("We have a winning ticket!")
    print(f"Your ticket: {new_ticket}")
    print(f"Winning ticket: {winning_ticket}")
    print(f"It only took {plays} tries to win!")
else:
    print(f"Tried {plays} times, without pulling a winner. :(")
    print(f"Your ticket: {new_ticket}")
    print(f"Winning ticket: {winning_ticket}")

#Conc: I've posted a few python discuss posts on the thread i found about this exercise,
# to figure out, how it works.

#9-16 is about Python module of the week website which I am going to explore.