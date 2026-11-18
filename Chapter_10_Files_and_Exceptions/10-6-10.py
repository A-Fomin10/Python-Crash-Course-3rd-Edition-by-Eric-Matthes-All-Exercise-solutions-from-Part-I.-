from pathlib import Path

#----------------------------------------------------------------------------#
# Note: In order for this entire file to work, you need to put both .txt and |
# .py files into the same directory where your .vscode directory is.         |
#----------------------------------------------------------------------------#

#10-6 Addition

# print("\nGive me two numbers, I'll add them up.")
# print("Enter 'q' to quit")


# fn = input("\nFirst number:")

# sn = input("\nSecond number:")

# try:
#     answer = int(fn) + int(sn)
# except ValueError:
#     print("Please enter numbers, not text.")
# else:
#     print(answer)

#10-7 Addition calculator

# while True:
#     fn = input("\nFirst number:")
#     if fn == 'q':
#         break
#     sn = input("\nSecond number:")
#     if sn == 'q':
#         break

#     try:
#         answer = int(fn) + int(sn)
#     except ValueError:
#         print("Please enter numbers, not text.")
#     else:
#         print(answer)

#10-8 Cats and Dogs

# filenames = ['cats.txt','dogs.txt']

# for f in filenames:
#     path = Path(f)
#     try:
#         contents = path.read_text()
#     except FileNotFoundError:
#         print(f"Sorry {path}, does not exist.")
#     else:
#         print(contents)

#10-9 Silent cats and Dogs 


# filenames = ['cats.txt','dogs.txt']

# for f in filenames:
#     path = Path(f)
#     try:
#         contents = path.read_text()
#     except FileNotFoundError:
#         pass
#     else:
#         print(contents)

#10-10 Common words 

filenames = ["How it works.txt","The boy mechanic.txt",
             "The Standard Electrical Dictionary.txt"]

for f in filenames:
    path = Path(f)
    try:
        contents = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        print(f"Sorry {path}, does not exist.")
    else:
        num = contents.count('the ')
        print(f"'{path}' has approximately {num} 'the' words.")


