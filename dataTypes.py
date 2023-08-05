# Data Types in Python
num1 = 2 + 4j
num2 = 3 + 2j
print(num1 + num2)  # (5+2j)x
# The imaginary unit is a mathematical concept that is used to represent the square root of -1. It is denoted by the symbol i in mathematics, but in some programming languages, including Python, i is often used as a variable name, so the symbol j is used instead to represent the imaginary unit.

# The purpose of the imaginary unit is to allow us to work with complex numbers, which have both a real part and an imaginary part. Complex numbers are used in many areas of mathematics and science, including electrical engineering, quantum mechanics, and signal processing, among others.
num3 = 2 + 4j
num4 = complex(3, 2)
print(num3 + num4)
# Define two complex numbers
complex_num1 = 3 + 4j
complex_num2 = 1 + 2j


result = complex_num1 * complex_num2
# 3*1 + 3*2j + 4j*1 + 4j*2j
# 3 + 6j + 4j + 8j^2
# 3 + 6j + 4j - 8
# -5 + 10j
print(result)  # Outputs: (-5+10j)

complex_num1 = 2 + 3j
complex_num2 = 1 + 4j
# (2 + 3j) * (1 + 4j)
result = complex_num1 * complex_num2
#  square root of -1
# (2 * 1) + (2 * 4j) + (3j * 1) - (3 * 4)
#  (2 + 8j) + (3j - 12)
#  (-10 + 11j)
print(result)  # (-10+11j)

# bUILT-IN FUNCTIONS
# abs()	Returns the absolute value of a number
print(abs(-4.7))  # 4.7
# round ()	Rounds a number
print(round(4.554))  # 5
# pow()	Returns the value of x to the power of y
print(pow(4, 3))  # 64
# min()	Returns the smallest number in a list
print(min(1, 2, 3, 4, 5))  # 1
# max()	Returns the largest number in a list
print(max(1, 2, 3, 4, 5))  # 5
# sum()	Returns the sum of all numbers in a list
print(sum([1, 2, 3, 4, 5]))  # 15
# len()	Returns the length of a string
print(len("Hello World"))  # 11
# sorted()	Returns a sorted list
print(sorted([5, 4, 3, 2, 1]))  # [1, 2, 3, 4, 5]
# reversed()	Returns a reversed iterator
print(list(reversed([5, 4, 3, 2, 1])))  # [1, 2, 3, 4, 5]
