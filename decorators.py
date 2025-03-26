# A decorator in Python is a higher-order function that modifies another function without changing its structure. It allows us to add extra functionality to functions dynamically.
def my_decorator(func):
    def wrapper():
        print("Before calling the function")
        func()
        print("After calling the function")
    return wrapper

@my_decorator
def say_hello():
    print("Hello, World!")

say_hello()

# Decorators with Arguments
# If the function we want to decorate takes arguments, the wrapper function should also take them.
def smart_divide(func):
    def wrapper(a, b):
        if b == 0:
            print("Cannot divide by zero!")
            return
        return func(a, b)
    return wrapper

@smart_divide
def divide(a, b):
    return a / b

print(divide(10, 2))  # ✅ Works
print(divide(5, 0))   # ❌ Error handled

# Using Multiple Decorators

def decorator1(func):
    def wrapper():
        print("Decorator 1 applied")
        func()
    return wrapper

def decorator2(func):
    def wrapper():
        print("Decorator 2 applied")
        func()
    return wrapper

@decorator1
@decorator2
def greet():
    print("Hello!")

greet()
