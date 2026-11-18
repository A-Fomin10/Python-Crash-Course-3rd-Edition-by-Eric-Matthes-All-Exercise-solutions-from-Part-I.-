dreams = ['cyapd','animated movies','ai and drones on the battlefield']
# print(dreams[0])
# print(dreams[2])
# First, here is a list of dreams, and then I called to pring for last and first items.

# message = f"My first idea of an AI product was {dreams[0].upper()}."
# print(message)


dreams[0] = 'rich'#THIS one replcaed CYAPD with rich. So if del just deletes it, this thing replaces it
print(dreams)


dreams.append('someone who loves me')#so append in the command to add an item at the End of the list, 
print(dreams)#meaning that before line 14 dreams[-1] would be ai and drones, now it became someone who.

dreams.insert(0,'private jet')#This one got inserted meaning, it didn't replace anything
print(dreams)

del dreams[2]#It completely deletes second item in the list, but as the count starts and 0, it deletes the third one(A.M.)
print(dreams)#I just read the book, it says that if I use del, I can't access the value from the list.

popped_dreams = dreams.pop()
print(f'The dream I really want to achieve here and now is {popped_dreams.upper()}.!')
print(dreams)#.pop removes the last item in the list, but I can still use it.
#pop can also be used to remove an item in any position in the list by simply adding parentheses
# dreams.pop(0)
# print(dreams) #however it won't work for values like 'private jet', only numbers. That's why u use 'remove'
too_far = 'private jet' 
dreams.remove('private jet')
# del dreams[0]
print(dreams)
print(f"\nA {too_far.lower()} is not на часі right now.")
#the point of .remove() is removing the item by its name instead of position in the list.
#Also .remove() still allows you to work with the item you removed from the list.

#The book tells me that i can use pop to get the last item from the list, but why can't I just:
# motorcycles1 = ['honda', 'suzuki','yamaha']
# print(f'The last motorcycle I owned is a {motorcycles1[-1]}')#because whatever adds to the list is still -1.
# motorcycles1.append('whatever')
# print(f'The last motorcycle I owned is a {motorcycles1[-1]}')



# print(sorted(dreams))
# print(dreams)
# print(sorted(dreams, reverse=True))
# print(dreams)
# dreams.sort()
# print(dreams)
# dreams.reverse()
# print(dreams)
# dreams.reverse()
# print(dreams)
# print(len(dreams))
#Okay so sorted dreams give us the list sorted, sort() sorts in and the we 
#have to pring it, the sorted + reverse=True gives us noting new, and it can 
#also be used as sort() but reverse() and the pring seperately, and len is 
# for the amount of numbers in the list.