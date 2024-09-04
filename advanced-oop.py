# CLASSES AND OBJECTS
print("\nCLASSES AND OBJECTS EXAMPLE:\n")
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def bark(self):
        return f"{self.name} says Woof!"

# Creating instances
buddy = Dog("Buddy", 5)
max = Dog("Max", 3)

print(buddy.name)  # Output: Buddy
print(max.bark())  # Output: Max says Woof!

# INHERITANCE
print("\nINHERITANCE EXAMPLE:\n")
class Animal:
    def __init__(self, species):
        self.species = species
    
    def make_sound(self):
        pass

class Cat(Animal):
    def __init__(self, name):
        super().__init__("Cat")
        self.name = name
    
    def make_sound(self):
        return f"{self.name} says Meow!"

whiskers = Cat("Whiskers")
print(whiskers.species)  # Output: Cat
print(whiskers.make_sound())  # Output: Whiskers says Meow!

# POLYMORPHISM
print("\nPOLYMORPHISM EXAMPLE:\n")
class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

class Duck(Animal):
    def speak(self):
        return "Quack!"

def animal_sound(animal):
    print(animal.speak())

# Creating objects
dog = Dog()
cat = Cat()
duck = Duck()

# Polymorphic behavior
animal_sound(dog)   # Output: Woof!
animal_sound(cat)   # Output: Meow!
animal_sound(duck)  # Output: Quack!

# CLASS AND STATIC METHODS
print("\nCLASS AND STATIC METHODS EXAMPLE:\n")
class MathOperations:
    @staticmethod
    def add(x, y):
        return x + y
    
    @classmethod
    def multiply(cls, x, y):
        return cls.add(x, 0) * y  # Using the static method

print(MathOperations.add(3, 4))  # Output: 7
print(MathOperations.multiply(3, 4))  # Output: 12
print('''
NOTE: Class methods are more flexible and can interact with the 
      class itself, while static methods are more like regular functions that 
      are namespaced within the class.
''')

# PROPERTIES
print("\nPROPERTIES EXAMPLE:\n")
class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius
    
    @property
    def celsius(self):
        return self._celsius
    
    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("Temperature below absolute zero is not possible")
        self._celsius = value
    
    @property
    def fahrenheit(self):
        return (self._celsius * 9/5) + 32

temp = Temperature(25)
print(temp.celsius)  # Output: 25
print(temp.fahrenheit)  # Output: 77.0
temp.celsius = 30
print(temp.fahrenheit)  # Output: 86.0
print('''
NOTE: Using @property and @<func-name>.setter allows you to create attributes 
      that behave like regular attributes but have additional logic behind 
      them, providing a clean and Pythonic way to implement getters and 
      setters.

      @property decorator defines a getter method that allows you to access the 
      method as if it were an attribute, without using parentheses. It can also
      compute or retrieve a value dynamically when the attribute is accessed.

      @<method-name>.setter decorator defines a setter method that allows you to 
      set the value of a property using assignment syntax. You can also validate
      and/or process the value before setting it.
''')

# MAGIC METHODS
print("MAGIC METHODS EXAMPLE:")
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    
    def __str__(self):
        return f"Vector({self.x}, {self.y})"

v1 = Vector(2, 3)
v2 = Vector(3, 4)
v3 = v1 + v2
print(v3)  # Output: Vector(5, 7)
print('''
NOTE: Magic methods (also called dunder methods) in Python are special methods 
      that have double underscores before and after their name. They are used 
      to define how objects of a class behave in various situations.

      Predefined magic methods allow you to define how instances of your classes 
      should behave in various Python operations, enabling you to make your objects 
      behave like built-in types or integrate seamlessly with Python's syntax.

      You can define arbitrarily named magic methods as long as they adhere to the 
      __ before and after naming convention. This convention is used to distinguish 
      special methods from regular attributes and methods. Such arbitrarily named magic
      methods do not have any predefined behaviors and so their usefulness is moot.
''')

# ABSTRACT BASE CLASSES
print("\nABSTRACT BASE CLASSES EXAMPLE:\n")
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        return "Woof!"

class Cat(Animal):
    def make_sound(self):
        return "Meow!"

dog = Dog()
cat = Cat()
print(dog.make_sound())  # Output: Woof!
print(cat.make_sound())  # Output: Meow!
print('''
NOTE: @abstractmethod decorator helps ensure that subclasses adhere to the 
      defined interface and provide necessary functionality. 

      An ABC (Abstract Base Class) cannot be instantiated directly. This prevents 
      the creation of incomplete objects that lack essential methods.

      ABC's cannot be instantiated directly. Its primary purpose is to define a 
      common interface for related classes.

      A method marked with @abstractmethod must be implemented by any concrete 
      subclass of the ABC. If a subclass doesn't implement an abstract method, 
      it will raise an error.
''')

