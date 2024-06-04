print("\n\n")

# list1 = [1,5,6,2]

# LIST - 
n1 = int(input("Enter the no of ele in the list: "))
list1 = []
for i in range(n1):
    value = int(input())
    list1.append(value)

print(f"List is - {list1}")
list1.sort()
print(f"List after sort - {list1}")
list1.sort(reverse=True)
print(f"List after reverse - {list1}")


# Define two lists
l1 = [1, 2, 3, 4, 5]
l2 = [3, 4, 5, 6, 7]

# Get elements present in both lists using the 'and' operator
common_elements = [element for element in l1 if element in l2]
# common_elements = l1 and l2

print(f"common ele are - {common_elements}")


# list []
# tuple ()
# set {}
# dictionary {}
"""
List []: An ordered and mutable collection of items enclosed in square brackets [].
Tuple (): An ordered and immutable collection of items enclosed in parentheses ().
Set {}: An unordered and mutable collection of unique items enclosed in curly braces {}.
Dictionary {}: An unordered and mutable collection of key-value pairs enclosed in curly braces {}.
"""


print("\n\n")
