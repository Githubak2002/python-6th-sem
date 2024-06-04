# DICTONARY

# student dict
stud = {
  "name":"khush",
  "age":22,
  "major":"computer science"
}

print("========================\n\n\n")

# accessing values
print(f"Student name: {stud['name']}")

# deleting values
del stud['major']

# adding key value pair
stud['marks'] = 98

# iterating over student dict
for key in stud:
  print(f"{key} ':' {stud[key]}")






print("\n\n\n========================")
