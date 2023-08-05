# Arithmetic operators
x = 3
y = 2
# Addition
print(x + y)  # 5
# Subtraction
print(x - y)  # 1
# Multiplication
print(x * y)  # 6 (3*2)
# Division
print(x / y)  # (3/2 = 1.5)
# Modulus
print(x % y)  # 1 (remainder of 3/2)
# Exponentiation (x to the power of y)
print(x**y)  #  (3^2) = 9
# Floor division (rounds down to nearest whole number)
print(x // y)  # 1  (3/2 = 1.5, rounded down to 1)

age = 20
age += 1
print(age)  # 21 (age = age + 1)

# Comparison operators
x = 3
y = 2

# Equal to
print(x == y)  # False
# Not equal to (or 'different from')
print(x != y)  # True (3 is not equal to 2) (3 is different from 2) (3 is not 2)
# Greater than
print(x > y)  # True
# Less than
print(x < y)  # False
# Greater than or equal to
print(x >= y)  # True
# Less than or equal to
print(x <= y)  # False

# Logical operators
x = 3
y = 2

# AND
print(x == 3 and y == 2)  # True
# OR
print(x == 3 or y == 2)  # True (x is 3, so the first condition is True)
# NOT
print(
    not (x == 3 and y == 2)
)  # False (x is 3 and y is 2, so the condition is True. 'not True' is False) (not False is True) (not True is False)

# Identity operators (is, is not) (compares the memory location of two objects) (is checks if two objects are the same object) (is not checks if two objects are not the same object) (is and is not are used to compare objects, not values) (is and is not are two different operators) (is and is not are not the same as == and !=) (is and is not are used to compare objects, == and != are used to compare values)
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

# is
print(x is z)  # True (x and z are the same object)     (x is z)
print(x is y)  # False (x and y are not the same object) (x is y)
# is not
print(x is not z)  # False (x and z are the same object)     (x is not z)

# Membership operators
x = ["apple", "banana"]

# in
print("banana" in x)  # True (banana is in the list x)   ("banana" in x)
# not in
print(
    "pineapple" not in x
)  # True (pineapple is not in the list x) ("pineapple" not in x)

# Ternary operator
age = 22
print("Eligible") if age >= 18 else print("Not eligible")  # Eligible
