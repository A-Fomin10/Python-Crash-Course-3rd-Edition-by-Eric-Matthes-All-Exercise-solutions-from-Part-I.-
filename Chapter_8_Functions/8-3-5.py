#All the programs here are edited as stated in 'Styling functions' sections of 
# chapter 8. (It needed me only to do 3 programs of choice)

#8-3 T-shirt

def t_shirt(size, text):
    """T-shirt description"""
    print(f"\nThe text on this T-shirt says: {text}")
    print(f"The size of this T-shirt is: {size}")


t_shirt('M', 'Lost in transmission') #positional argument
t_shirt(text='Do it for the culture', size='XS') #keyword argument

#8-4 Large shirts

def make_shirts(size='Large', text='I love python' ):
    """Shirt description"""
    print(f"\nThere is a '{text}' text on this shirt.")
    print(f"Its size is {size}.")

make_shirts() 

#The task is to make a large shirt, and a medium shirt as a default, and then
# a different size, so I'm gonna duplicate this code a few times.


def make_shirts(size='Medium', text='I love python' ):
    """Shirt description"""
    print(f"\nThere is a '{text}' text on this shirt.")
    print(f"Its size is {size}.")

make_shirts()

make_shirts(size='Extra Small') #this function call overwrote the default 
#value

#8-5 Cities 

def city_description(name, country='Ukraine'):
    """City description"""
    print(f"\nThe name of this city is {name};")
    print(f"It's located in {country}.")

city_description('Kyiv')
city_description('Odessa')
city_description('Vermillion', 'The United States') #Positional argument

#actully, all three of these are positional arguments. I remember from reading
#the book, that python treats everything as a positional argument by default.
#and because of this values without default paramenters must go first.