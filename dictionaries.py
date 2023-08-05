# Dictionaries are used to store data values in key:value pairs.
# A dictionary is a collection which is ordered*, changeable and does not allow duplicates.
# Dictionaries are written with curly brackets, and have keys and values:

# Create and print a dictionary:
my_dict = {"brand": "Ford", "model": "Mustang", "year": 1964}
print(my_dict)

# Accessing Items
# You can access the items of a dictionary by referring to its key name, inside square brackets:
x = my_dict["model"]
print("access " + x)

# There is also a method called get() that will give you the same result:
x = my_dict.get("model")
print(x)

# Change Values
# You can change the value of a specific item by referring to its key name:
my_dict["year"] = 2018
# print(my_dict)

# Loop Through a Dictionary
# You can loop through a dictionary by using a for loop.
# When looping through a dictionary, the return value are the keys of the dictionary,
# but there are methods to return the values as well.
# Print all key names in the dictionary, one by one:
for x in my_dict:
    print(x)

# Print all values in the dictionary, one by one:
for x in my_dict:
    print(my_dict[x])

# You can also use the values() function to return values of a dictionary:
for x in my_dict.values():
    print(x)

# Loop through both keys and values, by using the items() function:
for x, y in my_dict.items():
    print(x, y)

# Check if Key Exists
# To determine if a specified key is present in a dictionary use the in keyword:
if "model" in my_dict:
    print("Yes, 'model' is one of the keys in the my_dict dictionary")

# Dictionary Length
# To determine how many items (key-value pairs) a dictionary has, use the len() method.
print(len(my_dict))

# Adding Items
# Adding an item to the dictionary is done by using a new index key and assigning a value to it:
my_dict["color"] = "red"
print(my_dict)

# Removing Items
# There are several methods to remove items from a dictionary:
# The pop() method removes the item with the specified key name:
my_dict.pop("model")
print(my_dict)

# The popitem() method removes the last inserted item (in versions before 3.7, a random item is removed instead):
my_dict.popitem()
print(my_dict)

# The del keyword removes the item with the specified key name:
del my_dict["year"]
print(my_dict)

# The clear() method empties the dictionary:
my_dict.clear()
print(my_dict)


# The del keyword can also delete the dictionary completely:
del my_dict
# print(my_dict)  # this will cause an error because "my_dict" no longer exists.

# Copy a Dictionary
# You cannot copy a dictionary simply by typing dict2 = dict1, because: dict2 will only be a reference to dict1,
# and changes made in dict1 will automatically also be made in dict2.
# There are ways to make a copy, one way is to use the built-in Dictionary method copy().
my_dict = {"brand": "Ford", "model": "Mustang", "year": 1964}
my_dict2 = my_dict.copy()
print(my_dict2)

# Another way to make a copy is to use the built-in function dict().
my_dict3 = dict(my_dict)
print(my_dict3)

# Nested Dictionaries
# A dictionary can also contain many dictionaries, this is called nested dictionaries.
# Create a dictionary that contain three dictionaries:
my_family = {
    "child1": {"name": "Emil", "year": 2004},
    "child2": {"name": "Tobias", "year": 2007},
    "child3": {"name": "Linus", "year": 2011},
}
print(my_family)
