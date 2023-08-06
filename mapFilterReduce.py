# Map Filter Reduce
# Map: Apply same operation to each element of a sequence
# Filter: Apply a condition to each element of a sequence
# Reduce: Apply an operation to each element of a sequence and return a single value

# Map
# map(function, sequence)
# function: function to apply to each element of the sequence
# sequence: sequence to apply the function to

# Example for map easy example
numbers = [1, 2, 3, 4, 5]


def square(x):
    return x**2


# map(function, iterable)
squared = map(square, numbers)
# print(squared)
# print(list(squared))


def double(x):
    return x * 2


doubled = map(
    double, numbers
)  # map object is an iterator so we can use it in a for loop or convert it to a list
# print(doubled)
# print(list(doubled))

# Example for map with lambda
numbers = [1, 2, 3, 4, 5]
squared = map(lambda x: x * 2, numbers)
# print(squared)
# print(list(squared))

# Example for map with multiple iterables
numbers1 = [1, 2, 3, 4, 5]
numbers2 = [6, 7, 8, 9, 10]
added = map(lambda x, y: x + y, numbers1, numbers2)
# print(added)
# print(list(added))

# Filter
# filter(function, sequence)
# function: function to apply to each element of the sequence
# sequence: sequence to apply the function to and filter out elements that return False for the function applied to them (i.e. the function returns True) and keep elements that return True for the function applied to them (i.e. the function returns True)

# Example for filter easy example
numbers = [1, 2, 3, 4, 5]


# Example for filter with lambda
numbers = [1, 2, 3, 4, 5]
evens = filter(lambda x: x % 2 == 0, numbers)
print(evens)
print(list(evens))

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)

strings = ["hello", "", "world", "", "python"]
non_empty = list(filter(lambda x: x != "", strings))
print(non_empty)  # Output: ["hello", "world", "python"]

words = ["apple", "banana", "cherry", "date", "elderberry"]
starts_with_c = list(filter(lambda x: x.startswith("c"), words))
print(starts_with_c)  # Output: ["cherry"]

strings = ["hello", "", "world", "", "python"]
non_empty = list(filter(lambda x: x != "", strings))
print(non_empty)  # Output: ["hello", "world", "python"]

numbers = [-3, -2, -1, 0, 1, 2, 3]
positives = list(filter(lambda x: x >= 0, numbers))
print(positives)  # Output: [0, 1, 2, 3]

# Reduce
# reduce(function, sequence)
# function: function to apply to each element of the sequence and reduce the sequence to a single value (e.g. sum, product, etc.) and return the reduced value of the sequence
# sequence: sequence to apply the function to and reduce to a single value

# Example for reduce easy example
expenses = [
    ("Dinner", 80),
    ("Coffee", 4),
    ("Movie", 10),
]

total = 0
for expense in expenses:
    total += expense[1]
print(total)


doubled = map(
    double, numbers
)  # map object is an iterator so we can use it in a for loop or convert it to a list
# print(doubled)
# print(list(doubled))

# Example for map with lambda
numbers = [1, 2, 3, 4, 5]
squared = map(lambda x: x * 2, numbers)
# print(squared)
# print(list(squared))

# Example for map with multiple iterables
numbers1 = [1, 2, 3, 4, 5]
numbers2 = [6, 7, 8, 9, 10]
added = map(lambda x, y: x + y, numbers1, numbers2)
# print(added)
# print(list(added))

# Filter
# filter(function, sequence)
# function: function to apply to each element of the sequence
# sequence: sequence to apply the function to and filter out elements that return False for the function applied to them (i.e. the function returns True) and keep elements that return True for the function applied to them (i.e. the function returns True)

# Example for filter easy example
numbers = [1, 2, 3, 4, 5]


def is_even(x):
    return x % 2 == 0


# filter(function, iterable)
evens = filter(is_even, numbers)
print(evens)
print(list(evens))

# Example for filter with lambda
numbers = [1, 2, 3, 4, 5]
evens = filter(lambda x: x % 2 == 0, numbers)
print(evens)
print(list(evens))

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)

strings = ["hello", "", "world", "", "python"]
non_empty = list(filter(lambda x: x != "", strings))
print(non_empty)  # Output: ["hello", "world", "python"]

words = ["apple", "banana", "cherry", "date", "elderberry"]
starts_with_c = list(filter(lambda x: x.startswith("c"), words))
print(starts_with_c)  # Output: ["cherry"]

strings = ["hello", "", "world", "", "python"]
non_empty = list(filter(lambda x: x != "", strings))
print(non_empty)  # Output: ["hello", "world", "python"]

numbers = [-3, -2, -1, 0, 1, 2, 3]
positives = list(filter(lambda x: x >= 0, numbers))
print(positives)  # Output: [0, 1, 2, 3]

# Reduce
# reduce(function, sequence)
# function: function to apply to each element of the sequence and reduce the sequence to a single value (e.g. sum, product, etc.) and return the reduced value of the sequence
# sequence: sequence to apply the function to and reduce to a single value

# Example for reduce easy example
expenses = [
    ("Dinner", 80),
    ("Coffee", 4),
    ("Movie", 10),
]

total = 0

for expense in expenses:
    total += expense[1]

print(total)

# Example for reduce with lambda
from functools import reduce

expenses = [
    ("Dinner", 80),
    ("Coffee", 4),
    ("Movie", 10),
]

total = reduce(lambda x, y: x + y[1], expenses, 0)
print(total)
