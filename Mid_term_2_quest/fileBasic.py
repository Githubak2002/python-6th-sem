########### Basics of file ###########

# open - syntax var = open("path",mode='m')
# m - r(read),w(write),a(append),x(create and open in write mode)

# HELP!
# help(len) || help(math.sqrt) || help(greet) 

filePath = "fileBasic.txt"

# 1st method
with open(filePath, "w") as file:
  # write
  file.write("This is my first program on file handling in python\n")
  file.write("This is second line")
  # closing the file
  file.close()

# 2nd method
f = open(filePath,mode='r')

lol = f.read()
print("Reading the content of the file:")
print(lol)

f.close()

