# Open file in read mode
filePath = "fileFunctions.txt"

# file.read() - Read entire content of the file
f = open(filePath, "r")
content = f.read()
print("Content of the file:")
print(content)
f.close()

# file.readline() - Read a single line from the file
f = open(filePath, "r")
line = f.readline()
print("\nFirst line of the file:")
print(line)
f.close()

# file.lines() - Read all lines from the file and store them in a list
f = open(filePath, "r")
lines = f.readlines()
print("\nAll lines in list form:")
print(lines)
print("\nAll lines of the file:")
for line in lines:
    print(line, end="")  # Print each line without extra newline
f.close()

# file.write() - Open file in write mode
f = open(filePath, "w")
f.write("Hello, python!\n")
f.write("This is a new line.\n")
f.close()

# Read entire content of the file after writing
f = open(filePath, "r")
content = f.read()
print("\nContent of the file after writing:")
print(content)
f.close()

# file.seek() - Move file pointer to the beginning of the file
f = open(filePath, "r")
f.seek(0)

# file.tell() - Return the current position of the file pointer
position = f.tell()
print("\nCurrent position of the file pointer:", position)
f.close()
