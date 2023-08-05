# Sets

# Sets are unordered collections of unique elements. There can only be one representative of the same object.
# Sets are unordered, so you cannot be sure in which order the items will appear.
# Sets are unchangeable, meaning that we cannot change the items after the set has been created.
# Sets cannot have two items with the same value.
# Sets are written with curly brackets.
# Sets are unordered, so you cannot be sure in which order the items will appear.
# Sets are unchangeable, meaning that we cannot change the items after the set has been created.
# Sets cannot have two items with the same value.
# Sets are written with curly brackets.
# Create a Set:
my_set = {"apple", "banana", "cherry"}
print(my_set)

# Access Items
# You cannot access items in a set by referring to an index or a key.
# But you can loop through the set items using a for loop, or ask if a specified value is present in a set, by using the in keyword.
# Loop through the set, and print the values:
for x in my_set:
    print(x)

# Check if "banana" is present in the set:
print("banana" in my_set)

# Change Items
# Once a set is created, you cannot change its items, but you can add new items.
# Add Items
# To add one item to a set use the add() method.
# To add more than one item to a set use the update() method.
# Add an item to a set, using the add() method:
my_set.add("orange")
print(my_set)

# Add multiple items to a set, using the update() method:
my_set.update(["orange", "mango", "grapes"])
print(my_set)

# Get the Length of a Set
# To determine how many items a set has, use the len() method.
# Get the number of items in a set:
print(len(my_set))

# Remove Item
# To remove an item in a set, use the remove(), or the discard() method.
# Remove "banana" by using the remove() method:
my_set.remove("banana")
print(my_set)

# Remove "banana" by using the discard() method:
my_set.discard("banana")
print(my_set)

# Note: If the item to remove does not exist, remove() will raise an error.
# Note: If the item to remove does not exist, discard() will NOT raise an error.
# You can also use the pop(), method to remove an item, but this method will remove the last item.
# Remember that sets are unordered, so you will not know what item that gets removed.
# The return value of the pop() method is the removed item.
# Remove the last item by using the pop() method:
x = my_set.pop()
print(x)
print(my_set)

# The clear() method empties the set:
my_set.clear()
print(my_set)

# The del keyword will delete the set completely:
del my_set
# print(my_set) # this will raise an error because the set no longer exists

# Join Two Sets
# There are several ways to join two or more sets in Python.
# You can use the union() method that returns a new set containing all items from both sets, or the update() method that inserts all the items from one set into another:
# The union() method returns a new set with all items from both sets:
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(
    set3
)  # {'a', 1, 2, 3, 'c', 'b'} # Note: Both union() and update() will exclude any duplicate items.

# Check if subset or superset
# Check if "set3" is a subset of "set1":
print(set3.issubset(set1))  # False

# Check if "set1" is a superset of "set3":
print(set1.issuperset(set3))  # False

# Check if "set4" is a subset of "set1":
set4 = {"a", "b", "c"}
print(set1.issubset(set4))  # True

# Check if "set1" is a superset of "set4":
print(set1.issuperset(set4))  # True

# The intersection() method will return a new set, that only contains the items that are present in both sets.
# Return a set that contains the items that exist in both set x, and set y:
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.intersection(y)
print(z)  # {'apple'}

# The intersection_update() method will keep only the items that are present in both sets.
# Keep the items that exist in both set x, and set y:
x.intersection_update(y)
print(x)  # {'apple'}

# The symmetric_difference() method will return a new set, that contains only the elements that are NOT present in both sets.
# Return a set that contains all items from both sets, except items that are present in both sets:
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.symmetric_difference(y)
print(z)  # {'google', 'banana', 'microsoft', 'cherry'}

# The symmetric_difference_update() method will keep only the elements that are NOT present in both sets.
# Keep the items that are not present in both sets:
x.symmetric_difference_update(y)
print(x)  # {'google', 'banana', 'microsoft', 'cherry'}
