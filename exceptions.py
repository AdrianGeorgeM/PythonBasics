# Exceptions for the program to handle errors and exceptions in the program. Exceptions are raised when the program encounters an error during its execution. They disrupt the normal flow of the program and usually end it abruptly.
#
# Python provides us with many built-in exceptions to handle common errors. We can also create our own custom exceptions to handle errors that are specific to our code.

# Path: exceptions.py
# # Example:
# print(1 / 0)
#
# # Output:
# # Traceback (most recent call last):

# # File "exceptions.py", line 2, in <module>
# #     print(1 / 0)
# # ZeroDivisionError: division by zero

# # In the above example, we have tried to divide a number by zero. This raises a ZeroDivisionError exception. The program stops executing and Python prints the traceback of the exception to the console.

# # We can use the try...except statement to handle exceptions. The try block contains the code that might throw an exception. The except block contains the code that handles the exception. We can have multiple except blocks to handle different types of exceptions.

# # Example:
try:
    print(1 / 0)
except ZeroDivisionError:
    print("You cannot divide by zero!")

# # Output:
# # You cannot divide by zero!

# # In the above example, we have handled the ZeroDivisionError exception using the except block. The program does not terminate abruptly and prints the message to the console.

# # We can also use the else block with the try...except statement. The code inside the else block is executed if no exception is raised.

# # Example:
try:
    print(1 / 1)
except ZeroDivisionError:
    print("You cannot divide by zero!")
else:
    print("No exception was raised!")

# # Output:
# # 1.0
# # No exception was raised!

# # In the above example, we have used the else block with the try...except statement. Since no exception was raised, the code inside the else block is executed.

# # We can also use the finally block with the try...except statement. The code inside the finally block is executed whether or not an exception is raised.

# # Example:
try:
    print(1 / 0)
except ZeroDivisionError:
    print("You cannot divide by zero!")
finally:
    print("This code will run no matter what!")

# # Output:
# # You cannot divide by zero!
# # This code will run no matter what!

# # In the above example, we have used the finally block with the try...except statement. The code inside the finally block is executed whether or not an exception is raised.

# # We can also use the raise statement to raise an exception. We can raise a built-in exception or a custom exception.

# # Example:
# raise ZeroDivisionError("You cannot divide by zero!")

# # Output:
# # Traceback (most recent call last):
# #   File "exceptions.py", line 2, in <module>
# #     raise ZeroDivisionError("You cannot divide by zero!")

# # ZeroDivisionError: You cannot divide by zero!

# # In the above example, we have raised a ZeroDivisionError exception. The program stops executing and Python prints the traceback of the exception to the console.

# # We can also raise a custom exception. To do so, we need to create a class that inherits from the Exception class.


# # Example:
class MyCustomError(Exception):
    pass


raise MyCustomError("Something went wrong!")

# # Output:
# # Traceback (most recent call last):
# #   File "exceptions.py", line 2, in <module>
# #     raise MyCustomError("Something went wrong!")

# # __main__.MyCustomError: Something went wrong!

# # In the above example, we have raised a custom exception. The program stops executing and Python prints the traceback of the exception to the console.
