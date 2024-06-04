"""
1. list - array
2. .append
3. .pop 
4. f"Print with variable {list1[0].title()}"
5. list1.insert(3, "New ele at index 3")

"""

list1 = ["First", "Second", "Third"]
print(list1[0])
print(list1[-1])
print(list1[-2])

msg = f"My first list item's title is {list1[0].title()}"

print(msg)

list1.append("Fourth")
print(f"After appending: {list1}")

list1.insert(0, "Inserted")
list1.insert()
print(f"After inserting at index 0: {list1}")

list1.pop()
print(f"After popping the last item: {list1}")

list1.pop()
print(f"After popping another item: {list1}")
