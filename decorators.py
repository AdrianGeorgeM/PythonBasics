# Decorators
# Decorators are a way to dynamically alter the functionality of your functions. They are very useful to wrap functionality with the same code over and over again. For example, authentication, logging, and instrumentation are all examples of use cases for decorators.

# Functions in Python are first class citizens. This means that they support operations such as being passed as an argument, returned from a function, modified, and assigned to a variable. This is what enables us to use them as decorators.

# Let’s start with an example:


def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")

    return wrapper


def say_whee():
    print("Whee!")


say_whee = my_decorator(say_whee)

say_whee()

# Output:
# Something is happening before the function is called.
# Whee!
# Something is happening after the function is called.

# So, what just happened? The decorator was called before the function definition. In turn, the decorator returned the wrapper function object and assigned it to the function defined in the decorator. If you’re having trouble understanding this, think of it this way: @my_decorator is just an easier way of saying say_whee = my_decorator(say_whee).

# Reusing Decorators


# Let’s move on to a slightly more involved example:


def do_twice(func):
    def wrapper_do_twice():
        func()
        func()

    return wrapper_do_twice


@do_twice
def say_whee():
    print("Whee!")


say_whee()

# Output:
# Whee!
# Whee!

# This example also demonstrates that a decorator can do its work before the function it decorates is called.

# However, there’s one downside to this code as it is. The docstring of the original function is lost, because a wrapper function with a different docstring is returned by the decorator. (There are ways to fix this, but they are out of scope for this article.)

# To fix this, decorators should use the @functools.wraps decorator, which will preserve information about the original function. Update decorators.py as follows:

import functools


def do_twice(func):
    @functools.wraps(func)
    def wrapper_do_twice():
        func()
        func()

    return wrapper_do_twice


@do_twice
def say_whee():
    print("Whee!")


say_whee()

# Output:
# Whee!
# Whee!
