print(" ") 
print(" ")
print(" ")

s = "Pyhton programing"
# sliceing a string
print(s[slice(5,10)])
print(s[5:10])

# Length
print(f"Length of string s = {len(s)}")

s = "This is a String"

# Basic slicing
print(s[0:4])  # 'This' - From index 0 to 3
print(s[:4])   # 'This' - Omits start index, assumes start from 0
print(s[10:16]) # 'String' - From index 10 to 15
print(s[10:])  # 'String' - Omits end index, goes to the end of the string

# Negative indices
print(s[-6:])  # 'String' - Last 6 characters
print(s[:-7])  # 'This is a' - Everything except the last 7 characters
print(s[-6:-2]) # 'Stri' - From the 6th last to the 2nd last character

# Step in slicing
print(s[::2])  # 'Ti s tig' - Every second character from start to end
print(s[1::2]) # 'hsi  tig' - Every second character, starting from index 1
print(s[::-1]) # 'gnirtS a si sihT' - Reverses the string
print(s[::-2]) # 'git s iT' - Every second character in reverse order

# Combining indices and steps
print(s[2:10:2]) # 'i s ' - Every second character from index 2 to 9
print(s[-1:-7:-1]) # 'gnirtS' - Reverses the last 6 characters
print(s[5::-1])  # ' si sih' - Reverse from start to index 5
print(s[:5:-1])  # 'gnirtS a s' - From the end to index 5 in reverse order, excluding index 5

# Edge cases
print(s[:])    # 'This is a String' - The whole string
print(s[::])   # 'This is a String' - The whole string, equivalent to s[:]
print(s[::3])  # 'Tss rg' - Every third character from start to end
print(s[20:])  # '' - Accessing beyond the end returns an empty string
