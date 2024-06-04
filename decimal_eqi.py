# Using a for loop, write a program that prints out the decimal equivalents of 1/1 ,1/2 ... 1/10
print("\n\n")

for i in range(1, 11):
    x = 1/i
    print(f"1/{i} = {round(x,2)}")

# EXTRA - odd/even - printing from 1-n / n-1 using for loop
def even_or_odd(x1):
    return True if x1 % 2 == 0 else False

def print_n(n):
    for i1 in range(1,n+1):
        print(i1)
    # return "Printed from 1 to n"

def print_n_to_1(x1):
    for i2 in range(x1,0,-1):
        print(i2)


# print(f"Is the no entered even: {even_or_odd(x1)}")
# x1 = int(input("Enter a no: "))
x1 = 3
print(f"Printing for 1 to {x1}")
print_n(x1)
print(f"Printing for {x1} to 1")
print_n_to_1(x1)


print("\n\n") 