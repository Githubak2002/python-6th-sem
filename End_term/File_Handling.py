# Open file (both method) - read the content of the file 
# open - syntax var = open("path",mode='m')
# m - r(read),w(write),a(append),x(create and open in write mode)

# HELP!
# help(len) || help(math.sqrt) || help(greet) 

file_path = "End_term/endterm.txt"

# first method
with open(file_path,mode='w') as file:
  file.write("welcome back\n")
  file.write("All will be fine")
  file.close()

# second method
file = open(file_path,mode='r')
x = file.read()
print("Content in the file is:")
print(x)