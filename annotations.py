# Annotaions are used to add information to a program without affecting its execution. They are used for type checking and adding meta information to functions. Annotations are stored in the __annotations__ attribute of the function as a dictionary and have no effect on any other part of the function.


# Example:
def addInt(a: int, b: int) -> int:
    return a + b


print(addInt(4, 5))
print(addInt.__annotations__)

# Output:
# 9
# {'a': <class 'int'>, 'b': <class 'int'>, 'return': <class 'int'>}

# In the above example, we have annotated the function add() with the types of its parameters and the return value. These annotations are stored in the __annotations__ attribute of the function as a dictionary. The keys of the dictionary are the parameters and 'return' for the return value. The values of the dictionary are the types of the parameters and the return value.

# Annotations are not enforced by Python. They are merely stored in the __annotations__ attribute of the function. Therefore, we can use any type of object as a value in the __annotations__ dictionary.


# Example:
def add(a: int, b: str) -> list:
    return [a, b]


print(add(4, "5"))
