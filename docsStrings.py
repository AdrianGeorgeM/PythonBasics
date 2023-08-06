# Docstrings are not actually comments, but, they are documentation strings. These docstrings are within triple quotes. They are not assigned to any variable and therefore, at times, serve the purpose of comments as well.

# Example:


def double(num):
    """Function to double the value"""
    return 2 * num


print(double.__doc__)
print(double(5))
# Output:
# Function to double the value
# 10
# The docstrings are associated with the object as their __doc__ attribute. Therefore, we can access the docstrings of a function with the function name followed by __doc__.


# Example:
def add(a, b):
    """Function to add two numbers"""
    return a + b


print(add.__doc__)
print(add(4, 5))
# Output:
# Function to add two numbers
# 9
# Docstrings can be accessed anywhere in the function using the __doc__ attribute of the function. For example:
