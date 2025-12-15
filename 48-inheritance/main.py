# Inheritance  = Allows a class to inherit attributes and methods from another class.
#            Helps to reuse code and establish a relationship between classes.
#          The class that is inherited from is called the "parent" or "base" class.
#          The class that inherits is called the "child" or "derived" class.
# Example:

# Parent class
class Animal:
    # lets start a constructor
    def __init__(self, name):
        self.name = name
        self.is_alive = True
    def eat(self):
        return f"{self.name} is eating."
    def sleep(self):
        return f"{self.name} is sleeping."
    
class Dog(Animal):  # Dog inherits from Animal
    pass

class Cat(Animal):  # Cat inherits from Animal
    pass

class Mouse(Animal):  # Mouse inherits from Animal
    pass

dog = Dog("Scooby")
cat = Cat("Garfield")
mouse = Mouse("Jerry")
print(dog.name)  # Output: Scooby
print(dog.is_alive) # Output: True
print(dog.eat())   # Output: Scooby is eating.
print(cat.sleep()) # Output: Garfield is sleeping.
    