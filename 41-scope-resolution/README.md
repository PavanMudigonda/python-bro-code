[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/PavanMudigondaTR/python-bro-code/blob/main/41-scope-resolution/41-scope-resolution.ipynb) [![Kaggle](https://kaggle.com/static/images/open-in-kaggle.svg)](https://kaggle.com/kernels/welcome?src=https://raw.githubusercontent.com/PavanMudigondaTR/python-bro-code/main/41-scope-resolution/41-scope-resolution.ipynb)

# 🔍 Scope Resolution

## 📺 Video Tutorial

**What is Python scope resolution? 🔬** (8:05)

[![Watch on YouTube](https://img.shields.io/badge/Watch-YouTube-red?style=for-the-badge&logo=youtube)](https://youtu.be/XN83IECAscM)

## What You'll Learn

In this chapter, you'll master Python's scope resolution - understanding where variables are accessible and the order Python searches for them. You'll learn the LEGB rule (Local, Enclosing, Global, Built-in), understand variable shadowing, use the `global` and `nonlocal` keywords, and write code that properly manages variable scope across functions and modules.

## Learning Objectives

- Understand the four levels of variable scope in Python
- Apply the LEGB rule to predict variable resolution
- Distinguish between local, enclosing, global, and built-in scopes
- Use `global` keyword to modify global variables from functions
- Use `nonlocal` keyword to modify enclosing function variables
- Avoid common scope-related bugs and write cleaner code

## Concept Explanation

### What is Variable Scope?

**Scope** determines where a variable is visible and accessible in your code. Not all variables are available everywhere - scope controls access.

```python
x = 10  # Global scope - accessible everywhere

def my_function():
    y = 20  # Local scope - only accessible inside function
    print(x)  # Can access global x
    print(y)  # Can access local y

my_function()
print(x)  # Works - x is global
print(y)  # Error! y doesn't exist here
```

### The LEGB Rule

Python searches for variables in this order: **L**ocal → **E**nclosing → **G**lobal → **B**uilt-in

```
B (Built-in)    ← Python's built-in names (print, len, etc.)
    ↑
G (Global)      ← Variables at module level
    ↑
E (Enclosing)   ← Variables in enclosing functions
    ↑
L (Local)       ← Variables inside current function
```

**Search Process:**
1. Look in **Local** scope first
2. If not found, look in **Enclosing** scope
3. If not found, look in **Global** scope  
4. If not found, look in **Built-in** scope
5. If still not found → `NameError`

### 1. Local Scope (L)

Variables defined inside a function are **local** to that function:

```python
def my_function():
    x = 10  # Local variable
    print(x)  # 10

my_function()
print(x)  # NameError: x is not defined
```

**Key Points:**
- Local variables only exist during function execution
- Each function call creates a new local scope
- Local variables are destroyed when function returns

### 2. Enclosing Scope (E)

For **nested functions**, the outer function's scope is the enclosing scope:

```python
def outer():
    x = 10  # Enclosing scope for inner()
    
    def inner():
        print(x)  # Accesses x from enclosing scope
    
    inner()  # Prints 10

outer()
```

### 3. Global Scope (G)

Variables defined at the module level (outside all functions) are **global**:

```python
x = 100  # Global variable

def func1():
    print(x)  # Accesses global x

def func2():
    print(x)  # Also accesses same global x

func1()  # 100
func2()  # 100
```

### 4. Built-in Scope (B)

Python's built-in names (functions like `print()`, `len()`, `type()`):

```python
# Built-in functions available everywhere
print("Hello")  # 'print' is in built-in scope
result = len([1, 2, 3])  # 'len' is in built-in scope
```

### Variable Shadowing

Inner scopes can "shadow" (hide) outer scope variables:

```python
x = 100  # Global

def my_function():
    x = 10  # Local - shadows global x
    print(x)  # 10 (local x)

my_function()  # Prints 10
print(x)  # Prints 100 (global x unchanged)
```

### The `global` Keyword

Use `global` to modify global variables from inside a function:

**Without `global` (Creates local variable):**
```python
x = 100

def modify():
    x = 200  # Creates NEW local variable
    print(f"Inside: {x}")  # 200

modify()
print(f"Outside: {x}")  # 100 (global unchanged)
```

**With `global` (Modifies global variable):**
```python
x = 100

def modify():
    global x  # Declare we're using global x
    x = 200   # Modifies the global x
    print(f"Inside: {x}")  # 200

modify()
print(f"Outside: {x}")  # 200 (global changed)
```

### The `nonlocal` Keyword

Use `nonlocal` to modify variables in enclosing function scope:

```python
def outer():
    x = 10
    
    def inner():
        nonlocal x  # Refers to outer's x
        x = 20      # Modifies outer's x
        print(f"Inner: {x}")  # 20
    
    inner()
    print(f"Outer: {x}")  # 20 (modified by inner)

outer()
```

### Scope Best Practices

#### 1. **Minimize Global Variables**
```python
# Bad - global variables
count = 0
total = 0

def add_value(x):
    global count, total
    count += 1
    total += x

# Good - pass and return values
def add_value(count, total, x):
    count += 1
    total += x
    return count, total

count, total = add_value(count, total, 5)
```

#### 2. **Use Function Parameters**
```python
# Bad - relies on global
x = 10

def double():
    return x * 2

# Good - explicit parameter
def double(x):
    return x * 2

result = double(10)
```

#### 3. **Return Values Instead of Modifying Globals**
```python
# Bad
result = 0

def calculate(x):
    global result
    result = x * 2

# Good
def calculate(x):
    return x * 2

result = calculate(10)
```

### Understanding Scope with Examples

#### Example: Independent Local Scopes
```python
def func1():
    x = 10  # Local to func1
    print(f"func1: {x}")

def func2():
    x = 20  # Different local variable (separate scope)
    print(f"func2: {x}")

func1()  # func1: 10
func2()  # func2: 20
# Each function has its own x
```

#### Example: LEGB in Action
```python
x = "global"  # Global scope

def outer():
    x = "enclosing"  # Enclosing scope
    
    def inner():
        x = "local"  # Local scope
        print(x)  # Prints "local" (found in L)
    
    inner()
    print(x)  # Prints "enclosing" (local to outer)

outer()
print(x)  # Prints "global"
```

## Examples

### Example 1: Basic Local vs Global
```python
x = 100  # Global variable

def func1():
    """Function with its own local x."""
    x = 10  # Local variable
    print(f"Inside func1, x = {x}")

def func2():
    """Function with different local x."""
    x = 20  # Different local variable
    print(f"Inside func2, x = {x}")

func1()  # Inside func1, x = 10
func2()  # Inside func2, x = 20
print(f"Global x = {x}")  # Global x = 100
```

### Example 2: Accessing Global Variables
```python
total = 0  # Global variable

def add_to_total(value):
    """This only reads global total, doesn't modify it."""
    print(f"Current total: {total}")
    print(f"Adding {value}")
    # Note: We're reading total, not modifying it

add_to_total(10)  # Current total: 0, Adding 10
print(f"Total is still: {total}")  # 0
```

### Example 3: Modifying Global with `global`
```python
counter = 0  # Global counter

def increment():
    """Increment the global counter."""
    global counter  # Declare we're using global variable
    counter += 1
    print(f"Counter: {counter}")

increment()  # Counter: 1
increment()  # Counter: 2
increment()  # Counter: 3
print(f"Final counter: {counter}")  # Final counter: 3
```

### Example 4: Enclosing Scope with Nested Functions
```python
def outer(x):
    """Outer function with enclosing scope."""
    
    def inner():
        """Inner function accessing enclosing scope."""
        print(f"Inner can see x from outer: {x}")
    
    print(f"Outer x: {x}")
    inner()

outer(42)
# Outer x: 42
# Inner can see x from outer: 42
```

### Example 5: Using `nonlocal` for Closures
```python
def make_counter():
    """Create a counter function with persistent state."""
    count = 0  # Enclosing scope variable
    
    def counter():
        nonlocal count  # Modify enclosing scope variable
        count += 1
        return count
    
    return counter

# Create two independent counters
counter1 = make_counter()
counter2 = make_counter()

print(counter1())  # 1
print(counter1())  # 2
print(counter1())  # 3

print(counter2())  # 1 (independent counter)
print(counter2())  # 2
```

### Example 6: LEGB Resolution Order
```python
x = "global x"  # Global

def outer():
    x = "outer x"  # Enclosing
    
    def inner():
        x = "inner x"  # Local
        print(f"1. Local: {x}")  # Finds x in Local scope
    
    def inner2():
        # No local x, finds in enclosing
        print(f"2. Enclosing: {x}")  # Finds x in Enclosing scope
    
    inner()
    inner2()

def no_local():
    # No local or enclosing x, finds in global
    print(f"3. Global: {x}")  # Finds x in Global scope

outer()
# 1. Local: inner x
# 2. Enclosing: outer x

no_local()
# 3. Global: global x

print(f"4. Global: {x}")  # global x
```

### Example 7: Shopping Cart with Scope
```python
# Global variables (generally avoid, but for demonstration)
cart_items = []
cart_total = 0.0

def add_item(name, price):
    """Add item to shopping cart."""
    global cart_items, cart_total
    
    cart_items.append({"name": name, "price": price})
    cart_total += price
    
    print(f"Added {name} (${price:.2f})")
    print(f"Total: ${cart_total:.2f}")

def clear_cart():
    """Clear the shopping cart."""
    global cart_items, cart_total
    
    cart_items = []
    cart_total = 0.0
    print("Cart cleared!")

def show_cart():
    """Display cart contents."""
    print("\n=== Shopping Cart ===")
    for item in cart_items:
        print(f"  {item['name']}: ${item['price']:.2f}")
    print(f"Total: ${cart_total:.2f}")
    print("=" * 21)

# Use the cart functions
add_item("Apple", 1.50)
add_item("Banana", 0.75)
add_item("Orange", 2.00)
show_cart()
clear_cart()
show_cart()
```

## Practice Exercises

### Beginner Level

1. **Scope Tester**: Create functions that demonstrate local vs global scope with print statements.

2. **Counter Function**: Build a function that uses `global` to maintain a counter across calls.

3. **Nested Access**: Write nested functions where inner function accesses outer function's variable.

4. **Variable Shadow**: Demonstrate variable shadowing with same-named variables in different scopes.

5. **Built-in Override**: Show what happens when you create a variable with a built-in name.

### Intermediate Level

6. **Closure Factory**: Create a function that returns another function with access to enclosing scope.

7. **State Manager**: Build functions using `nonlocal` to maintain state in nested functions.

8. **Scope Debugger**: Write a function that prints all variables in different scopes.

9. **Bank Account**: Create account functions using scope to protect balance variable.

10. **Configuration System**: Use global variables for app configuration with getter/setter functions.

### Advanced Level

11. **Decorator with State**: Create a decorator that uses closure to maintain state across decorated function calls.

12. **Namespace Manager**: Build a system that manages different namespaces using scope.

13. **Singleton Pattern**: Implement singleton pattern using closure and scope.

14. **Function Factory**: Create a factory function that returns customized functions using scope.

15. **Scope Chain Visualizer**: Build a tool that visualizes the scope chain for complex nested functions.

## Common Mistakes to Avoid

### Mistake 1: Modifying Global Without `global`

**Wrong:**
```python
count = 0

def increment():
    count = count + 1  # UnboundLocalError!
    # Python sees assignment, treats count as local
    # But tries to read it before assignment

increment()
```

**Correct:**
```python
count = 0

def increment():
    global count  # Declare using global count
    count = count + 1

increment()
print(count)  # 1
```

**Why:** Assignment creates local variable. Use `global` to modify global.

### Mistake 2: Assuming Local Changes Affect Global

**Wrong:**
```python
total = 100

def modify_total():
    total = 200  # Creates local variable, doesn't affect global

modify_total()
print(total)  # Still 100!
```

**Correct:**
```python
# Option 1: Use global
total = 100

def modify_total():
    global total
    total = 200

modify_total()
print(total)  # 200

# Option 2: Return value (better)
def modify_total(value):
    return value * 2

total = modify_total(total)
print(total)  # 200
```

**Why:** Local assignment doesn't affect global. Use `global` or return values.

### Mistake 3: Wrong Use of `nonlocal`

**Wrong:**
```python
x = 10

def func():
    nonlocal x  # SyntaxError: no binding for nonlocal 'x'
    x = 20

# nonlocal only works in nested functions!
```

**Correct:**
```python
def outer():
    x = 10
    
    def inner():
        nonlocal x  # Now it works - x is in enclosing scope
        x = 20
    
    inner()
    print(x)  # 20

outer()
```

**Why:** `nonlocal` only works for enclosing function scopes, not global.

### Mistake 4: Overusing Global Variables

**Wrong:**
```python
# Bad - too many globals
user_name = ""
user_age = 0
user_email = ""

def set_user_info(name, age, email):
    global user_name, user_age, user_email
    user_name = name
    user_age = age
    user_email = email
```

**Correct:**
```python
# Good - use parameters and returns
def create_user(name, age, email):
    return {
        "name": name,
        "age": age,
        "email": email
    }

user = create_user("Alice", 25, "alice@example.com")
```

**Why:** Global variables make code harder to test and maintain. Prefer parameters and return values.

## Real-World Applications

### 1. **Configuration Management**
```python
DEBUG = False  # Global config
DATABASE_URL = "localhost:5432"

def setup_app():
    global DEBUG
    if environment == "development":
        DEBUG = True
```

### 2. **Closures for Decorators**
```python
def cache_result(func):
    cached = {}  # Enclosing scope
    
    def wrapper(*args):
        if args not in cached:
            cached[args] = func(*args)
        return cached[args]
    
    return wrapper
```

### 3. **State Machines**
```python
def create_state_machine():
    state = "idle"  # Enclosing scope
    
    def transition(new_state):
        nonlocal state
        state = new_state
    
    def get_state():
        return state
    
    return transition, get_state
```

### 4. **Singleton Pattern**
```python
_instance = None  # Global

def get_instance():
    global _instance
    if _instance is None:
        _instance = DatabaseConnection()
    return _instance
```

## Challenge Projects

### 1. **Function Call Tracker**
Build a system that tracks function calls using scope.

**Requirements:**
- Track number of calls per function
- Track total execution time
- Use closures and decorators
- Report statistics
- Reset functionality

### 2. **Namespace Manager**
Create a namespace management system.

**Requirements:**
- Multiple isolated namespaces
- Variable get/set operations
- Scope chain visualization
- Import/export variables
- Namespace inheritance

### 3. **State Machine Framework**
Build a state machine using scope management.

**Requirements:**
- State transitions using nonlocal
- State history tracking
- Rollback functionality
- Event handlers
- State validation

### 4. **Advanced Counter System**
Create various types of counters using scope.

**Requirements:**
- Simple counter with increment/decrement
- Rate-limited counter
- Bounded counter (min/max)
- Multi-counter manager
- Thread-safe version (bonus)

### 5. **Configuration System**
Build a hierarchical configuration system.

**Requirements:**
- Global defaults
- Environment-specific configs
- Override mechanism
- Config validation
- Save/load from files
- Type checking

---

## Navigation

- **Previous:** [39. Modules](../39-modules/README.md)
- **Next:** [41. If Name Main](../41-if-name-main/README.md)
- **[Back to Main README](../README.md)**

## 🎓 Key Takeaways from Video

1. Variables store data values that can be reused
2. Define functions using the def keyword
3. Follow along with the video for hands-on practice

> 💡 *These points cover the main concepts from the video tutorial to help reinforce your learning.*
