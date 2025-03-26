# Object-Oriented Programming (OOP) is a programming paradigm that allows structuring code using objects and classes. It helps in making the code more reusable, modular, and organized.
#
#  Class & Object
#Class → A blueprint for creating objects

# Object → An instance of a class
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def show_info(self):
        print(f"This is a {self.brand} {self.model}")

# Creating Objects
car1 = Car("Tesla", "Model S")
car2 = Car("BMW", "X5")

car1.show_info()  # Output: This is a Tesla Model S
car2.show_info()  # Output: This is a BMW X5

# constructor is a special method that gets called automatically when an object is created. In Python, the constructor is defined using the __init__ method.
# The __init__ function is a special method in Python classes that initializes an object’s attributes when an instance of the class is created
class Person:
    def __init__(self, name, age):
        self.name = name  # Instance variable
        self.age = age    # Instance variable

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")

# Creating an object
person1 = Person("Aman", 25)
person1.display()

# Why Use __init__?
 #✔️ Automatically initializes object properties
# ✔️ Reduces redundant code
# ✔️ Provides default values
# Default Constructor (No Parameters)
#If no arguments are passed, a constructor can still initialize default values.
class Student:
    def __init__(self):
        print("Student object created!")

# Creating an object
s1 = Student()

#  Parameterized Constructor
#A constructor can accept parameters to set initial values.
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def show_info(self):
        print(f"Car: {self.brand} {self.model}")

# Creating Objects
c1 = Car("Tesla", "Model 3")
c2 = Car("BMW", "X5")

c1.show_info()  # Car: Tesla Model 3
c2.show_info()  # Car: BMW X5

# Constructor with Default Values
# We can also set default values in the constructor.
class Employee:
    def __init__(self, name="Unknown", salary=50000):
        self.name = name
        self.salary = salary

    def display(self):
        print(f"Employee: {self.name}, Salary: {self.salary}")

# Creating objects
e1 = Employee("John", 70000)
e2 = Employee()  # Uses default values

e1.display()  # Employee: John, Salary: 70000
e2.display()  # Employee: Unknown, Salary: 50000

# Can We Have Multiple __init__ Methods?
#❌ No, Python does not support multiple __init__ methods.
# If you define multiple __init__, only the last one will work.

#🔹 Alternative: Use default arguments or *args.
class Book:
    def __init__(self, title, author="Unknown"):
        self.title = title
        self.author = author

    def display(self):
        print(f"Book: {self.title}, Author: {self.author}")

b1 = Book("Python Basics", "John Doe")
b2 = Book("Machine Learning")  # Uses default author

b1.display()  # Book: Python Basics, Author: John Doe
b2.display()  # Book: Machine Learning, Author: Unknown

# Destructor (__del__ Method)
# Python also has a destructor, which is the __del__ method. It is called when an object is deleted or goes out of scope.

class Demo:
    def __init__(self):
        print("Object Created!")

    def __del__(self):
        print("Object Destroyed!")

# Creating and deleting an object
obj = Demo()
del obj  # Calls __del__

