# Using RANGE
print("========================\n\n\n")

# print sum of n natural no
def sumOfN(n):
  sum = 0
  for i in range(1,n+1):
    sum += i

  print(f"Sum of {n} natural no is: {sum}") 

n = int(input("Enter a no: "))

# range wiht step size
def printEvenNoRange(start,end):
  for i in range(start,end,2):
    print(i)



# sumOfN(n)
# printEvenNoRange(2,11)









print("\n\n\n========================")
