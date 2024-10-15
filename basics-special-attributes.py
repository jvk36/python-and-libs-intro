# ******** __name__ and __main__ attributes USAGE example *********************
# __name__: This is a built-in attribute in Python. When a Python file is run 
#   directly, the __name__ attribute is set to "__main__". However, if the file 
#   is imported as a module into another script, __name__ is set to the module's 
#   name.
# __main__: This refers to the top-level environment where a script is executed.
# *****************************************************************************
def greet():
    print("Hello from the greet function!")

if __name__ == "__main__":
    print("This script is being run directly.")
    greet()
else:
    print("This script has been imported.")

# ******** __init__ and __str__ attributes USAGE example **********************
# __init__: This is a special method that is automatically called when a new 
#   instance of a class is created. It's often used to initialize the object's 
#   attributes.
# __str__: This method defines the string representation of the object when 
#   print() is called on it or str() is used.
# ***************************************************************************** 
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return f"Person(Name: {self.name}, Age: {self.age})"

# Creating an instance of Person
p = Person("Alice", 30)
print(p)  # Will automatically call __str__ method

# ******** __repr__ vs __str__ attributes USAGE example **********************
# __repr__: Meant to provide a string that could recreate the object or give 
#   a detailed representation, useful for developers.
# __str__: Provides a more readable and user-friendly string representation of 
#   an object.
# ***************************************************************************** 
class Car:
    def __init__(self, model, year):
        self.model = model
        self.year = year
    
    def __repr__(self):
        return f"Car(model='{self.model}', year={self.year})"
    
    def __str__(self):
        return f"{self.model} ({self.year})"

car = Car("Toyota Camry", 2020)
print(repr(car))  # Calls __repr__
print(str(car))   # Calls __str__

# ******** __len__, __getitem__, and __setitem__ attributes USAGE example *****
# __len__: Returns the length of the container.
# __getitem__: Allows access to elements using the [] notation.
# __setitem__: Allows setting elements using the [] notation.
# ***************************************************************************** 
class CustomList:
    def __init__(self, items):
        self.items = items
    
    def __len__(self):
        return len(self.items)
    
    def __getitem__(self, index):
        return self.items[index]
    
    def __setitem__(self, index, value):
        self.items[index] = value

my_list = CustomList([1, 2, 3])
print(len(my_list))  # Calls __len__
print(my_list[1])    # Calls __getitem__
my_list[1] = 10      # Calls __setitem__
print(my_list[1])    # Calls __getitem__ again

# ******** __call__ attribute USAGE example ***********************************
# __call__: This allows an instance of a class to be called as if it were 
#   a function.
# ***************************************************************************** 
class Multiplier:
    def __init__(self, factor):
        self.factor = factor
    
    def __call__(self, value):
        return value * self.factor

double = Multiplier(2)
print(double(5))  # Calls __call__ method

