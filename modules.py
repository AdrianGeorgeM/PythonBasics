# Modules

# A module is a file containing Python definitions and statements. A module can define functions, classes and variables. A module can also include runnable code.

# Example
# Save this code in a file named mymodule.py


def greeting(name):
    print("Hello, " + name)


# Use a Module
# Now we can use the module we just created, by using the import statement:

import mymodule

mymodule.greeting("Jonathan")
# Note: When using a function from a module, use the syntax: module_name.function_name.

# Variables in Module
# The module can contain functions, as already described, but also variables of all types (arrays, dictionaries, objects etc):

# Example
# Save this code in the file mymodule.py

person1 = {"name": "John", "age": 36, "country": "Norway"}
# Example
# Import the module named mymodule, and access the person1 dictionary:

import mymodule

a = mymodule.person1["age"]
print(a)
# Naming a Module
# You can name the module file whatever you like, but it must have the file extension .py

# Re-naming a Module
# You can create an alias when you import a module, by using the as keyword:

# Example
# Create an alias for mymodule called mx:

import mymodule as mx

a = mx.person1["age"]
print(a)

# Built-in Modules
# There are several built-in modules in Python, which you can import whenever you like.

# Example
# Import and use the platform module:

import platform

x = platform.system()
print(x)
# Using the dir() Function
# There is a built-in function to list all the function names (or variable names) in a module. The dir() function:

# Example
# List all the defined names belonging to the platform module:

import platform
