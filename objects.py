# Objects in python

age = 20
name = "Swaroop"

print("{} was {} years old when he wrote this book".format(name, age))

print("Why is {} playing with that python?".format(name))

# The above two lines can also be written as
print(name + " was " + str(age) + " years old when he wrote this book")
print("Why is " + name + " playing with that python?")

items = ["apple", "banana", "cherry"]
print("I have {} fruits".format(len(items)))

items.append("orange")
print("I have {} fruits".format(len(items)))
