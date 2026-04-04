# 🎯 Default Arguments

## 🚀 Open Notebook

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/PavanMudigonda/python-bro-code/blob/main/33-default-arguments/33-default-arguments.ipynb) [![Open In Kaggle](https://img.shields.io/badge/Open%20in-Kaggle-20BEFF?style=flat&logo=kaggle)](https://kaggle.com/kernels/welcome?src=https://github.com/PavanMudigonda/python-bro-code/blob/main/33-default-arguments/33-default-arguments.ipynb)


## 📺 Video Tutorial

[![Watch on YouTube](https://img.shields.io/badge/Watch-YouTube-red?style=for-the-badge&logo=youtube)](https://youtu.be/m2uURZxex3c)

**Python default arguments are awesome! 👍** (6:15)

## What You'll Learn

In this chapter, you'll learn about default arguments - function parameters that have preset values. You'll understand how to make functions more flexible by providing default values, when arguments can be omitted, and the correct order for different parameter types to create user-friendly, versatile functions.

## Learning Objectives

- Define functions with default parameter values
- Understand when and why to use default arguments
- Master the correct order of parameter types (positional, default, keyword, *args/**kwargs)
- Create flexible functions that work with varying numbers of arguments
- Override default values when needed
- Apply best practices for choosing appropriate default values

## Concept Explanation

### What are Default Arguments?

Default arguments are parameters that have a pre-assigned value. When calling a function, if you don't provide a value for that parameter, it uses the default instead.

```python
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

greet("Alice")              # Uses default: "Hello, Alice!"
greet("Bob", "Hi")          # Overrides default: "Hi, Bob!"
greet("Charlie", "Hey")     # Overrides default: "Hey, Charlie!"
```

**Benefits:**
- Makes functions more flexible
- Reduces number of required arguments
- Provides sensible defaults for common cases
- Simplifies function calls

### Syntax for Default Arguments

Default values are assigned in the function definition using `=`:

```python
def function_name(required_param, optional_param=default_value):
    # function body
    pass
```

Example with multiple defaults:

```python
def create_user(username, role="user", active=True, notifications=True):
    print(f"Username: {username}")
    print(f"Role: {role}")
    print(f"Active: {active}")
    print(f"Notifications: {notifications}")

# All defaults used
create_user("alice123")

# Some defaults overridden
create_user("admin_bob", role="admin")

# Multiple defaults overridden
create_user("charlie", role="moderator", notifications=False)
```

### Parameter Order Rules (CRITICAL!)

Python enforces a specific order for different parameter types:

```python
def function(
    positional,          # 1. Required positional (no default)
    default_param=value, # 2. Default arguments (optional)
    *args,               # 3. Variable positional arguments
    **kwargs             # 4. Variable keyword arguments
):
    pass
```

**You CANNOT put a required parameter after a default parameter:**

```python
# WRONG - SyntaxError!
def bad_function(name="Anonymous", age):
    pass

# CORRECT
def good_function(age, name="Anonymous"):
    pass
```

### When to Use Default Arguments

#### 1. **Common Default Values**
When a parameter usually has the same value:

```python
def connect_database(host, port=5432, timeout=30):
    # PostgreSQL default port is 5432
    # 30 seconds is reasonable timeout
    pass

# Most calls use defaults
connect_database("localhost")

# Occasionally override
connect_database("prod-server", port=3306)  # MySQL
```

#### 2. **Optional Configuration**
For optional features or settings:

```python
def send_email(to, subject, body, cc=None, bcc=None, priority="normal"):
    # cc and bcc are optional
    # priority has sensible default
    pass

send_email("user@example.com", "Hello", "Message body")
send_email("user@example.com", "Urgent", "Important!", priority="high")
```

#### 3. **Backward Compatibility**
Adding new parameters without breaking existing code:

```python
# Original function
def process_data(data):
    # process data
    pass

# Enhanced with new optional parameter
def process_data(data, format="json"):
    # Can now handle different formats
    # Old code still works: process_data(my_data)
    pass
```

### Mutable Default Arguments (DANGER ZONE!)

**Never use mutable objects (lists, dicts) as defaults:**

```python
# WRONG - This is a common bug!
def add_item(item, shopping_list=[]):
    shopping_list.append(item)
    return shopping_list

# Unexpected behavior!
list1 = add_item("apple")   # ['apple']
list2 = add_item("banana")  # ['apple', 'banana'] - WRONG!
# The same list is reused!

# CORRECT - Use None and create new list
def add_item(item, shopping_list=None):
    if shopping_list is None:
        shopping_list = []
    shopping_list.append(item)
    return shopping_list

# Now works correctly
list1 = add_item("apple")   # ['apple']
list2 = add_item("banana")  # ['banana'] - CORRECT!
```

**Why?** Default values are created once when the function is defined, not each time it's called. Mutable defaults persist across calls.

### Overriding Default Arguments

You can override defaults in two ways:

#### 1. **Positional (Order Matters)**
```python
def greet(name, title="Mr", greeting="Hello"):
    print(f"{greeting} {title} {name}")

# Override by position
greet("Smith", "Dr")  # Hello Dr Smith
greet("Smith", "Dr", "Good morning")  # Good morning Dr Smith
```

#### 2. **Keyword (Order Doesn't Matter)**
```python
# Skip some defaults, specify others by name
greet("Smith", greeting="Hi")  # Hi Mr Smith
greet("Smith", greeting="Hey", title="Ms")  # Hey Ms Smith
```

### Combining Default Arguments with Keyword Arguments

This combination creates very flexible functions:

```python
def create_profile(username, email, bio="", location="Unknown", 
                   age=None, verified=False):
    profile = {
        "username": username,
        "email": email,
        "bio": bio,
        "location": location,
        "age": age,
        "verified": verified
    }
    return profile

# Minimal call - only required arguments
profile1 = create_profile("alice", "alice@example.com")

# Selective overrides using keyword arguments
profile2 = create_profile(
    "bob",
    "bob@example.com",
    bio="Python developer",
    verified=True
)

# Can skip middle parameters
profile3 = create_profile(
    "charlie",
    "charlie@example.com",
    location="New York",
    age=25
)
```

## Examples

### Example 1: Simple Default Argument
```python
def power(base, exponent=2):
    """
    Raise base to the power of exponent.
    
    Parameters:
        base (float): The base number
        exponent (float): The exponent (default: 2 for square)
    
    Returns:
        float: base raised to exponent
    """
    return base ** exponent

# Use default (square)
print(power(5))      # 25 (5^2)
print(power(3))      # 9 (3^2)

# Override default
print(power(5, 3))   # 125 (5^3)
print(power(2, 10))  # 1024 (2^10)
```

### Example 2: Multiple Default Arguments
```python
def format_price(amount, currency="$", decimal_places=2, show_symbol=True):
    """
    Format a price with currency symbol.
    
    Parameters:
        amount (float): Price amount
        currency (str): Currency symbol (default: $)
        decimal_places (int): Number of decimals (default: 2)
        show_symbol (bool): Whether to show currency symbol (default: True)
    
    Returns:
        str: Formatted price string
    """
    formatted = f"{amount:.{decimal_places}f}"
    
    if show_symbol:
        return f"{currency}{formatted}"
    return formatted

# All defaults
print(format_price(19.99))  # $19.99

# Override currency
print(format_price(19.99, "€"))  # €19.99

# Override decimal places
print(format_price(19.99, decimal_places=0))  # $20

# Override multiple
print(format_price(19.99, "£", 3))  # £19.990

# Use keyword arguments to skip some
print(format_price(19.99, show_symbol=False))  # 19.99
```

### Example 3: Price Calculator with Tax and Discount
```python
def calculate_price(base_price, tax_rate=0.08, discount=0, shipping=0):
    """
    Calculate final price with tax, discount, and shipping.
    
    Parameters:
        base_price (float): Original price
        tax_rate (float): Tax rate as decimal (default: 0.08 = 8%)
        discount (float): Discount amount in dollars (default: 0)
        shipping (float): Shipping cost (default: 0)
    
    Returns:
        float: Final price
    """
    # Calculate: base + tax - discount + shipping
    subtotal = base_price - discount
    tax = subtotal * tax_rate
    final_price = subtotal + tax + shipping
    
    return final_price

# Just base price (8% tax, no discount, no shipping)
print(f"${calculate_price(100):.2f}")  # $108.00

# With discount
print(f"${calculate_price(100, discount=20):.2f}")  # $86.40

# Different tax rate
print(f"${calculate_price(100, tax_rate=0.10):.2f}")  # $110.00

# Full customization
print(f"${calculate_price(100, tax_rate=0.05, discount=15, shipping=10):.2f}")
# $99.25
```

### Example 4: Greeting Generator
```python
def create_greeting(name, title="", greeting="Hello", punctuation="!"):
    """
    Create a personalized greeting.
    
    Parameters:
        name (str): Person's name
        title (str): Title (Mr, Ms, Dr, etc.) - optional
        greeting (str): Greeting word (default: Hello)
        punctuation (str): End punctuation (default: !)
    
    Returns:
        str: Formatted greeting
    """
    if title:
        return f"{greeting} {title} {name}{punctuation}"
    return f"{greeting} {name}{punctuation}"

# Basic greeting
print(create_greeting("Alice"))  # Hello Alice!

# With title
print(create_greeting("Smith", title="Dr"))  # Hello Dr Smith!

# Different greeting
print(create_greeting("Bob", greeting="Hi"))  # Hi Bob!

# Everything custom
print(create_greeting("Johnson", "Prof", "Good morning", "."))
# Good morning Prof Johnson.
```

### Example 5: Email Sender Function
```python
def send_email(to, subject, body, from_address="noreply@company.com",
               cc=None, bcc=None, priority="normal", html=False):
    """
    Send an email (simulated).
    
    Parameters:
        to (str): Recipient email
        subject (str): Email subject
        body (str): Email body
        from_address (str): Sender email (default: noreply@company.com)
        cc (str): CC address (default: None)
        bcc (str): BCC address (default: None)
        priority (str): Email priority (default: normal)
        html (bool): Whether body is HTML (default: False)
    """
    print(f"From: {from_address}")
    print(f"To: {to}")
    if cc:
        print(f"CC: {cc}")
    if bcc:
        print(f"BCC: {bcc}")
    print(f"Subject: {subject}")
    print(f"Priority: {priority}")
    print(f"Format: {'HTML' if html else 'Plain Text'}")
    print(f"Body: {body}")
    print("-" * 50)

# Simple email
send_email("user@example.com", "Test", "This is a test")

# With CC and high priority
send_email(
    "user@example.com",
    "Urgent: Server Down",
    "The production server is down!",
    cc="team@example.com",
    priority="high"
)

# HTML email with custom sender
send_email(
    "customer@example.com",
    "Welcome!",
    "<h1>Welcome to our service!</h1>",
    from_address="welcome@company.com",
    html=True
)
```

### Example 6: Database Connection Function
```python
def connect_database(host, database, username="root", 
                     password="", port=3306, timeout=30):
    """
    Connect to a database (simulated).
    
    Parameters:
        host (str): Database host
        database (str): Database name
        username (str): Username (default: root)
        password (str): Password (default: empty)
        port (int): Port number (default: 3306 for MySQL)
        timeout (int): Connection timeout in seconds (default: 30)
    
    Returns:
        dict: Connection details
    """
    connection = {
        "host": host,
        "database": database,
        "username": username,
        "port": port,
        "timeout": timeout,
        "connected": True
    }
    
    print(f"Connected to {database} at {host}:{port}")
    print(f"User: {username}, Timeout: {timeout}s")
    
    return connection

# Minimal connection (use most defaults)
conn1 = connect_database("localhost", "myapp")

# Custom username and password
conn2 = connect_database(
    "prod-server.com",
    "production_db",
    username="admin",
    password="secure123"
)

# PostgreSQL (different port)
conn3 = connect_database(
    "localhost",
    "postgres_db",
    port=5432,
    timeout=60
)
```

### Example 7: Shopping Cart with Default Tax
```python
def add_to_cart(item_name, price, quantity=1, tax_rate=0.08, 
                gift_wrap=False, express_shipping=False):
    """
    Add item to shopping cart with calculated total.
    
    Parameters:
        item_name (str): Name of item
        price (float): Price per unit
        quantity (int): Number of items (default: 1)
        tax_rate (float): Tax rate (default: 0.08 = 8%)
        gift_wrap (bool): Add gift wrapping (default: False)
        express_shipping (bool): Use express shipping (default: False)
    
    Returns:
        dict: Cart item details
    """
    subtotal = price * quantity
    
    # Add-on fees
    gift_wrap_fee = 5.00 if gift_wrap else 0
    shipping_fee = 15.00 if express_shipping else 5.00
    
    # Calculate tax on subtotal + gift wrap
    taxable_amount = subtotal + gift_wrap_fee
    tax = taxable_amount * tax_rate
    
    total = subtotal + tax + gift_wrap_fee + shipping_fee
    
    cart_item = {
        "item": item_name,
        "unit_price": price,
        "quantity": quantity,
        "subtotal": subtotal,
        "tax": tax,
        "gift_wrap": gift_wrap_fee,
        "shipping": shipping_fee,
        "total": total
    }
    
    # Display
    print(f"\n{'='*40}")
    print(f"Item: {item_name}")
    print(f"Price: ${price:.2f} x {quantity} = ${subtotal:.2f}")
    print(f"Tax ({tax_rate*100}%): ${tax:.2f}")
    if gift_wrap:
        print(f"Gift Wrap: ${gift_wrap_fee:.2f}")
    print(f"Shipping: ${shipping_fee:.2f}")
    print(f"{'='*40}")
    print(f"TOTAL: ${total:.2f}")
    
    return cart_item

# Simple purchase
add_to_cart("Laptop", 999.99)

# Multiple quantities
add_to_cart("Mouse", 29.99, quantity=2)

# With gift wrap and express shipping
add_to_cart("Headphones", 149.99, gift_wrap=True, express_shipping=True)

# Different tax rate (e.g., different state)
add_to_cart("Keyboard", 79.99, tax_rate=0.10)
```

## Practice Exercises

### Beginner Level

1. **Simple Greeter**: Create a function `greet(name, greeting="Hello")` that greets a person with a customizable greeting.

2. **Rectangle Area**: Write `calculate_area(length, width=1)` that calculates rectangle area, defaulting to a square if width is omitted.

3. **Repeater**: Create `repeat_string(text, times=3)` that repeats a string a specified number of times (default 3).

4. **Discount Calculator**: Write `apply_discount(price, discount_percent=10)` that applies a discount with 10% as default.

5. **Coffee Order**: Create `order_coffee(size="medium", milk=True, sugar=True)` that prints a coffee order with defaults.

### Intermediate Level

6. **Email Validator**: Write a function that validates an email, with optional strict mode parameter (default False).

7. **Date Formatter**: Create a function that formats dates with customizable separators (default: "/") and order (default: "MDY").

8. **Password Generator**: Write a function that generates passwords with customizable length (default: 12) and character types.

9. **Shipping Calculator**: Create a function that calculates shipping cost with weight, distance, and optional express shipping (default: False).

10. **Report Generator**: Write a function that creates reports with title, data, optional footer (default: "End of Report"), and format (default: "text").

### Advanced Level

11. **API Request Simulator**: Create a function that simulates API requests with method (default: "GET"), headers (default: {}), timeout (default: 30), retry (default: 3).

12. **Logger Function**: Write a comprehensive logging function with log level (default: "INFO"), timestamp (default: True), file output (default: None).

13. **Cache Manager**: Create a function with TTL (time to live) default, max size default, and eviction policy default.

14. **Query Builder**: Write a function that builds database queries with optional WHERE clauses, ORDER BY (default: None), and LIMIT (default: None).

15. **Configuration Merger**: Create a function that merges configurations with defaults, handling nested dictionaries and overrides.

## Common Mistakes to Avoid

### Mistake 1: Mutable Default Arguments

**Wrong:**
```python
def add_student(name, class_list=[]):
    class_list.append(name)
    return class_list

class1 = add_student("Alice")  # ['Alice']
class2 = add_student("Bob")    # ['Alice', 'Bob'] - WRONG!
# Same list is reused!
```

**Correct:**
```python
def add_student(name, class_list=None):
    if class_list is None:
        class_list = []
    class_list.append(name)
    return class_list

class1 = add_student("Alice")  # ['Alice']
class2 = add_student("Bob")    # ['Bob'] - CORRECT!
```

**Why:** Mutable defaults are created once and shared across all function calls. Always use `None` as default and create the mutable object inside the function.

### Mistake 2: Wrong Parameter Order

**Wrong:**
```python
# SyntaxError: non-default argument follows default argument
def create_user(role="user", username, email):
    pass
```

**Correct:**
```python
def create_user(username, email, role="user"):
    pass
```

**Why:** Required parameters (no default) must come before optional parameters (with default). Python enforces this rule.

### Mistake 3: Confusing Default Values with Function Calls

**Wrong:**
```python
import datetime

# This evaluates ONCE when function is defined!
def log_message(message, timestamp=datetime.datetime.now()):
    print(f"[{timestamp}] {message}")

log_message("First")   # 2024-01-10 10:00:00
time.sleep(5)
log_message("Second")  # 2024-01-10 10:00:00 - SAME TIME!
```

**Correct:**
```python
def log_message(message, timestamp=None):
    if timestamp is None:
        timestamp = datetime.datetime.now()
    print(f"[{timestamp}] {message}")

log_message("First")   # 2024-01-10 10:00:00
time.sleep(5)
log_message("Second")  # 2024-01-10 10:00:05 - CORRECT!
```

**Why:** Default values are evaluated once at function definition time, not each time the function is called.

### Mistake 4: Overriding Defaults Positionally When Order Changes

**Wrong:**
```python
def send_notification(user, message, email=True, sms=False, push=False):
    pass

# Want to enable only push, but this is confusing:
send_notification("Alice", "Hello", False, False, True)
# Hard to read - what do these booleans mean?
```

**Correct:**
```python
# Use keyword arguments for clarity
send_notification("Alice", "Hello", push=True)
# or
send_notification("Alice", "Hello", email=False, push=True)
```

**Why:** Keyword arguments are clearer and more maintainable, especially with boolean flags.

## Real-World Applications

### 1. **API Design**
REST APIs use default parameters for pagination, filtering, and sorting:

```python
def get_users(page=1, per_page=20, sort_by="created_at", 
              order="desc", active_only=True):
    # Fetch users from database with sensible defaults
    pass
```

### 2. **Configuration Management**
Applications use defaults for configuration settings:

```python
def initialize_app(debug=False, port=5000, host="localhost",
                   database_url="sqlite:///app.db"):
    # Start app with production-safe defaults
    pass
```

### 3. **Data Processing**
Data pipelines have default parameters for common operations:

```python
def clean_data(data, remove_nulls=True, normalize=True,
               encoding="utf-8", handle_duplicates="remove"):
    # Process data with standard cleaning options
    pass
```

### 4. **Machine Learning**
ML models use default hyperparameters:

```python
def train_model(data, learning_rate=0.001, epochs=100,
                batch_size=32, optimizer="adam"):
    # Train with commonly used defaults
    pass
```

## Challenge Projects

### 1. **Flexible Calculator**
Create a calculator with default operation.

**Requirements:**
- `calculate(a, b, operation="+")` function
- Support +, -, *, /, **, %
- Optional rounding parameter (default: None)
- Optional absolute value parameter (default: False)
- Comprehensive error handling

### 2. **Blog Post Generator**
Create a function that generates blog posts with many defaults.

**Requirements:**
- Required: title, content
- Defaults: author="Anonymous", published=True, category="General"
- Optional: tags=None, featured_image=None, comments_enabled=True
- Generate slug from title
- Add timestamp
- Return formatted post dictionary

### 3. **Invoice Generator**
Build an invoice generator with customizable defaults.

**Requirements:**
- Required: items list, customer name
- Defaults: tax_rate=0.08, discount=0, payment_terms="Net 30"
- Optional: notes="", due_date=None, invoice_number=auto-generated
- Calculate subtotals, tax, total
- Format and display professional invoice

### 4. **File Backup System**
Create a backup function with intelligent defaults.

**Requirements:**
- Required: source_path
- Defaults: destination="./backups", compress=True, overwrite=False
- Optional: encryption=False, retention_days=30, include_hidden=False
- Generate timestamp-based backup names
- Handle different file types
- Verification after backup

### 5. **Smart Form Validator**
Build a form validation system with default rules.

**Requirements:**
- Validate multiple field types
- Defaults: required=False, min_length=0, max_length=None
- Email validator with default strict=False
- Password validator with default complexity="medium"
- Custom error messages with defaults
- Return validation results dictionary

---

## Navigation

- **Previous:** [31. Functions](31-functions.md)
- **Next:** [33. Keyword Arguments](33-keyword-arguments.md)
- **[Back to Main README](../README.md)**

## 🎓 Key Takeaways from Video

1. Lists store multiple items in a single variable
2. Define functions using the def keyword
3. Import modules to use external code
4. Use loops to repeat actions

> 💡 *These points cover the main concepts from the video tutorial to help reinforce your learning.*