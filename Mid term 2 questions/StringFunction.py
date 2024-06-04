# Example string
s = "   Hello, world!   "

# strip(): Removes leading and trailing whitespace characters
print(s.strip())  # Output: "Hello, world!"
# lstrip(): Removes leading whitespace characters
print(s.lstrip())  # Output: "Hello, world!   "
# rstrip(): Removes trailing whitespace characters
print(s.rstrip())  # Output: "   Hello, world!"

# lower(): Converts the string to lowercase
print(s.lower())  # Output: "   hello, world!   "

# upper(): Converts the string to uppercase
print(s.upper())  # Output: "   HELLO, WORLD!   "

# capitalize(): Capitalizes the first character of the string
print(s.capitalize())  # Output: "   hello, world!   "

# title(): Converts the first character of each word to uppercase
print(s.title())  # Output: "   Hello, World!   "

# swapcase(): Swaps the case of each character in the string
print(s.swapcase())  # Output: "   hELLO, WORLD!   "

# replace(): Replaces occurrences of a substring with another substring
print(s.replace("Hello", "Hi"))  # Output: "   Hi, world!   "

# split(): Splits the string into a list of substrings based on a delimiter
print(s.split(","))  # Output: ['   Hello', ' world!   ']

# join(): Joins the elements of an iterable (e.g., list) into a string using the specified separator
words = ["Hello", "world!"]
print(" ".join(words))  # Output: "Hello world!"
