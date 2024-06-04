# file = input("enter the name of the file: ")
# file content - Hi there! AI is helping us or destroying us 

file = "text.txt"
f = open(file, 'r')
txt = f.read()
# readLineFun = f.readline()
# readLinesFun = f.readlines()

print("Type of read function: ", type(txt))
# print("Type of read Line Fun: ", type(readLinesFun))
# print("Type of read Lines Fun: ", type(readLinesFun))


print(f"\nContent in file:\n{txt}")
# print(f"\nRead line function returns: {readLineFun}")
# print(f"\nRead lines function returns: {readLinesFun}")
f.close()

# Open the file in append mode
with open(file, 'a') as txt_file:
  txt_file.write('\nAI - Always Irritating Programers')
f.close()

with open(file,'r') as read_file:
  reading = read_file.read()
  print(f"\nFile content after appending →\n{reading}")
f.close()

# Open the file in write mode
with open(file, 'w') as txt_file:
  txt_file.write('Writting to the file \nHi there! \nAI is helping us or destroying us ')

with open(file,'r') as read_file:
  reading = read_file.read()
  print(f"\nFile content after writting in it →\n{reading}")
f.close()











"""
# File name
file = "text.txt"

# Open file
with open(file, 'r') as f:
    # Read entire content of the file
    txt = f.read()

    # Read a single line
    readLineFun = f.readline()

    # Read all lines into a list
    readLinesFun = f.readlines()

# Display types of return values
print("Type of read Line Fun:", type(readLineFun))
print("Type of read Lines Fun:", type(readLinesFun))
print("Type of read function:", type(txt))

# Display file content and return values
print(f"\nContent in file: {txt}")
print(f"\nRead line function returns: {readLineFun}")
print(f"\nRead lines function returns: {readLinesFun}")
"""