file = open('sample3.txt', 'r')
content = file.read()
print(content)
file.close()

file = open('sample3.txt', 'w')
file.write("New content written.\n")
file.close()

file = open('sample3.txt', 'a')
file.write("Appended content.\n")
file.close()

file = open('sample3.txt', 'r')
print(file.read())
file.close()

file = open('sample3.txt', 'r')
lines = file.readlines()
file.close()

file = open('sample3.txt', 'w')
file.write("")
file.close()

import os
if os.path.exists('sample3.txt'):
    print("File exists.")
else:
    print("File does not exist.")