# ⭐ Args and Kwargs

## 🚀 Open Notebook

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/PavanMudigonda/python-bro-code/blob/main/35-args-kwargs/35-args-kwargs.ipynb) [![Open In Kaggle](https://img.shields.io/badge/Open%20in-Kaggle-20BEFF?style=flat&logo=kaggle)](https://kaggle.com/kernels/welcome?src=https://github.com/PavanMudigonda/python-bro-code/blob/main/35-args-kwargs/35-args-kwargs.ipynb)


## 📺 Video Tutorial

[![Watch on YouTube](https://img.shields.io/badge/Watch-YouTube-red?style=for-the-badge&logo=youtube)](https://youtu.be/Vh__2V2tXUM)

**Python *ARGS & **KWARGS are awesome! 📦** (6:57)

## What You'll Learn

In this chapter, you'll master `*args` and `**kwargs` - Python's powerful features for handling variable numbers of arguments. You'll learn how to create flexible functions that accept any number of positional or keyword arguments, understand the unpacking operators, and build truly versatile functions that can adapt to different calling patterns.

## Learning Objectives

- Use `*args` to accept unlimited positional arguments
- Use `**kwargs` to accept unlimited keyword arguments  
- Understand the unpacking operators `*` and `**`
- Master the correct order: positional, default, `*args`, `**kwargs`
- Combine `*args` and `**kwargs` with regular parameters
- Apply variable arguments in real-world scenarios

## Concept Explanation

### What are *args and **kwargs?

**`*args`** (arbitrary arguments) allows a function to accept **any number of positional arguments**. They're collected into a **tuple**.

**`**kwargs`** (keyword arguments) allows a function to accept **any number of keyword arguments**. They're collected into a **dictionary**.

```python
def example(*args, **kwargs):
    print(f"args type: {type(args)}")      # <class 'tuple'>
    print(f"kwargs type: {type(kwargs)}")  # <class 'dict'>
    
example(1, 2, 3, name="Alice", age=25)
```

**The Names Don't Matter!**
- `*args` and `**kwargs` are conventions
- The `*` and `**` are what matters
- Could use `*numbers`, `**options`, etc.

```python
# These all work the same:
def func1(*args, **kwargs): pass
def func2(*items, **options): pass  
def func3(*values, **settings): pass
```

But stick with `*args` and `**kwargs` - it's what other Python developers expect!

### Why Use *args and **kwargs?

#### 1. **Unknown Number of Arguments**
When you don't know how many arguments you'll receive:

```python
# Without *args - limited
def add_two(a, b):
    return a + b

# With *args - unlimited!
def add(*args):
    return sum(args)

add(1, 2)           # 3
add(1, 2, 3)        # 6
add(1, 2, 3, 4, 5)  # 15
```

#### 2. **Wrapper Functions**
When creating decorators or wrapper functions:

```python
def logged(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        return func(*args, **kwargs)  # Pass everything through
    return wrapper

@logged
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

greet("Alice")  # Works!
greet("Bob", greeting="Hi")  # Also works!
```

#### 3. **Flexible Configuration**
Accept arbitrary configuration options:

```python
def configure_app(**kwargs):
    for key, value in kwargs.items():
        print(f"Setting {key} = {value}")

configure_app(debug=True, port=8000, host="localhost")
# Can pass any number of settings!
```

### Understanding *args (Arbitrary Positional Arguments)

`*args` collects extra positional arguments into a **tuple**:

```python
def print_args(*args):
    print(f"Type: {type(args)}")  # <class 'tuple'>
    print(f"Count: {len(args)}")
    for i, arg in enumerate(args, 1):
        print(f"  Arg {i}: {arg}")

print_args(1, 2, 3)
# Type: <class 'tuple'>
# Count: 3
#   Arg 1: 1
#   Arg 2: 2
#   Arg 3: 3
```

**Combining with Regular Parameters:**

```python
def greet(greeting, *names):
    # greeting is required
    # names can be 0 or more
    for name in names:
        print(f"{greeting}, {name}!")

greet("Hello", "Alice", "Bob", "Charlie")
# Hello, Alice!
# Hello, Bob!
# Hello, Charlie!
```

### Understanding **kwargs (Arbitrary Keyword Arguments)

`**kwargs` collects extra keyword arguments into a **dictionary**:

```python
def print_kwargs(**kwargs):
    print(f"Type: {type(kwargs)}")  # <class 'dict'>
    print(f"Count: {len(kwargs)}")
    for key, value in kwargs.items():
        print(f"  {key} = {value}")

print_kwargs(name="Alice", age=25, city="NYC")
# Type: <class 'dict'>
# Count: 3
#   name = Alice
#   age = 25
#   city = NYC
```

**Combining with Regular Parameters:**

```python
def create_user(username, **details):
    # username is required
    # details can be any keyword arguments
    print(f"Username: {username}")
    for key, value in details.items():
        print(f"{key}: {value}")

create_user("alice123", email="alice@example.com", age=25, verified=True)
```

### Parameter Order (CRITICAL!)

Parameters must be in this exact order:

```python
def function(
    positional1, positional2,  # 1. Regular positional
    default1=value1,           # 2. Default arguments
    *args,                     # 3. *args (catches extra positional)
    keyword1=value2,           # 4. Keyword-only arguments (after *args)
    **kwargs                   # 5. **kwargs (catches extra keywords)
):
    pass
```

**Complete Example:**

```python
def complex_function(required, default="default", *args, 
                     keyword_only, **kwargs):
    print(f"Required: {required}")
    print(f"Default: {default}")
    print(f"Args: {args}")
    print(f"Keyword-only: {keyword_only}")
    print(f"Kwargs: {kwargs}")

complex_function(
    "value1",              # required
    "value2",              # default
    "extra1", "extra2",    # args
    keyword_only="kw",     # keyword_only (must use keyword!)
    option1="opt1",        # kwargs
    option2="opt2"         # kwargs
)
```

### Unpacking with * and **

The `*` and `**` operators also **unpack** sequences and dictionaries:

**Unpacking Lists/Tuples with *:**

```python
def add(a, b, c):
    return a + b + c

numbers = [1, 2, 3]
result = add(*numbers)  # Same as add(1, 2, 3)
print(result)  # 6
```

**Unpacking Dictionaries with **:**

```python
def greet(greeting, name):
    print(f"{greeting}, {name}!")

data = {"greeting": "Hello", "name": "Alice"}
greet(**data)  # Same as greet(greeting="Hello", name="Alice")
```

**Combining in Function Calls:**

```python
def full_name(first, middle, last, title="Mr"):
    return f"{title} {first} {middle} {last}"

names = ["John", "Paul"]
details = {"last": "Smith", "title": "Dr"}

print(full_name(*names, **details))
# Dr John Paul Smith
```

### Common Patterns

#### 1. **Sum All Numbers**
```python
def sum_all(*numbers):
    return sum(numbers)

print(sum_all(1, 2, 3, 4, 5))  # 15
```

#### 2. **Print with Custom Separator**
```python
def print_items(*items, sep=" | "):
    print(sep.join(str(item) for item in items))

print_items("apple", "banana", "cherry")
# apple | banana | cherry

print_items(1, 2, 3, sep=" -> ")
# 1 -> 2 -> 3
```

#### 3. **Merge Dictionaries**
```python
def merge_configs(**configs):
    # Start with defaults
    default_config = {"debug": False, "port": 8000}
    # Update with provided configs
    default_config.update(configs)
    return default_config

config = merge_configs(debug=True, database="postgres")
print(config)
# {'debug': True, 'port': 8000, 'database': 'postgres'}
```

#### 4. **Shipping Labels**
```python
def shipping_label(name, *args, **kwargs):
    # name is required
    # args = additional address lines
    # kwargs = extra info (phone, email, etc.)
    
    print(f"To: {name}")
    for line in args:
        print(f"    {line}")
    for key, value in kwargs.items():
        print(f"{key}: {value}")

shipping_label(
    "John Doe",
    "123 Main St",
    "Apt 4B",
    "New York, NY 10001",
    phone="555-1234",
    delivery="Express"
)
```

## Examples

### Example 1: Simple *args Function
```python
def multiply(*numbers):
    """
    Multiply all numbers together.
    
    Parameters:
        *numbers: Variable number of numeric arguments
    
    Returns:
        Product of all numbers
    """
    result = 1
    for num in numbers:
        result *= num
    return result

print(multiply(2, 3))          # 6
print(multiply(2, 3, 4))       # 24
print(multiply(2, 3, 4, 5))    # 120
print(multiply(10))            # 10
```

### Example 2: Simple **kwargs Function
```python
def display_info(**info):
    """
    Display user information.
    
    Parameters:
        **info: Variable keyword arguments with user details
    """
    print("User Information:")
    print("-" * 30)
    for key, value in info.items():
        # Capitalize key for display
        print(f"{key.title()}: {value}")
    print("-" * 30)

display_info(name="Alice", age=25, city="NYC", job="Engineer")
# User Information:
# ------------------------------
# Name: Alice
# Age: 25
# City: NYC
# Job: Engineer
# ------------------------------
```

### Example 3: Combining *args and **kwargs
```python
def create_shipping_label(*address_lines, **contact):
    """
    Create a shipping label with address and contact info.
    
    Parameters:
        *address_lines: Address components (street, city, etc.)
        **contact: Contact information (phone, email, etc.)
    """
    print("=" * 40)
    print("SHIPPING LABEL")
    print("=" * 40)
    
    # Print address
    print("\nAddress:")
    for line in address_lines:
        print(f"  {line}")
    
    # Print contact info
    if contact:
        print("\nContact Information:")
        for key, value in contact.items():
            print(f"  {key.title()}: {value}")
    
    print("=" * 40)

create_shipping_label(
    "John Smith",
    "123 Main Street",
    "Apartment 4B",
    "New York, NY 10001",
    phone="555-123-4567",
    email="john@example.com",
    delivery_instructions="Leave at front desk"
)
```

### Example 4: Function Average Calculator
```python
def calculate_stats(*numbers, operation="mean"):
    """
    Calculate statistics for numbers.
    
    Parameters:
        *numbers: Variable number of numeric values
        operation (str): Type of stat ('mean', 'sum', 'min', 'max')
    
    Returns:
        Calculated statistic
    """
    if not numbers:
        return None
    
    if operation == "mean":
        return sum(numbers) / len(numbers)
    elif operation == "sum":
        return sum(numbers)
    elif operation == "min":
        return min(numbers)
    elif operation == "max":
        return max(numbers)
    else:
        return None

# Different operations
print(f"Mean: {calculate_stats(10, 20, 30, 40, 50)}")
# Mean: 30.0

print(f"Sum: {calculate_stats(10, 20, 30, 40, 50, operation='sum')}")
# Sum: 150

print(f"Max: {calculate_stats(10, 20, 30, 40, 50, operation='max')}")
# Max: 50
```

### Example 5: Custom Print Function
```python
def custom_print(*args, sep=" ", end="\n", prefix="", suffix=""):
    """
    Custom print function with additional options.
    
    Parameters:
        *args: Items to print
        sep (str): Separator between items
        end (str): String appended after last item
        prefix (str): String prepended before first item
        suffix (str): String appended after all items
    """
    output = prefix + sep.join(str(arg) for arg in args) + suffix
    print(output, end=end)

# Basic usage
custom_print("Hello", "World")
# Hello World

# With custom separator
custom_print(1, 2, 3, 4, 5, sep=" -> ")
# 1 -> 2 -> 3 -> 4 -> 5

# With prefix and suffix
custom_print("Error:", "File not found", prefix="[!] ", suffix=" (!)")
# [!] Error: File not found (!)
```

### Example 6: Configuration Builder
```python
def build_config(app_name, *required_features, **optional_settings):
    """
    Build application configuration.
    
    Parameters:
        app_name (str): Application name (required)
        *required_features: Required feature names
        **optional_settings: Optional configuration settings
    
    Returns:
        dict: Complete configuration
    """
    config = {
        "app_name": app_name,
        "features": list(required_features),
        "settings": optional_settings
    }
    
    # Display configuration
    print(f"Configuration for: {app_name}")
    print(f"Required Features: {', '.join(required_features)}")
    print(f"Settings:")
    for key, value in optional_settings.items():
        print(f"  {key}: {value}")
    
    return config

# Build configuration
config = build_config(
    "MyApp",
    "authentication",
    "database",
    "api",
    debug=True,
    port=8080,
    database_url="postgresql://localhost/mydb",
    cache_enabled=True
)
```

### Example 7: Advanced Wrapper Function
```python
def timer_decorator(func):
    """Decorator that times function execution."""
    import time
    
    def wrapper(*args, **kwargs):
        """Wrapper that accepts any arguments."""
        print(f"Calling {func.__name__}...")
        
        start_time = time.time()
        result = func(*args, **kwargs)  # Pass all arguments through
        end_time = time.time()
        
        print(f"Execution time: {end_time - start_time:.4f} seconds")
        return result
    
    return wrapper

@timer_decorator
def process_data(*numbers, operation="sum"):
    """Process numbers with specified operation."""
    import time
    time.sleep(0.5)  # Simulate processing
    
    if operation == "sum":
        return sum(numbers)
    elif operation == "product":
        result = 1
        for num in numbers:
            result *= num
        return result

# Decorator works with any arguments!
result1 = process_data(1, 2, 3, 4, 5)
# Calling process_data...
# Execution time: 0.5xxx seconds

result2 = process_data(2, 3, 4, operation="product")
# Calling process_data...
# Execution time: 0.5xxx seconds
```

## Practice Exercises

### Beginner Level

1. **Max Finder**: Write a function `find_max(*numbers)` that returns the maximum number from any number of arguments.

2. **String Joiner**: Create `join_strings(*strings, sep=" ")` that joins all strings with a separator.

3. **Info Display**: Write `display_user(**info)` that prints all user information from keyword arguments.

4. **List Combiner**: Create `combine_lists(*lists)` that combines multiple lists into one.

5. **Greeting Generator**: Write `greet_all(*names, greeting="Hello")` that greets multiple people.

### Intermediate Level

6. **Shopping Cart**: Create a function that accepts items as *args and calculates total with tax from **kwargs.

7. **Data Filter**: Write a function that filters a dataset using *args for required filters and **kwargs for optional ones.

8. **HTML Generator**: Create `html_tag(tag_name, *content, **attributes)` that generates HTML tags.

9. **Query Builder**: Write a SQL query builder using *tables for JOIN and **conditions for WHERE.

10. **Logger**: Create a logging function that accepts message, *extra_info, and **metadata.

### Advanced Level

11. **Decorator Factory**: Create a decorator factory that accepts *args and **kwargs and passes them to decorated functions.

12. **API Client**: Write a flexible API client method that handles *path_segments and **query_params.

13. **Data Validator**: Create a validator that accepts *validation_rules and **validation_config.

14. **Event System**: Build an event emitter that can pass *event_args and **event_kwargs to listeners.

15. **ORM Query**: Create a database ORM query method using *select_fields, **filter_conditions, and other keyword args.

## Common Mistakes to Avoid

### Mistake 1: Wrong Parameter Order

**Wrong:**
```python
# SyntaxError: invalid syntax
def bad_function(**kwargs, *args):
    pass
```

**Correct:**
```python
def good_function(*args, **kwargs):
    pass
```

**Why:** `*args` must come before `**kwargs`. Python enforces strict parameter order.

### Mistake 2: Forgetting *args is a Tuple

**Wrong:**
```python
def add(*args):
    return args + 10  # TypeError: can only concatenate tuple (not "int") to tuple

add(1, 2, 3)
```

**Correct:**
```python
def add(*args):
    return sum(args) + 10  # Use sum() for tuple of numbers

add(1, 2, 3)  # Returns 16
```

**Why:** `*args` is a tuple, not a single value. Use appropriate tuple operations.

### Mistake 3: Not Unpacking When Passing Lists/Dicts

**Wrong:**
```python
def add(a, b, c):
    return a + b + c

numbers = [1, 2, 3]
result = add(numbers)  # TypeError: missing 2 required positional arguments
```

**Correct:**
```python
numbers = [1, 2, 3]
result = add(*numbers)  # Unpack the list
print(result)  # 6
```

**Why:** Need `*` to unpack sequence into separate arguments.

### Mistake 4: Modifying *args or **kwargs Directly

**Wrong:**
```python
def process(*args, **kwargs):
    args.append(100)  # AttributeError: 'tuple' object has no attribute 'append'
    kwargs["new"] = "value"  # This works but modifies the original dict!
```

**Correct:**
```python
def process(*args, **kwargs):
    args_list = list(args)  # Convert to list
    args_list.append(100)
    
    kwargs_copy = kwargs.copy()  # Create a copy
    kwargs_copy["new"] = "value"
```

**Why:** `*args` is a tuple (immutable). `**kwargs` modifications affect the original if you're not careful.

## Real-World Applications

### 1. **Logging Libraries**
Logging functions use *args and **kwargs to handle flexible message formatting:

```python
logger.info("User %s logged in from %s", username, ip_address)
logger.error("Error occurred", exc_info=True, stack_info=True)
```

### 2. **Django ORM**
Database queries use **kwargs for flexible filtering:

```python
User.objects.filter(age__gte=18, is_active=True, city="NYC")
Article.objects.create(title="Post", content="...", author=user)
```

### 3. **Matplotlib**
Plotting functions accept *args for data and **kwargs for styling:

```python
plt.plot(x, y, color='blue', linewidth=2, marker='o', label='Data')
```

### 4. **Function Decorators**
Decorators use *args and **kwargs to wrap any function:

```python
@cache
@retry(attempts=3)
@log_execution
def api_call(endpoint, method="GET", **params):
    pass
```

## Challenge Projects

### 1. **Universal Function Logger**
Create a decorator that logs function calls with all arguments.

**Requirements:**
- Log function name
- Log all positional arguments
- Log all keyword arguments
- Log return value
- Log execution time
- Handle exceptions
- Configurable log level

### 2. **Flexible Calculator**
Build a calculator that handles multiple operations and numbers.

**Requirements:**
- `calculate(*numbers, operation="sum")`
- Support: sum, product, average, min, max
- Handle **options for rounding, formatting
- Error handling for invalid operations
- Return detailed result dictionary

### 3. **HTML Tag Generator**
Create a system to generate HTML tags with any attributes.

**Requirements:**
- `tag(name, *content, **attributes)`
- Handle nested tags (content can be other tags)
- Self-closing tags (img, br, hr)
- Proper attribute formatting
- HTML escaping
- Pretty printing option

### 4. **Event System**
Build a publish-subscribe event system.

**Requirements:**
- `emit(event_name, *args, **kwargs)`
- `subscribe(event_name, callback)`
- Pass *args and **kwargs to callbacks
- Multiple subscribers per event
- Event history
- Wildcard event matching

### 5. **Data Pipeline Builder**
Create a data processing pipeline using *args and **kwargs.

**Requirements:**
- `pipeline(*functions, **config)`
- Chain multiple processing functions
- Pass data through pipeline
- Each function accepts *args and **kwargs
- Error handling and rollback
- Progress tracking
- Partial pipeline execution

---

## Navigation

- **Previous:** [33. Keyword Arguments](33-keyword-arguments.md)
- **Next:** [35. Iterables](35-iterables.md)
- **[Back to Main README](../README.md)**

## 🎓 Key Takeaways from Video

1. Functions are reusable blocks of code
2. Understanding the proper syntax is important
3. Define functions using the def keyword
4. Use loops to repeat actions
5. Use if-elif-else for conditional logic

> 💡 *These points cover the main concepts from the video tutorial to help reinforce your learning.*