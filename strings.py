# Strings are immutable sequences of Unicode code points.

# Strings are sequences of characters, and share their basic methods of access with those other Python sequences – lists and tuples.


print("Hello, world!".upper())  # HELLO, WORLD!
print("Hello, world!".lower())  # hello, world!
print("Hello, world!".capitalize())  # Hello, world!
print("Hello, world!".title())  # Hello, World!
print(
    "Hello, world!".swapcase()
)  # hELLO, WORLD! //what is the difference between swapcase and title //title is for the first letter of each word and swapcase is for all letters in the string
print(
    "Hello, world!".casefold()
)  # hello, world! //what is the difference between casefold and lower //casefold is for unicode characters and lower is for ascii characters
print("Hello, world!".center(20))  #   Hello, world!
print("Hello, world!".center(20, "*"))  # ***Hello, world!***
print("Hello, world!".ljust(20))  # Hello, world!
print("Hello,world!".endswith("world!"))  # True
print("Hello,world Today!".split())  # ['Hello,', 'world!']
print("Hello,   world!".strip())  #
print("Hello, world!".join("123"))  # 1Hello,   world!2Hello,   world!3
print(
    "Hello, world!".lower().islower()
)  # True    //islower is a method of string class and lower is a method of string object
print("Hello, world!22".ljust(10))  # Hello, world!

name = "Adria13n"
# print(name[0])  # A
# print(name[1])  # d
print(name[-1])  #
my_string = "Hello, World!"
new_string = my_string.replace("World", "Python")
print(new_string)  # Hello, Python!
# replace first letter of string
print(my_string.replace("H", "J"))  # Jello, World!
my_string = "Hello, World!"
new_string = my_string[:7] + "Python" + my_string[13:]
print(new_string)  # Hello, Python!
my_string = "Hello,   World!"
new_string = my_string.strip()
print(new_string)  # "Hello, World!"
