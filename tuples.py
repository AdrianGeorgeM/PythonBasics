# Tuples are immutable lists (cannot be changed)
# Tuples are faster than lists
# Tuples are used to store data that will not be changed
# Tuples are written with round brackets

# Create a tuple
my_tuple = ("apple", "banana", "cherry")
print(my_tuple)

# Access tuple items
print(my_tuple[1])

# Change tuple values
# my_tuple[1] = "blackcurrant"  # This will raise an error
# print(my_tuple)

# Loop through a tuple
for x in my_tuple:
    print(x)

# Check if item exists
if "apple" in my_tuple:
    print("Yes, 'apple' is in the fruits tuple")

# Tuple length
print(len(my_tuple))

# Create tuple with one item
my_tuple = ("apple",)
print(type(my_tuple))

# NOT a tuple
my_tuple = "apple"
print(type(my_tuple))

# Join two tuples
tuple1 = ("a", "b", "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print(tuple3)

# Tuples are unchangeable, but they can contain mutable objects
# Like lists
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 2, 3)
tuple3 = (True, False, False)
tuple4 = ([1, 2, 3], [4, 5, 6])
print(tuple4)

# Tuple methods
# count()	Returns the number of times a specified value occurs in a tuple
# index()	Searches the tuple for a specified value and returns the position of where it was found
my_tuple = ("a", "p", "p", "l", "e")
print(my_tuple.count("p"))
print(my_tuple.index("l"))

# Unpacking a tuple
fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits
print(green)
print(yellow)
print(red)

# Using asterisk*
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits
print(green)
print(yellow)
print(red)
