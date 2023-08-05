# Classes  in python


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name} and I'm {self.age} years old.")


# Student class inherits from Person
class Student(Person):
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.grade = grade

    def study(self):
        print(f"I'm studying and I'm in grade {self.grade}.")


s1 = Student("Adrian", 20, "Sophomore")
s1.greet()  # prints "Hello, my name is Alice and I'm 20 years old."
s1.study()  # prints "I'm studying and I'm in grade Sophomore."


class MyClass:
    class_var = "I'm a Class Variable"

    def __init__(self, name):
        self.name = name  # This is an instance variable


p1 = MyClass("Alice")
p2 = MyClass("Bob")

print(p1.class_var)  # prints "I'm a Class Variable"
print(p2.class_var)  # prints "I'm a Class Variable"
