from pathlib import Path
#----------------------------------------------------------------------------#
# Note: In order for this entire file to work, you need to put both .txt and |
# .py files into the same directory where your .vscode directory is.         |
#----------------------------------------------------------------------------#
#10-1 Learning Python


print(f"\nFirst way be reading entire file\n")
path = Path("learning_python.txt")
contents = path.read_text()
print(contents)

print(f"\nSecond way with a for loop\n")
lines = contents.splitlines()
for line in lines:
    print(line)

#10-2 Learning C

print(f"\n Third way with a replace method\n")
print(contents.replace("Python", "C"))

print(f"\n Fourth way with a for loop and a replace method\n")
for line in lines:
    print(line.replace("Python", "C"))


#10-3 Simpler Code

print(f"\n Simpler Code 1\n")
path1 = Path("learning_python.txt")
print(path1.read_text())

print(f"\n Simpler Code 2 \n")
for line in contents.splitlines():
    print(line)

print(f"\n Simpler Code 3\n")
path1 = Path("learning_python.txt")
print(path1.read_text().replace("Python","C"))

print(f"\n Simpler Code 4 \n")
for line in contents.splitlines():
    print(line.replace("Python","C"))