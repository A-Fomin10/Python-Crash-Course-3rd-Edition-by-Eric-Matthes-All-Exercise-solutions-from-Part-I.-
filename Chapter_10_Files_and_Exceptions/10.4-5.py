from pathlib import Path

#----------------------------------------------------------------------------#
# Note: In order for this entire file to work, you need to put both .txt and |
# .py files into the same directory where your .vscode directory is.         |
#----------------------------------------------------------------------------#
#10-4 Guest 

# name = input("Enter your first name")

# path = Path("guest.txt")
# path.write_text(name)

#10-5 Guest Book

guest_book = []
flag = True
path = Path("guest_book.txt")

while flag == True:
    name = input("Enter your first name. Press 'n' to exit.")
    if name == 'n':
        flag = False
    else:
        guest_book.append(name)


content = ''

for guest in guest_book:
       content = content + guest + '\n' 

path.write_text(content)


    




    

    