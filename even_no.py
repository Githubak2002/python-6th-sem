#Write a Program for checking whether the given number is an even number ornot.
print("\n\n")

# Function to calculate distance between two points
def even_or_odd(x1):
    return True if x1 % 2 == 0 else False


x1 = int(input("Enter a no: "))

print(f"Is the no entered even: {even_or_odd(x1)}")


print("\n\n")