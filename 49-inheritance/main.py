# ============================================
# CHAPTER 48: INHERITANCE
# ============================================
# Inheritance = Allows a class to inherit attributes and methods from another class
#               Helps to reuse code and establish relationships between classes
#
# Terminology:
# - Parent class (Base class/Superclass): The class being inherited FROM
# - Child class (Derived class/Subclass): The class that inherits
#
# Benefits:
# - Code reuse - write common code once in parent class
# - Logical hierarchy - model real-world relationships
# - Easier maintenance - update parent class affects all children
# - Polymorphism - child classes can override parent methods
#
# Syntax: class ChildClass(ParentClass):

# =============================================
# PARENT CLASS (Base Class)
# =============================================
# This is the parent class that child classes will inherit from
class Animal:
    """
    Parent class representing a general animal.
    All child classes will inherit these attributes and methods.
    """
    
    # =============================================
    # CONSTRUCTOR
    # =============================================
    def __init__(self, name):
        """Initialize animal with name and alive status."""
        self.name = name         # Instance variable for animal's name
        self.is_alive = True     # All animals start alive
    
    # =============================================
    # METHODS (Inherited by all child classes)
    # =============================================
    def eat(self):
        """Method that all animals can use."""
        return f"{self.name} is eating."
    
    def sleep(self):
        """Method that all animals can use."""
        return f"{self.name} is sleeping."

# =============================================
# CHILD CLASSES (Inherit from Animal)
# =============================================
# Syntax: class ChildName(ParentName):
# 'pass' means "inherit everything from parent, don't add anything new"

class Dog(Animal):  # Dog inherits from Animal
    """Dog class - inherits all Animal properties and methods."""
    pass  # No additional code needed, inherits everything

class Cat(Animal):  # Cat inherits from Animal
    """Cat class - inherits all Animal properties and methods."""
    pass

class Mouse(Animal):  # Mouse inherits from Animal
    """Mouse class - inherits all Animal properties and methods."""
    pass

# =============================================
# CREATE INSTANCES OF CHILD CLASSES
# =============================================
# Even though Dog, Cat, Mouse have no code,
# they inherit __init__, eat(), and sleep() from Animal
dog = Dog("Scooby")      # Creates Dog with Animal's constructor
cat = Cat("Garfield")    # Creates Cat with Animal's constructor
mouse = Mouse("Jerry")   # Creates Mouse with Animal's constructor

# =============================================
# USE INHERITED ATTRIBUTES AND METHODS
# =============================================
# All these work because they're inherited from Animal class
print(dog.name)       # Output: Scooby (inherited attribute)
print(dog.is_alive)   # Output: True (inherited attribute)
print(dog.eat())      # Output: Scooby is eating. (inherited method)
print(cat.sleep())    # Output: Garfield is sleeping. (inherited method)

# =============================================
# KEY BENEFITS DEMONSTRATED
# =============================================
# - Wrote eat() and sleep() methods only ONCE in Animal
# - All child classes (Dog, Cat, Mouse) can use them
# - If we update Animal, all children get the update
# - This is the power of inheritance - code reuse!
    