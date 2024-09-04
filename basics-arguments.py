# BASIC POSITIONAL ARGUMENTS
print("\nBASIC POSITIONAL ARGUMENTS EXAMPLE:\n")
def greet(name, greeting):
    return f"{greeting}, {name}!\n"

print(greet("Alice", "Hello"))  # Output: Hello, Alice!

# KEYWORD ARGUMENTS
print("\nKEYWORD ARGUMENTS EXAMPLE:\n")
def greet(name, greeting):
    return f"{greeting}, {name}!\n"

print(greet(greeting="Hi", name="Bob"))  # Output: Hi, Bob!

# DEFAULT ARGUMENT
print("\nDEFAULT ARGUMENT EXAMPLE:\n")
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!\n"

print(greet("Charlie"))  # Output: Hello, Charlie!
print(greet("David", "Hi"))  # Output: Hi, David!

# *args (Variable-length positional arguments)
print("\n*args (Variable-length positional arguments) Example:\n")
def sum_all(*args):
    return f"{sum(args)}\n"

print(sum_all(1, 2, 3, 4))  # Output: 10

# **kwargs (Variable-length keyword arguments)
print("\n**kwargs (Variable-length keyword arguments) Example:\n")
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}\n")

print_info(name="Eve", age=30, city="New York")
# Output:
# name: Eve
# age: 30
# city: New York

# Combining *args and **kwargs
print("\nCombining *args and **kwargs Example:\n")
def print_all(*args, **kwargs):
    print(f"Positional arguments: {args}\n")
    print(f"Keyword arguments: {kwargs}\n")

print_all(1, 2, 3, name="Frank", job="Developer")
# Output:
# Positional arguments: (1, 2, 3)
# Keyword arguments: {'name': 'Frank', 'job': 'Developer'}

# Keyword only arguments
print("\nKeyword only arguments Example:\n")
def greet(*, name, greeting="Hello"):
    return f"{greeting}, {name}!\n"

print(greet(name="Grace"))  # Output: Hello, Grace!
# print(greet("Grace"))  # This would raise a TypeError

# Positional only arguments (Python 3.8+)
print("\nPositional only arguments (Python 3.8+) Example:\n")
print("Note: The / acts as a separator. The ones before are positional only")
def divide(a, b, /):
    return a / b

print(f"{divide(10, 2)}\n")  # Output: 5.0
# print(divide(a=10, b=2))  # This would raise a TypeError

# Argument Unpacking aka Decomposition
print("\nArgument Unpacking aka Decomposition Example:\n")
def greet(name, greeting):
    return f"{greeting}, {name}!"

args = ["Alice", "Hello"]
print(f"{greet(*args)}\n")  # Output: Hello, Alice!

kwargs = {"name": "Bob", "greeting": "Hi"}
print(f"{greet(**kwargs)}\n")  # Output: Hi, Bob!


