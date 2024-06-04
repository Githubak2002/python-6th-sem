def calculate_even_sum_fibonacci(n):
    if n <= 0:
        return 0

    fib1, fib2 = 0, 1
    sum_even = 0

    for _ in range(2, n + 1):
        fib_next = fib1 + fib2  # Next Fibonacci number

        if fib_next % 2 == 0:
            sum_even += fib_next

        fib1, fib2 = fib2, fib_next

    return sum_even

n = int(input("Enter the value of n: "))
print("Sum of all even numbers in the nth Fibonacci series:", calculate_even_sum_fibonacci(n))
