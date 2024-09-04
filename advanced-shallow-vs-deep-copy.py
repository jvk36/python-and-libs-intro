# SHALLOW vs DEEP COPY
print("\nSHALLOW vs DEEP COPY EXAMPLE:\n")

print("SHALLOW COPY:\n")
import copy

# List example
original = [1, [2, 3], {'a': 4}]
shallow = copy.copy(original)

print(f"original = [1, [2, 3], {{'a': 4}}]: {original}")  # Output: [1, [2, 3], {'a': 4}]
print(f"shallow = copy.copy(original): {shallow}")   # Output: [1, [2, 3], {'a': 4}]

# Modifying a nested object
print("\nModifying a nested object:")
original[1][0] = 'X'
print("original[1][0] = 'X'")
print(f"original: {original}")  # Output: [1, ['X', 3], {'a': 4}]
print(f"shallow: {shallow}")   # Output: [1, ['X', 3], {'a': 4}]

# Modifying the top-level structure
print("\nModifying the top-level structure:")
original[0] = 'Y'
print("original[0] = 'Y'")
print(f"original: {original}")  # Output: ['Y', ['X', 3], {'a': 4}]
print(f"shallow: {shallow}")   # Output: [1, ['X', 3], {'a': 4}]
print('''
NOTE: A shallow copy creates a new object but references the same memory 
      addresses for nested objects. It only copies the top-level structure, 
      not the nested objects.
''')

print("\nDEEP COPY:\n")
# List example
original = [1, [2, 3], {'a': 4}]
print("original = [1, [2, 3], {'a': 4}]")
deep = copy.deepcopy(original)
print("deep = copy.deepcopy(original)")

print(f"original: {original}")  # Output: [1, [2, 3], {'a': 4}]
print(f"deep: {deep}")      # Output: [1, [2, 3], {'a': 4}]

# Modifying a nested object
print("Modifying a nested object")
original[1][0] = 'X'
print("original[1][0] = 'X'")
print(f"original: {original}")  # Output: [1, ['X', 3], {'a': 4}]
print(f"deep: {deep}")      # Output: [1, [2, 3], {'a': 4}]

# Modifying the top-level structure
print("Modifying the top-level structure")
original[0] = 'Y'
print("original[0] = 'Y'")
print(f"original: {original}")  # Output: ['Y', ['X', 3], {'a': 4}]
print(f"deep: {deep}")      # Output: [1, [2, 3], {'a': 4}]
print('''
NOTE: A deep copy creates a new object and recursively copies all nested 
      objects, creating independent copies at every level.
''')


