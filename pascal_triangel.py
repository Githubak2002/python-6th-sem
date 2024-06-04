
# Question - print the pattern [pascal triangle]
def print_pascal_triangle(rows):
    for i in range(rows):
        coef = 1
        for j in range(1, rows-i+1):
            print(" ", end="")
        
        for k in range(0, i+1):
            if k > 0:
                coef = coef * (i - k + 1) // k
            print(" ", coef, end="")
        print()

# Print Pascal's Triangle up to the 6th row
print_pascal_triangle(6)