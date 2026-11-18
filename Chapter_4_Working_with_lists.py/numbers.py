# for inclusive in range (1, 21):
#     print(inclusive)
#Commented previous one out, because it gave a big output(completed)
#When in comes to ranges - It starts with the number I wrote but ends 1 before
#(I wrote 21, and it ends with 20)

# for long in range(1, 1000001):
#     print(long)
#Comented out because it's also long(completed) My pc was happy about this one.

# million = list(range(1, 1000001))#It defines a list only if I write 'list'
# #also isn't it technicly a tuple? Google says no
# print(min(million))
# print(max(million))
# print(sum(million))
# #done

# odd_numbers = list(range(1, 22, 2))#number "3" means that pyhon will skip every third number(I will change 3 to 2)
# print(odd_numbers)

# multipliesof3 = list(range(3, 32, 3))#This is one way to write multiples of three but ex tells us to use a for loop..
# print(multipliesof3)

threes = []#Defined a list 
for value in range(1,11):
    three = value **3
    threes.append(three)# What I can also do is delete 'Theree' from lines 24,26,27, and write value **3 in .append()
print(threes)
#**2 raises the value to the second power 
# *2 or other number is a multiplier


# threes2 = [value *3 for value in range(1,11)]
# print(threes2)  #two ways to do this in a for loop

# cubes = []
# for value in range(1,11):
#     cube = value **3
#     cubes.append(cube)
# print(cubes) #it took me around few hours to find the mistake. 
# I puted "value" in the gaps instead of "cube" and the code didn't work(Line 33)

# cubes2 = [value **3 for value in range(1,11)]
# print(cubes2) #last exercise in this section of the chapter - done.
# print(len(cubes2))#Printed len just to test myself
