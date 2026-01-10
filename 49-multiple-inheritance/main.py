# ============================================
# CHAPTER 49: MULTIPLE INHERITANCE
# ============================================
# Multiple Inheritance = When a class inherits from MORE THAN ONE parent class
#                        Allows combining features from multiple classes
#
# Syntax: class Child(Parent1, Parent2, Parent3):
#
# Key Concepts:
# - Child class inherits attributes/methods from ALL parent classes
# - Can access features from multiple parents
# - Method Resolution Order (MRO) determines which parent method is used
# - Use super() to call parent class methods
# - Diamond problem: When multiple parents share a common ancestor
#
# Benefits:
# - Combine functionality from multiple sources
# - Code reuse from multiple classes
# - Model complex real-world relationships
#
# Cautions:
# - Can become complex and hard to maintain
# - Name conflicts if parents have same method names
# - Use composition (has-a) instead when possible

# =============================================
# EXAMPLE 1: SIMPLE MULTIPLE INHERITANCE
# =============================================

class Animal:
    """Base class for all animals."""
    def __init__(self, name):
        self.name = name
        self.is_alive = True
    
    def eat(self):
        return f"{self.name} is eating."

class Flyer:
    """Mixin class for flying ability."""
    def fly(self):
        return f"{self.name} is flying!"

class Swimmer:
    """Mixin class for swimming ability."""
    def swim(self):
        return f"{self.name} is swimming!"

# =============================================
# MULTIPLE INHERITANCE: Duck inherits from THREE classes
# =============================================
class Duck(Animal, Flyer, Swimmer):
    """
    Duck inherits from:
    - Animal (base attributes like name, is_alive, eat)
    - Flyer (flying ability)
    - Swimmer (swimming ability)
    """
    pass  # Inherits everything from all three parents

# =============================================
# MULTIPLE INHERITANCE: Fish inherits from TWO classes
# =============================================
class Fish(Animal, Swimmer):
    """
    Fish inherits from:
    - Animal (base attributes)
    - Swimmer (swimming ability)
    Note: Fish does NOT inherit from Flyer
    """
    pass

# =============================================
# SINGLE INHERITANCE: Bird inherits from TWO classes
# =============================================
class Bird(Animal, Flyer):
    """
    Bird inherits from:
    - Animal (base attributes)
    - Flyer (flying ability)
    Note: Bird does NOT inherit from Swimmer
    """
    pass

# =============================================
# CREATE INSTANCES
# =============================================
# Duck can do everything (eat, fly, swim)
duck = Duck("Donald")

# Fish can eat and swim (no flying)
fish = Fish("Nemo")

# Bird can eat and fly (no swimming)
bird = Bird("Tweety")

# =============================================
# DEMONSTRATE MULTIPLE INHERITANCE
# =============================================
print("=== Duck (inherits from Animal, Flyer, Swimmer) ===")
print(duck.eat())   # From Animal class
print(duck.fly())   # From Flyer class
print(duck.swim())  # From Swimmer class

print("\n=== Fish (inherits from Animal, Swimmer) ===")
print(fish.eat())   # From Animal class
print(fish.swim())  # From Swimmer class
# print(fish.fly())  # ERROR! Fish doesn't inherit from Flyer

print("\n=== Bird (inherits from Animal, Flyer) ===")
print(bird.eat())   # From Animal class
print(bird.fly())   # From Flyer class
# print(bird.swim()) # ERROR! Bird doesn't inherit from Swimmer

# =============================================
# METHOD RESOLUTION ORDER (MRO)
# =============================================
# Python uses C3 Linearization to determine method lookup order
# When child and parents have same method name, Python checks in this order:
# 1. Child class
# 2. First parent (left to right)
# 3. Second parent
# 4. And so on...

print("\n=== Method Resolution Order ===")
print("Duck MRO:", Duck.__mro__)
# Output shows order: Duck -> Animal -> Flyer -> Swimmer -> object

# =============================================
# EXAMPLE 2: METHOD OVERRIDE WITH MULTIPLE INHERITANCE
# =============================================

class FlyingFish(Animal, Flyer, Swimmer):
    """
    FlyingFish can fly AND swim.
    Overrides eat() method with custom behavior.
    """
    def eat(self):
        # Override parent's eat() method
        return f"{self.name} catches fish while gliding!"

flying_fish = FlyingFish("Exocoetus")

print("\n=== Flying Fish (Custom behavior) ===")
print(flying_fish.eat())   # Uses overridden method
print(flying_fish.fly())   # From Flyer
print(flying_fish.swim())  # From Swimmer

# =============================================
# KEY TAKEAWAYS
# =============================================
# 1. Multiple inheritance allows inheriting from multiple classes
# 2. Syntax: class Child(Parent1, Parent2, ...)
# 3. Child inherits ALL attributes/methods from ALL parents
# 4. MRO determines which method is called when conflicts exist
# 5. Use mixin classes (like Flyer, Swimmer) for specific abilities
# 6. Child can override any inherited method
# 7. Keep inheritance hierarchies simple when possible
