# Higher-order functions are functions that can either take other functions as 
# arguments or return functions as their results (or both). They are a powerful 
# feature in Python that enables functional programming paradigms. 

# SIMPLE FUNCTION FACTORY
print("\nSIMPLE FUNCTION FACTORY EXAMPLE:\n")
# Function factories create/generate a new function each time it is called.
def power_function(n):
    def power(x):
        return x ** n
    return power

square = power_function(2)
cube = power_function(3)

print(square(4))  # Output: 16
print(cube(3))    # Output: 27
print("NOTE: Function factories create/generate a new function each time it is called.")

# CLOSURE
print("\nCLOSURE EXAMPLE:\n")
# A closure is a function that retains access to variables in its outer (enclosing) 
# scope even after the outer function has returned.
def counter():
    count = 0
    def increment():
        nonlocal count
        count += 1
        return count
    return increment

c = counter()
print(c())  # 1
print(c())  # 2
print(
'''
NOTE: A closure is a function that retains access to variables in its 
outer (enclosing) scope even after the outer function has returned.
''')

# DECORATORS
print("\nDECORATORS EXAMPLE:\n")
def uppercase_decorator(func):
    def wrapper(name):
        result = func(name)
        return result.upper()
    return wrapper

@uppercase_decorator
def greet(name):
    return "hello, " + name

print(greet("world!"))  # Output: HELLO, WORLD!

# FUNCTION COMPOSITION
print("\nFUNCTION COMPOSITION EXAMPLE:\n")
def compose(*functions):
    def inner(arg):
        for f in reversed(functions):
            arg = f(arg)
        return arg
    return inner

def add_one(x):
    return x + 1

def double(x):
    return x * 2

composed_function = compose(double, add_one)
print(composed_function(3))  # Output: 8 (double(add_one(3)))
print('''
NOTE: Function composition in Python allows you to combine multiple functions 
      to create a new function where the output of one function becomes the 
      input of the next.
''')

# PARTIAL FUNCTION 
print("\nPARTIAL FUNCTION EXAMPLE:\n")
from functools import partial

def power(base, exponent):
    return base ** exponent

square = partial(power, exponent=2)
cube = partial(power, exponent=3)

print(square(4))  # Output: 16
print(cube(3))    # Output: 27
print('''
NOTE: Partial function application is a technique in Python that allows you to 
      create a new function by fixing a certain number of arguments to an 
      existing function. This new function has fewer parameters than the 
      original. Python's functools.partial is used to implement this feature.
''')


