print("\n\n")

# Creating a dictionary
student = {
    "KEY": "VALUE",
    "name": "Anurag",
    "age": 20,
    "major": "Computer Science"
}
print(f"Student's Dictionary is - \n{student}")

# Accessing values in a dictionary 
print(student["name"])  # Output: Anurag
print(student.get("age"))  # Output: 20

# Modifying a dictionary
student["age"] = 21
print(student)  # Output: {'name': 'Alice', 'age': 21, 'major': 'Computer Science'}

# Adding a new key-value pair
student["year"] = 3
print(student)  # Output: {'name': 'Alice', 'age': 21, 'major': 'Computer Science', 'year': 3}

# Removing a key-value pair
del student["major"]
print(student)  # Output: {'name': 'Alice', 'age': 21, 'year': 3}

# Iterating through a dictionary
print("Itrating through dictionary sturent -")
for k, v in student.items():
    print(f"{k}: {v}")






print("\n\n")