# BASIC LIST COMPREHENSION
print("\nBASIC LIST COMPREHENSION EXAMPLE:\n")
squares = [x**2 for x in range(10)]
print(f"\nsquares: [x**2 for x in range(10)]: {squares}\n")

# LIST COMPREHENSION WITH A CONDITION
print("\nLIST COMPREHENSION WITH A CONDITION EXAMPLE:\n")
squares = [x**2 for x in range(10) if x%2==0]
print(f"\nsquares of even numbers: [x**2 for x in range(10) if x%2==0]: {squares}\n")

# LIST COMPREHENSION WITH IF-ELSE
print("\nLIST COMPREHENSION WITH IF-ELSE EXAMPLE:\n")
classifier = ['Even' if x%2==0 else 'Odd' for x in range(10)]
print(f"\nEven Odd Classifier: ['Even' if x%2==0 else 'Odd' for x in range(10)]: {classifier}\n")

# NESTED LIST COMPREHENSION
print("\nNESTED LIST COMPREHENSION EXAMPLE:\n")
matrix = [[i*3 + j for j in range(3)] for i in range(3)]
print(f"\nMatrix: [[i*3 + j for j in range(3)] for i in range(3)]: {matrix}\n")

# LIST COMPREHENSION WITH MULTIPLE CONDITIONS
print("\nLIST COMPREHENSION WITH MULTIPLE CONDITIONS EXAMPLE:\n")
divisible_by_2_and_3 = [x for x in range(50) if x % 2 == 0 if x % 3 == 0]
print(f"\nDivisible by 2 and 3: [x for x in range(50) if x % 2 == 0 if x % 3 == 0]: {divisible_by_2_and_3}")

# LIST COMPREHENSION WITH MULTIPLE INPUT LISTS
print("\nLIST COMPREHENSION WITH MULTIPLE INPUT LISTS EXAMPLE:\n")
combined = [(x, y) for x in [1, 2, 3] for y in ['a', 'b', 'c']]
print(f"\nCombined: [(x, y) for x in [1, 2, 3] for y in ['a', 'b', 'c']]: {combined}")

# FLATTENING A 2D LIST
print("\nFLATTENING A 2D LIST EXAMPLE:\n")
nested = [[1, 2], [3, 4], [5, 6]]
flattened = [item for sublist in nested for item in sublist]
print(f"Nested: {nested}, Flattened: [item for sublist in nested for item in sublist]: {flattened}")

# SET OPERATIONS
print("\nSET OPERATIONS EXAMPLE:\n")
numbers = [1, 2, 2, 3, 4, 3, 5]
unique_numbers = [x for x in set(numbers)]
print(f"numbers: {numbers}, unique_numbers: [x for x in set(numbers)]: {unique_numbers}")
