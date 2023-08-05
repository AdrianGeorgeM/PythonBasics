# Functions


def hello(name):
    print("Hello World " + name)


hello("John")
hello("Mike")


def add(num1=5, num2=5):
    return num1 + num2


# print(add(1, 2))
# print(add(3, 4))
add()


def names(*args):
    for name in args:
        print(name)


names("John", "Mike", "Kane", "Kevin")


# return statement
def talk(pharse):
    def say(word):
        print(word)

        words = pharse.split(" ")
        for word in words:
            say(word)


talk("Hello World")


# nonlocal keyword is used to work with variables inside nested functions, where the variable should not belong to the inner function. Use the keyword nonlocal to declare that the variable is not local.
def outer():
    x = "local"

    def inner():
        nonlocal x
        x = "nonlocal"
        print("inner:", x)

    inner()
    print("outer:", x)


outer()
