# Generators are a powerful feature in Python for creating iterators 
# in a memory-efficient way. They allow you to generate items 
# on-the-fly instead of creating and storing an entire sequence 
# in memory. 

# GENERATOR FUNCTIONS

print("\nGENERATOR FUNCTION EXAMPLE:\n")
# A generator function is defined like a normal function but uses the 
# yield keyword instead of return. When called, it returns a generator 
# object.
def count_up_to(n):
    i = 1
    while i <= n:
        yield i
        i += 1

# Using the generator
for number in count_up_to(5):
    print(number, end=' ')
print("\nNOTE: the numbers are generated one at a time, rather than creating a list of all numbers at once.")

# GENERATOR EXPRESSIONS
print("\nGENERATOR EXPRESSION EXAMPLE:\n")
# Similar to list comprehensions, but using parentheses instead of square brackets
squares = (x**2 for x in range(5))
print(f"squares: (x**2 for x in range(5)): {squares}")  # Output: <generator object <genexpr> at 0x...>
print(f"list(squares): {list(squares)}")  # Output: [0, 1, 4, 9, 16]
print("NOTE: Generator expressions are similar to list comprehensions, but uses parentheses instead of square brackets.")

# INFINITE GENERATORS
print("\nINFINITE GENERATORS EXAMPLE:\n")
# Generators can represents infinite sequences
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

fib = fibonacci()
for _ in range(10):
    print(next(fib), end=' ')
# Output: 0 1 1 2 3 5 8 13 21 34

# GENERATORS THAT CAN CHANGE STATE
print("\n\nGENERATORS THAT CAN CHANGE STATE EXAMPLE:\n")
def stateful_generator():
    state = 0
    while True:
        received = yield state
        if received is not None:
            state = received
        else:
            state += 1

gen = stateful_generator()
print(next(gen), end=' ')  # Output: 0
print(next(gen), end=' ')  # Output: 1
print(gen.send(10), end=' ')  # Output: 10
print(next(gen))  # Output: 11
print("NOTE: After printing 0 and 1, the gen.send changes 'received' in the generator function to 10 which changes the 'state' variable.")

# YIELDING FROM DIFFERENT ITERABLE
print("\nYIELDING FROM DIFFERENT ITERABLE EXAMPLE:\n")
def flatten(nested_list):
    for item in nested_list:
        if isinstance(item, list):
            yield from flatten(item)
        else:
            yield item

nested = [1, [2, 3, [4, 5]], 6]
print(f"nested: [1, [2, 3, [4, 5]], 6]: {list(flatten(nested))}")  # Output: [1, 2, 3, 4, 5, 6]
print("NOTE: After yielding 1, 'yield from flatten(item)' recursively flattens the list.")

# GENERATOR PIPELINES
print("\nGENERATOR PIPELINE EXAMPLE:\n")
def read_data():
    for i in range(10):
        yield i

def process_data(data):
    for item in data:
        if item % 2 == 0:
            yield item * 2

def format_data(data):
    for item in data:
        yield f"Item: {item}"

pipeline = format_data(process_data(read_data()))
for item in pipeline:
    print(item, end=' ')
# Output: Item: 0, Item: 4, Item: 8, ...

