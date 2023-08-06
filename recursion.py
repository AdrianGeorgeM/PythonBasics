# Recursion

# 1. Factorial explain with recursion and iteration (for loop)
# 2. Fibonacci sequence
# 3. Ackermann


def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(5))


# Fibonacci sequence: 1,
def fibonacci(n):
    if n <= 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(5))


def ackermann(m, n):
    if m == 0:
        return n + 1
    elif n == 0:
        return ackermann(m - 1, 1)
    else:
        return ackermann(m - 1, ackermann(m, n - 1))


print(ackermann(3, 4))
