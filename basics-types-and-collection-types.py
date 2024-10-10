print("Integer (int) - Represents whole numbers:")
age = 25
print(age)  # Output: 25
print(type(age))  # Output: <class 'int'>

print("Float (float) - Represents decimal numbers:")
pi = 3.14159
print(pi)  # Output: 3.14159
print(type(pi))  # Output: <class 'float'>

print("String (str) - Represents text:")
name = "Alice"
print(name)  # Output: Alice
print(type(name))  # Output: <class 'str'>

print("Boolean (bool) - Represents True or False values:")
is_valid = True
print(is_valid)  # Output: True
print(type(is_valid))  # Output: <class 'bool'>

print("NoneType (None) - Represents a null value:")
result = None
print(result)  # Output: None
print(type(result))  # Output: <class 'NoneType'>

print("List (list) - Ordered, mutable, and allows duplicate elements:")
fruits = ["apple", "banana", "cherry"]
fruits.append("date")
print(fruits)  # Output: ['apple', 'banana', 'cherry', 'date']
print(type(fruits))  # Output: <class 'list'>

print("Tuple (tuple) - Ordered, immutable, and allows duplicate elements:")
coordinates = (10.0, 20.0)
print(coordinates)  # Output: (10.0, 20.0)
print(type(coordinates))  # Output: <class 'tuple'>

print("Set (set) - Unordered, mutable, and does not allow duplicate elements:")
unique_numbers = {1, 2, 3, 3, 4}
print(unique_numbers)  # Output: {1, 2, 3, 4}
print(type(unique_numbers))  # Output: <class 'set'>

print("Dictionary (dict) - Unordered, mutable, and stores key-value pairs:")
person = {"name": "Alice", "age": 25}
person["job"] = "Engineer"
print(person)  # Output: {'name': 'Alice', 'age': 25, 'job': 'Engineer'}
print(type(person))  # Output: <class 'dict'>

print("List of Lists - a list can contain other lists, creating a matrix-like structure:")
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matrix[1])  # Output: [4, 5, 6]

print("Dictionary of Lists - A Dictionary can store lists as values:")
student_scores = {
    "Alice": [85, 90, 95],
    "Bob": [75, 80, 85]
}
print(student_scores["Alice"])  # Output: [85, 90, 95]

print("List of Dictionaries - A List can store Dictionaries:")
employees = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 30}
]
print(employees[0]["name"])  # Output: Alice

