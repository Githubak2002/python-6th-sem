# Write a program to compute distance between two points taking input from theuser
print("\n\n")

import math
# Function to calculate distance between two points
def calculate_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)


x1 = int(input("Enter the x1: "))
y1 = int(input("Enter the y1: "))
x2 = int(input("Enter the x1 : "))
y2 = int(input("Enter the y1 : "))

print(f"Dis is b/n ({x1},{y1}) and ({x2},{y2}) is {calculate_distance(x1,y1,x2,y2)}")


print("\n\n")