
# Importing Modules
import math

# Printing - loop
def basicFun():
  print(math.sqrt(4))
  print(21/4)     # 5.25
  print(21//4)    # 5 - floor division
  print("Printing 1 to 4 using for loop and range")
  for x in  range(5):
    print(x)              # 1 2 3 4 


# Basic data structure
def basicDataSruct():
  print("\nThere exist three data structure")
  DS = ['List - []','Tuples ()','Dictionaries - {"key":"value"}','Sets - {}']

  for x in DS:
    print(x)


# String and its function
def stringFun():
  str = "Hello python"
  print("\nstr is - ", str)
  print("str.upper() - ", str.upper())
  print("str.lower() - ", str.lower())
  print("str.split(" ") - ", str.split(" "))
  print('str.replace("python","py") - ', str.replace("python","py"))
  print('len(str) - ', len(str))
  

print("========================\n\n\n")

naam = input("Enter your name: ")
age = int(input("Enter your age: "))
print(f"hello {naam} your age is {age}\n")

# basicFun()
# basicDataSruct()
stringFun()






print("\n\n\n========================")



