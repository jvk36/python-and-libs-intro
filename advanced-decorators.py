# ******** decorators intro *************************************************
# A decorator in Python is a function that modifies the behavior of another 
# function or method. It allows you to wrap another function to extend its 
# behavior without explicitly modifying it. Decorators are often used to add 
# cross-cutting concerns like logging, access control, memoization, or timing 
# to existing functions..
#
# Basic Decorator Function: A decorator is simply a function that takes 
#   another function as an argument and returns a new function.
#
# NOTE: Here, @my_decorator is syntactic sugar for 
#       say_hello = my_decorator(say_hello).
# ***************************************************************************** 
def my_decorator(func):
    def wrapper():
        print("Something before the function runs")
        func()
        print("Something after the function runs")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()

# ******** decorator functions with *args and **kwargs ************************
# When the decorator needs to work with functions that have arbitrary 
# arguments, you can use *args and **kwargs to ensure compatibility with any 
# function signature.
#
# NOTE: The wrapper function takes any arguments (*args and **kwargs) and 
#       passes them to the decorated function.
# ***************************************************************************** 
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Arguments passed: {args}, {kwargs}")
        result = func(*args, **kwargs)
        return result
    return wrapper

@my_decorator
def add(x, y):
    return x + y

print(add(5, 10))


# ******** modifying decorator behavior using wrapper functions with args *****
# Decorators can also take arguments to modify their behavior.
#
# NOTE: Here, @repeat(3) calls the outer repeat function with n = 3, which 
#       then returns the actual decorator.
# ***************************************************************************** 
def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")

# ******** @classmethod and @staticmethod built-in decorators *****************
# @classmethod methods  have a mandatory first argument, but this argument 
# isn't a class instance self but is the uninstantiated class cls.
#
# @staticmethod decorator is similar to @classmethod in that it can be called 
# from an uninstantiated class object, although in this case there is no cls 
# parameter passed to its method. 
#
# NOTE: The cls parameter is the class object which allows @classmethod methods 
#       to easily instantiate the class. The lack of this cls parameter in 
#       @staticmethod methods make them true static methods in the traditional 
#       sense. 
# ***************************************************************************** 
class MyClass:
    count = 0
    
    @classmethod
    def increment_count(cls):
        cls.count += 1

    @staticmethod
    def static_method():
        print("This is a static method")

MyClass.increment_count()
print(MyClass.count)
MyClass.static_method()

# ******** chaining multiple decorators ***************************************
# You can apply multiple decorators to a single function. 
#
# NOTE: Here, @greet_decorator wraps greet, and @uppercase wraps the result of 
#       the @greet_decorator function.
# ***************************************************************************** 
def uppercase(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper()
    return wrapper

def greet_decorator(func):
    def wrapper(*args, **kwargs):
        print("Executing greeting function")
        return func(*args, **kwargs)
    return wrapper

@uppercase
@greet_decorator
def greet(name):
    return f"Hello, {name}"

print(greet("Alice"))

# ******** decorators with return values that are modified ********************
# Decorators can have return values and you can also modify the return value of 
# the decorated function. 
# ***************************************************************************** 
def add_2(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs) + 2
    return wrapper

@add_2
def get_number():
    return 10

print(get_number())

# ******** Class based decorators *********************************************
# Instead of using functions as decorators, you can use classes with a 
# __call__ method. This allows for more complex state management. 
#
# NOTE: Here, MyDecorator is initialized when say_hello is defined, and the 
#       __call__ method is invoked when say_hello is called.
# ***************************************************************************** 
class MyDecorator:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print("Class decorator is being used")
        return self.func(*args, **kwargs)

@MyDecorator
def say_hello(name):
    print(f"Hello, {name}")

say_hello("Alice")
