# Lambda functions, also known as anonymous functions, are small, one-line 
# functions in Python that can have any number of arguments but can only 
# have one expression. They are useful for creating quick, throw-away 
# functions without needing to formally define a function using the def keyword.

# BASIC LAMBDA FUNCTIONS
print("\nBASIC LAMBDA FUNCTIONS EXAMPLE:\n")
# Traditional function
def add(x, y):
    return x + y

# Equivalent lambda function
add_lambda = lambda x, y: x + y

print(add(3, 4))        # Output: 7
print(add_lambda(3, 4)) # Output: 7

# USING LAMBDA FUNCTIONS WITH BUILT-IN FUNCTIONS
print("\nUSING LAMBDA FUNCTIONS WITH BUILT-IN FUNCTIONS EXAMPLE:\n")
print("Usage with map:")
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
print("numbers = [1, 2, 3, 4, 5], squared = list(map(lambda x: x**2, numbers))")  
print(f"squared: {squared}\n")

print("Usage with filter:")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("even_numbers = list(filter(lambda x: x % 2 == 0, numbers))")
print(f"even_numbers: {even_numbers}\n")  # Output: [2, 4, 6, 8, 10]

print("Usage with sorted:")
pairs = [(1, 'one'), (3, 'three'), (2, 'two'), (4, 'four')]
sorted_pairs = sorted(pairs, key=lambda pair: pair[1])
print("sorted_pairs = sorted(pairs, key=lambda pair: pair[1])")
print(f"sorted_pairs: {sorted_pairs}\n")  # Output: [(4, 'four'), (1, 'one'), (3, 'three'), (2, 'two')]

print("Usage with reduce:")
from functools import reduce

numbers = [1, 2, 3, 4, 5]
sum_of_squares = reduce(lambda x, y: x + y**2, numbers, 0)
print("sum_of_squares = reduce(lambda x, y: x + y**2, numbers, 0)")
print(f"sum_of_squares: {sum_of_squares}")  # Output: 55

