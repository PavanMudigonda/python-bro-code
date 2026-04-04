# 🧬 Inheritance

## 🚀 Open Notebook

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/PavanMudigonda/python-bro-code/blob/main/49-inheritance/49-inheritance.ipynb) [![Open In Kaggle](https://img.shields.io/badge/Open%20in-Kaggle-20BEFF?style=flat&logo=kaggle)](https://kaggle.com/kernels/welcome?src=https://github.com/PavanMudigonda/python-bro-code/blob/main/49-inheritance/49-inheritance.ipynb)



## 📺 Video Tutorial

[![Watch on YouTube](https://img.shields.io/badge/Watch-YouTube-red?style=for-the-badge&logo=youtube)](https://youtu.be/u1be7Vele5o)

**Python INHERITANCE in 6 minutes! 👨‍👦‍👦** (6:40)

## What You'll Learn

In this chapter, you'll discover inheritance - one of the four pillars of Object-Oriented Programming. You'll learn how to create parent-child class relationships, reuse code efficiently, extend functionality through method overriding, use the `super()` function to access parent methods, and understand when inheritance is the right design choice.

## Learning Objectives

- Create parent (base) classes and child (derived) classes
- Inherit attributes and methods from parent classes
- Override parent methods in child classes while maintaining base functionality
- Use `super()` to call parent class methods
- Understand the "is-a" relationship in inheritance
- Implement multi-level inheritance hierarchies

## Concept Explanation

### What is Inheritance?

**Inheritance** allows a class to acquire the attributes and methods of another class.

**Real-world analogy:**  
You inherit traits from your parents (eye color, height), but you also have your own unique traits.

```python
# Parent class (base class)
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        print(f"{self.name} makes a sound")

# Child class (derived class) inherits from Animal
class Dog(Animal):
    pass  # Inherits everything from Animal

# Dog automatically has __init__ and speak
dog = Dog("Buddy")
dog.speak()  # Buddy makes a sound
```

### Why Use Inheritance?

**Benefits:**
1. **Code Reuse** - Write common code once in parent
2. **Organization** - Group related classes
3. **Extensibility** - Add features without modifying parent
4. **Maintainability** - Fix bugs in one place

### Inheritance Syntax

```python
class ParentClass:
    # Parent attributes and methods
    pass

class ChildClass(ParentClass):  # Inherit from ParentClass
    # Child attributes and methods
    pass
```

### The "is-a" Relationship

Use inheritance when child **"is a"** type of parent:

✅ Good examples:
- Dog **is a** Animal
- Circle **is a** Shape
- Manager **is an** Employee

❌ Bad examples:
- Car **has an** Engine (composition, not inheritance)
- House **has a** Door (composition, not inheritance)

### Inheriting Attributes and Methods

**Child classes automatically get all parent attributes and methods:**

```python
class Vehicle:
    def __init__(self, brand):
        self.brand = brand
    
    def start(self):
        print(f"{self.brand} is starting...")

class Car(Vehicle):
    pass  # Inherits brand and start()

car = Car("Toyota")
print(car.brand)  # Toyota
car.start()       # Toyota is starting...
```

### Adding Child-Specific Features

**Child can have additional attributes/methods:**

```python
class Animal:
    def __init__(self, name):
        self.name = name
    
    def eat(self):
        print(f"{self.name} is eating")

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  # Call parent __init__
        self.breed = breed      # Add child attribute
    
    def bark(self):  # Child-specific method
        print(f"{self.name} says Woof!")

dog = Dog("Max", "Golden Retriever")
dog.eat()   # Inherited method
dog.bark()  # Dog-specific method
```

### Method Overriding

**Child can provide its own version of parent methods:**

```python
class Animal:
    def speak(self):
        print("Some generic sound")

class Cat(Animal):
    def speak(self):  # Override parent method
        print("Meow!")

class Dog(Animal):
    def speak(self):  # Override parent method
        print("Woof!")

cat = Cat()
dog = Dog()

cat.speak()  # Meow! (overridden)
dog.speak()  # Woof! (overridden)
```

### Using super()

**`super()` calls the parent class method:**

```python
class Animal:
    def __init__(self, name):
        self.name = name
        print("Animal initialized")

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  # Call parent __init__
        self.breed = breed
        print("Dog initialized")

dog = Dog("Buddy", "Labrador")
# Output:
# Animal initialized
# Dog initialized
```

### Multi-Level Inheritance

**Classes can form inheritance chains:**

```python
class Organism:
    def __init__(self):
        self.alive = True

class Animal(Organism):
    def __init__(self):
        super().__init__()
        self.can_move = True

class Mammal(Animal):
    def __init__(self):
        super().__init__()
        self.warm_blooded = True

class Dog(Mammal):
    def __init__(self):
        super().__init__()
        self.species = "Canis familiaris"

dog = Dog()
print(dog.alive)         # True (from Organism)
print(dog.can_move)      # True (from Animal)
print(dog.warm_blooded)  # True (from Mammal)
print(dog.species)       # Canis familiaris (from Dog)
```

## Examples

### Example 1: Basic Animal Inheritance

```python
class Animal:
    """Base animal class."""
    
    def __init__(self, name):
        self.name = name
        self.is_alive = True
    
    def eat(self):
        print(f"{self.name} is eating")
    
    def sleep(self):
        print(f"{self.name} is sleeping")

class Dog(Animal):
    """Dog inherits from Animal."""
    pass

class Cat(Animal):
    """Cat inherits from Animal."""
    pass

class Mouse(Animal):
    """Mouse inherits from Animal."""
    pass

# All inherit name, is_alive, eat(), sleep()
dog = Dog("Scooby")
cat = Cat("Garfield")
mouse = Mouse("Mickey")

dog.eat()    # Scooby is eating
cat.sleep()  # Garfield is sleeping
print(f"{mouse.name} alive? {mouse.is_alive}")  # Mickey alive? True
```

### Example 2: Vehicle Hierarchy

```python
class Vehicle:
    """Base vehicle class."""
    
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.is_running = False
    
    def start(self):
        """Start the vehicle."""
        if not self.is_running:
            self.is_running = True
            print(f"{self.brand} {self.model} started")
        else:
            print("Already running")
    
    def stop(self):
        """Stop the vehicle."""
        if self.is_running:
            self.is_running = False
            print(f"{self.brand} {self.model} stopped")
        else:
            print("Already stopped")
    
    def info(self):
        """Vehicle information."""
        return f"{self.year} {self.brand} {self.model}"

class Car(Vehicle):
    """Car class inherits from Vehicle."""
    
    def __init__(self, brand, model, year, num_doors):
        super().__init__(brand, model, year)
        self.num_doors = num_doors
    
    def info(self):
        """Override to add door count."""
        return f"{super().info()} ({self.num_doors} doors)"

class Motorcycle(Vehicle):
    """Motorcycle class inherits from Vehicle."""
    
    def __init__(self, brand, model, year, engine_cc):
        super().__init__(brand, model, year)
        self.engine_cc = engine_cc
    
    def wheelie(self):
        """Motorcycle-specific method."""
        if self.is_running:
            print(f"{self.brand} {self.model} does a wheelie!")
        else:
            print("Start the motorcycle first!")

# Create vehicles
car = Car("Toyota", "Camry", 2023, 4)
motorcycle = Motorcycle("Harley", "Sportster", 2022, 1200)

print(car.info())         # 2023 Toyota Camry (4 doors)
print(motorcycle.info())  # 2022 Harley Sportster

car.start()              # Toyota Camry started
motorcycle.start()       # Harley Sportster started
motorcycle.wheelie()     # Harley Sportster does a wheelie!
```

### Example 3: Employee Management System

```python
class Employee:
    """Base employee class."""
    
    def __init__(self, name, employee_id, salary):
        self.name = name
        self.employee_id = employee_id
        self.salary = salary
    
    def get_info(self):
        """Employee information."""
        return f"ID: {self.employee_id} | {self.name} | ${self.salary:,}"
    
    def give_raise(self, amount):
        """Increase salary."""
        self.salary += amount
        print(f"{self.name} received ${amount:,} raise")

class Manager(Employee):
    """Manager inherits from Employee."""
    
    def __init__(self, name, employee_id, salary, department):
        super().__init__(name, employee_id, salary)
        self.department = department
        self.team = []
    
    def add_team_member(self, employee):
        """Add employee to team."""
        self.team.append(employee)
        print(f"{employee.name} added to {self.name}'s team")
    
    def get_info(self):
        """Override to include department and team size."""
        base_info = super().get_info()
        return f"{base_info} | {self.department} Manager | Team: {len(self.team)}"

class Developer(Employee):
    """Developer inherits from Employee."""
    
    def __init__(self, name, employee_id, salary, language):
        super().__init__(name, employee_id, salary)
        self.language = language
        self.projects = []
    
    def add_project(self, project):
        """Assign project."""
        self.projects.append(project)
        print(f"{project} assigned to {self.name}")
    
    def get_info(self):
        """Override to include language and projects."""
        base_info = super().get_info()
        return f"{base_info} | {self.language} Developer | Projects: {len(self.projects)}"

# Create employees
manager = Manager("Alice", "M001", 95000, "Engineering")
dev1 = Developer("Bob", "D001", 80000, "Python")
dev2 = Developer("Charlie", "D002", 75000, "JavaScript")

# Manager manages team
manager.add_team_member(dev1)
manager.add_team_member(dev2)

# Assign projects
dev1.add_project("AI Module")
dev1.add_project("API Gateway")

# Show info
print("\n" + manager.get_info())
print(dev1.get_info())
print(dev2.get_info())
```

### Example 4: Shape Hierarchy

```python
class Shape:
    """Base shape class."""
    
    def __init__(self, color):
        self.color = color
    
    def describe(self):
        """Basic description."""
        return f"A {self.color} shape"

class Circle(Shape):
    """Circle inherits from Shape."""
    
    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius
    
    def area(self):
        """Calculate area."""
        return 3.14159 * self.radius ** 2
    
    def describe(self):
        """Override description."""
        return f"A {self.color} circle with radius {self.radius}"

class Rectangle(Shape):
    """Rectangle inherits from Shape."""
    
    def __init__(self, color, width, height):
        super().__init__(color)
        self.width = width
        self.height = height
    
    def area(self):
        """Calculate area."""
        return self.width * self.height
    
    def describe(self):
        """Override description."""
        return f"A {self.color} rectangle ({self.width}x{self.height})"

class Square(Rectangle):
    """Square inherits from Rectangle."""
    
    def __init__(self, color, side):
        super().__init__(color, side, side)
        self.side = side
    
    def describe(self):
        """Override description."""
        return f"A {self.color} square with side {self.side}"

# Create shapes
circle = Circle("red", 5)
rectangle = Rectangle("blue", 4, 6)
square = Square("green", 4)

shapes = [circle, rectangle, square]

for shape in shapes:
    print(f"{shape.describe()}: Area = {shape.area():.2f}")

# Output:
# A red circle with radius 5: Area = 78.54
# A blue rectangle (4x6): Area = 24.00
# A green square with side 4: Area = 16.00
```

### Example 5: Bank Account Types

```python
class BankAccount:
    """Base bank account class."""
    
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
        self.transactions = []
    
    def deposit(self, amount):
        """Deposit money."""
        if amount > 0:
            self.balance += amount
            self.transactions.append(f"Deposit: +${amount}")
            print(f"Deposited ${amount}. Balance: ${self.balance}")
        else:
            print("Invalid amount")
    
    def withdraw(self, amount):
        """Withdraw money."""
        if amount > self.balance:
            print("Insufficient funds")
        elif amount > 0:
            self.balance -= amount
            self.transactions.append(f"Withdrawal: -${amount}")
            print(f"Withdrew ${amount}. Balance: ${self.balance}")
        else:
            print("Invalid amount")
    
    def get_balance(self):
        """Show balance."""
        return f"{self.owner}'s balance: ${self.balance}"

class SavingsAccount(BankAccount):
    """Savings account with interest."""
    
    def __init__(self, owner, balance=0, interest_rate=0.02):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate
    
    def add_interest(self):
        """Add monthly interest."""
        interest = self.balance * self.interest_rate
        self.balance += interest
        self.transactions.append(f"Interest: +${interest:.2f}")
        print(f"Interest added: ${interest:.2f}. Balance: ${self.balance:.2f}")

class CheckingAccount(BankAccount):
    """Checking account with overdraft."""
    
    def __init__(self, owner, balance=0, overdraft_limit=500):
        super().__init__(owner, balance)
        self.overdraft_limit = overdraft_limit
    
    def withdraw(self, amount):
        """Override to allow overdraft."""
        if amount > self.balance + self.overdraft_limit:
            print(f"Exceeds overdraft limit of ${self.overdraft_limit}")
        elif amount > 0:
            self.balance -= amount
            self.transactions.append(f"Withdrawal: -${amount}")
            print(f"Withdrew ${amount}. Balance: ${self.balance}")
            if self.balance < 0:
                print(f"⚠️ Overdraft: ${abs(self.balance)}")
        else:
            print("Invalid amount")

# Create accounts
savings = SavingsAccount("Alice", 1000, 0.03)
checking = CheckingAccount("Bob", 500, 1000)

print("=== Savings Account ===")
savings.deposit(500)
savings.add_interest()
print(savings.get_balance())

print("\n=== Checking Account ===")
checking.withdraw(700)  # Goes into overdraft
checking.deposit(300)
print(checking.get_balance())
```

### Example 6: User Roles

```python
class User:
    """Base user class."""
    
    def __init__(self, username, email):
        self.username = username
        self.email = email
        self.is_active = True
    
    def login(self):
        """User login."""
        if self.is_active:
            print(f"{self.username} logged in")
            return True
        else:
            print("Account is deactivated")
            return False
    
    def logout(self):
        """User logout."""
        print(f"{self.username} logged out")

class Admin(User):
    """Admin inherits from User."""
    
    def __init__(self, username, email):
        super().__init__(username, email)
        self.permissions = ["read", "write", "delete", "manage_users"]
    
    def delete_user(self, user):
        """Admin can delete users."""
        user.is_active = False
        print(f"Admin {self.username} deactivated {user.username}")
    
    def login(self):
        """Override login with admin message."""
        if super().login():
            print("Admin privileges granted")

class Moderator(User):
    """Moderator inherits from User."""
    
    def __init__(self, username, email):
        super().__init__(username, email)
        self.permissions = ["read", "write", "moderate"]
    
    def moderate_content(self, content_id):
        """Moderate content."""
        print(f"Moderator {self.username} reviewed content #{content_id}")

class RegularUser(User):
    """Regular user inherits from User."""
    
    def __init__(self, username, email):
        super().__init__(username, email)
        self.permissions = ["read", "write"]
    
    def post_content(self, content):
        """Post content."""
        print(f"{self.username} posted: {content}")

# Create users
admin = Admin("admin_alice", "alice@admin.com")
mod = Moderator("mod_bob", "bob@mod.com")
user = RegularUser("user_charlie", "charlie@user.com")

# Test functionality
admin.login()
admin.delete_user(user)

mod.login()
mod.moderate_content(101)

user.login()  # Account is deactivated
```

### Example 7: Pet System with Multiple Levels

```python
class Animal:
    """Base animal class."""
    
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.energy = 100
    
    def eat(self, food):
        """Eat food."""
        self.energy = min(100, self.energy + 20)
        print(f"{self.name} ate {food}. Energy: {self.energy}")
    
    def sleep(self):
        """Sleep to restore energy."""
        self.energy = 100
        print(f"{self.name} is sleeping... Zzz")

class Pet(Animal):
    """Pet inherits from Animal."""
    
    def __init__(self, name, species, owner):
        super().__init__(name, species)
        self.owner = owner
        self.happiness = 50
    
    def play(self):
        """Play with pet."""
        if self.energy >= 20:
            self.energy -= 20
            self.happiness = min(100, self.happiness + 15)
            print(f"{self.name} is playing! Happiness: {self.happiness}")
        else:
            print(f"{self.name} is too tired to play")

class Dog(Pet):
    """Dog inherits from Pet."""
    
    def __init__(self, name, owner, breed):
        super().__init__(name, "Dog", owner)
        self.breed = breed
        self.tricks = []
    
    def bark(self):
        """Dog-specific method."""
        print(f"{self.name}: Woof! Woof!")
    
    def learn_trick(self, trick):
        """Teach dog a trick."""
        self.tricks.append(trick)
        print(f"{self.name} learned {trick}!")
    
    def perform_trick(self):
        """Perform a random trick."""
        if self.tricks:
            import random
            trick = random.choice(self.tricks)
            print(f"{self.name} performs {trick}!")
            self.happiness = min(100, self.happiness + 10)
        else:
            print(f"{self.name} doesn't know any tricks yet")

class Cat(Pet):
    """Cat inherits from Pet."""
    
    def __init__(self, name, owner, color):
        super().__init__(name, "Cat", owner)
        self.color = color
        self.mood = "neutral"
    
    def meow(self):
        """Cat-specific method."""
        print(f"{self.name}: Meow~")
    
    def scratch(self):
        """Cat scratches."""
        self.happiness -= 10
        self.mood = "annoyed"
        print(f"{self.name} scratched the furniture! Mood: {self.mood}")
    
    def pet(self):
        """Pet the cat."""
        if self.mood == "annoyed":
            print(f"{self.name} hisses at you!")
        else:
            self.happiness = min(100, self.happiness + 20)
            self.mood = "happy"
            print(f"{self.name} purrs. Mood: {self.mood}")

# Create pets
dog = Dog("Max", "John", "Golden Retriever")
cat = Cat("Luna", "Sarah", "Gray")

print("=== Dog Activities ===")
dog.bark()
dog.learn_trick("sit")
dog.learn_trick("roll over")
dog.perform_trick()
dog.play()
dog.eat("dog food")

print("\n=== Cat Activities ===")
cat.meow()
cat.pet()
cat.scratch()
cat.pet()
cat.sleep()
```

## Practice Exercises

### Beginner Exercises

1. **Fruit Hierarchy**
   - Create `Fruit` base class with name and color
   - Create `Apple`, `Banana`, `Orange` child classes
   - Each fruit should have a `taste()` method

2. **Phone Types**
   - Create `Phone` base class with brand and model
   - Create `Smartphone` child with apps list
   - Create `FlipPhone` child with simple methods

3. **Book System**
   - Create `Book` base class with title and author
   - Create `Ebook` with file format
   - Create `AudioBook` with narrator

4. **Basic RPG Character**
   - Create `Character` with name and health
   - Create `Warrior`, `Mage`, `Archer` children
   - Each has different attack method

5. **Simple Store Items**
   - Create `Item` base class with name and price
   - Create `Food` with expiration date
   - Create `Clothing` with size

### Intermediate Exercises

1. **Streaming Service**
   - Create `Content` base class
   - `Movie` child with director and runtime
   - `TVShow` child with seasons and episodes
   - Implement watch tracking

2. **Transportation System**
   - `Transport` base class with capacity
   - `Bus`, `Train`, `Airplane` children
   - Each with unique boarding methods
   - Passenger management

3. **File System**
   - `FileSystemItem` base class
   - `File` with size and type
   - `Folder` that can contain files
   - Implement size calculation

4. **Notification System**
   - `Notification` base class
   - `EmailNotification` with subject/body
   - `SMSNotification` with character limit
   - `PushNotification` with icon

5. **Payment Methods**
   - `Payment` base class
   - `CreditCard` with CVV validation
   - `PayPal` with email
   - `Cryptocurrency` with wallet address

### Advanced Exercises

1. **Content Management System**
   - Multi-level inheritance
   - `Content` → `Article` → `BlogPost`/`NewsArticle`
   - Versioning and approval workflow
   - SEO metadata

2. **Game Entity System**
   - `Entity` → `LivingEntity` → `Player`/`Enemy`
   - Inventory system
   - Combat mechanics
   - Status effects

3. **Insurance Policy System**
   - `Policy` base with premium calculation
   - `HealthInsurance`, `AutoInsurance`, `HomeInsurance`
   - Claims processing
   - Risk assessment

4. **Academic System**
   - `Person` → `Student`/`Teacher`
   - `Student` → `Undergraduate`/`Graduate`
   - Course enrollment
   - Grade management

5. **E-commerce Platform**
   - `Product` → `Physical`/`Digital`
   - Shipping calculations
   - Inventory tracking
   - Review system

## Common Mistakes to Avoid

### Mistake 1: Forgetting to Call super().__init__()

❌ **Wrong:**
```python
class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def __init__(self, name, breed):
        # Forgot super().__init__()!
        self.breed = breed

dog = Dog("Max", "Labrador")
print(dog.name)  # ERROR! name not set
```

✅ **Correct:**
```python
class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  # Call parent __init__
        self.breed = breed

dog = Dog("Max", "Labrador")
print(dog.name)  # Max
```

### Mistake 2: Using Inheritance When Composition is Better

❌ **Wrong:**
```python
# Car "is a" Engine? No!
class Engine:
    def start(self):
        print("Engine started")

class Car(Engine):  # Wrong relationship
    pass
```

✅ **Correct:**
```python
# Car "has an" Engine
class Engine:
    def start(self):
        print("Engine started")

class Car:
    def __init__(self):
        self.engine = Engine()  # Composition
    
    def start(self):
        self.engine.start()
```

### Mistake 3: Overriding Without Understanding

❌ **Wrong:**
```python
class Animal:
    def __init__(self, name):
        self.name = name
        self.energy = 100

class Dog(Animal):
    def __init__(self, breed):
        # Completely replaces parent __init__
        # Lost name and energy!
        self.breed = breed
```

✅ **Correct:**
```python
class Animal:
    def __init__(self, name):
        self.name = name
        self.energy = 100

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  # Keep parent functionality
        self.breed = breed      # Add child functionality
```

### Mistake 4: Deep Inheritance Hierarchies

❌ **Wrong:**
```python
# Too many levels - hard to maintain
class A:
    pass
class B(A):
    pass
class C(B):
    pass
class D(C):
    pass
class E(D):  # Way too deep!
    pass
```

✅ **Correct:**
```python
# Keep it shallow (2-3 levels max)
class Animal:
    pass

class Mammal(Animal):
    pass

class Dog(Mammal):
    pass  # That's enough!
```

## Real-World Applications

### 1. **Web Frameworks**
- Django: Model inheritance for database tables
- Flask: Blueprint inheritance for routes
- Abstract base classes for views/controllers

### 2. **Game Development**
- Character hierarchies (Entity → Living → Player/Enemy)
- Item systems (Item → Weapon/Armor/Consumable)
- UI components (Widget → Button/Label/TextBox)

### 3. **GUI Applications**
- Qt/PyQt: Widget inheritance
- Tkinter: Frame and widget hierarchies
- Custom controls extending base widgets

### 4. **Enterprise Systems**
- User role hierarchies
- Document types
- Product catalogs
- Workflow states

## Challenge Projects

### 1. **Zoo Management System**
- Animal hierarchy (Mammal, Bird, Reptile)
- Feeding schedules
- Habitat management
- Visitor interactions

### 2. **Library System**
- Media types (Book, DVD, Magazine)
- Borrowing system
- Different loan periods
- Late fees calculation

### 3. **HR Management**
- Employee types (Full-time, Part-time, Contractor)
- Payroll calculation
- Benefits management
- Performance tracking

### 4. **Social Media Platform**
- Post types (Text, Image, Video, Poll)
- User roles (Regular, Verified, Admin)
- Content moderation
- Engagement tracking

### 5. **Restaurant POS System**
- Menu items (Food, Beverage, Dessert)
- Order types (Dine-in, Takeout, Delivery)
- Payment methods
- Tip calculation

---

## Navigation

← [Previous: 47 - Class Variables](47-class-variables.md) | [Next: 49 - Multiple Inheritance](49-multiple-inheritance.md) →

[↑ Back to Main README](../README.md)