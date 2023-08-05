# Loops


# While loop
condition = False
while condition == True:
    print("Hello")
    condition = False

# For loop
for i in range(10):
    print(i)

# For loop with list
my_list = [1, 2, 3, 4, 5]
for i in my_list:
    print(i)

# For loop with tuple
my_tuple = (1, 2, 3, 4, 5)
for i in my_tuple:
    print(i)

# # For loop with dictionary
my_dict = {"name": "John", "age": 36}
for i in my_dict:
    print(i)
    print(my_dict[i])

# For loop with dictionary keys
for i in my_dict.keys():
    print(i)

# For loop with dictionary values
for i in my_dict.values():
    print(i)

# For loop with dictionary items
for (
    i
) in (
    my_dict.items()
):  # Returns a tuple of key and value pair in a list of tuples [(key, value)]
    print(i)

# For loop with dictionary items
for key, value in my_dict.items():
    print(key, value)

# For loop with dictionary items
for key, value in my_dict.items():
    print(key)
    print(value)
