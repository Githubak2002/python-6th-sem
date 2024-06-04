print("\n\n")

# Get a string input from the user
user_string = input("Enter a string: ")
# Initialize an empty dictionary to store character counts
char_count = {}

# Count the number of characters in the string
for char in user_string:
    if char == " ":
        continue
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1

# Print the character counts
for char, count in char_count.items():
    # print(f"Char '{char}' appears {count} time(s) in the string.")
    print(f"'{char}' - {count} ")

print("\n\n")
