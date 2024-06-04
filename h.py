def sum_of_even_fibonacci(n):
    even_fib1, even_fib2 = 0, 2
    sum_even = even_fib1 + even_fib2

    for _ in range(3, n + 1):
        even_fib_next = 4 * even_fib2 + even_fib1

        if even_fib_next > n:
            break

        sum_even += even_fib_next

        even_fib1, even_fib2 = even_fib2, even_fib_next

    return sum_even

# Example usage
n = int(input("Enter the maximum value of the Fibonacci sequence: "))
print("Sum of all even numbers in the Fibonacci series up to", n, ":", sum_of_even_fibonacci(n))
