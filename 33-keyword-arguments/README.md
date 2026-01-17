# 🏷️ Keyword Arguments


## 📺 Video Tutorial

[![Watch on YouTube](https://img.shields.io/badge/Watch-BroCode_Python_Master_Class-red?style=for-the-badge&logo=youtube)](https://youtu.be/m2uURZxex3c)


## What You'll Learn

In this chapter, you'll master keyword arguments - a powerful Python feature that lets you pass arguments by parameter name rather than position. You'll learn how keyword arguments improve code readability, reduce errors, enable flexible function calls, and create self-documenting code that's easier to maintain.

## Learning Objectives

- Call functions using keyword arguments (name=value syntax)
- Understand advantages of keyword arguments over positional arguments
- Mix positional and keyword arguments correctly
- Use keyword arguments to skip optional parameters
- Write more readable and maintainable function calls
- Apply best practices for when to use keyword vs positional arguments

## Concept Explanation

### What are Keyword Arguments?

Keyword arguments are arguments passed to a function with the parameter name explicitly specified using the `name=value` syntax.

**Positional Arguments (Traditional Way):**
```python
def greet(greeting, title, first, last):
    print(f"{greeting} {title} {first} {last}")

# Order matters - must match parameter order
greet("Hello", "Mr", "John", "Doe")
```

**Keyword Arguments (Named Way):**
```python
# Order doesn't matter - names are explicit
greet(greeting="Hello", title="Mr", first="John", last="Doe")

# Can be in any order!
greet(last="Doe", first="John", greeting="Hello", title="Mr")
```

### Why Use Keyword Arguments?

#### 1. **Improved Readability**
Code becomes self-documenting:

```python
# Positional - what do these mean?
create_user("alice", 25, "alice@email.com", True, False)

# Keyword - crystal clear!
create_user(
    username="alice",
    age=25,
    email="alice@email.com",
    active=True,
    admin=False
)
```

#### 2. **Order Independence**
Don't need to remember parameter order:

```python
def book_flight(from_city, to_city, date, passengers, class_type):
    pass

# Positional - must remember exact order
book_flight("NYC", "LAX", "2024-05-15", 2, "economy")

# Keyword - order doesn't matter
book_flight(
    to_city="LAX",
    from_city="NYC",
    passengers=2,
    date="2024-05-15",
    class_type="economy"
)
```

#### 3. **Skip Optional Parameters**
Can specify only the parameters you want to change:

```python
def format_text(text, bold=False, italic=False, underline=False, 
                color="black", size=12):
    pass

# Positional - must provide all or use positional order
format_text("Hello", False, False, False, "red", 12)

# Keyword - specify only what you need
format_text("Hello", color="red")
format_text("Hello", bold=True, size=16)
```

#### 4. **Prevent Errors**
Explicit names prevent mistakes:

```python
def set_alarm(hour, minute, am_pm):
    pass

# Positional - easy to swap hour and minute
set_alarm(30, 7, "AM")  # WRONG - meant 7:30, got 30:07

# Keyword - prevents confusion
set_alarm(hour=7, minute=30, am_pm="AM")  # CORRECT
```

### Mixing Positional and Keyword Arguments

You can combine both styles, but **positional must come first**:

```python
def create_account(username, password, email, notifications=True):
    pass

# ✓ VALID - positional then keyword
create_account("alice", "pass123", "alice@email.com", notifications=False)

# ✓ VALID - some positional, some keyword
create_account("alice", "pass123", email="alice@email.com")

# ✓ VALID - all keyword
create_account(username="alice", password="pass123", email="alice@email.com")

# ✗ INVALID - keyword before positional
create_account(username="alice", "pass123", "alice@email.com")  # SyntaxError!
```

### When to Use Keyword Arguments

**Use Keyword Arguments When:**

1. **Function has many parameters** (3+ is a good rule of thumb)
   ```python
   # Hard to read
   connect("localhost", 5432, "admin", "pass", 30, True, False)
   
   # Easy to read
   connect(
       host="localhost",
       port=5432,
       user="admin",
       password="pass",
       timeout=30,
       ssl=True,
       debug=False
   )
   ```

2. **Parameters are boolean flags**
   ```python
   # What do these True/False mean?
   process_data(data, True, False, True)
   
   # Now it's obvious
   process_data(data, normalize=True, cache=False, async_mode=True)
   ```

3. **You want to skip optional parameters**
   ```python
   def send_email(to, subject, body, cc=None, bcc=None, priority="normal"):
       pass
   
   # Skip cc and bcc, set priority
   send_email("user@example.com", "Hello", "Message", priority="high")
   ```

4. **Parameter order isn't intuitive**
   ```python
   # Which is width and which is height?
   create_rectangle(200, 100)
   
   # Clear and explicit
   create_rectangle(width=200, height=100)
   ```

**Use Positional Arguments When:**

1. **Function has 1-2 obvious parameters**
   ```python
   # These are fine with positional
   print("Hello")
   len([1, 2, 3])
   max(5, 10)
   ```

2. **Order is natural and obvious**
   ```python
   # From/to order is intuitive
   range(1, 10)
   substring.replace("old", "new")
   ```

### Keyword-Only Arguments (Advanced)

You can force parameters to be keyword-only using `*`:

```python
def create_user(username, *, email, age):
    # username can be positional or keyword
    # email and age MUST be keyword
    pass

# ✓ VALID
create_user("alice", email="alice@email.com", age=25)

# ✗ INVALID - email and age must be keyword
create_user("alice", "alice@email.com", 25)  # TypeError!
```

This prevents mistakes when parameter order might be confusing.

### Best Practices

#### 1. **Use Descriptive Parameter Names**
```python
# Bad - unclear names
def calc(x, y, z):
    pass

# Good - clear names
def calculate_price(base_price, tax_rate, discount):
    pass
```

#### 2. **Consistency in Your Codebase**
```python
# If you use keyword arguments for similar functions, be consistent
create_user(username="alice", email="alice@email.com")
create_admin(username="bob", email="bob@email.com")  # Same style
```

#### 3. **Document Parameters**
```python
def complex_function(param1, param2, param3=None, param4=False):
    """
    Brief description.
    
    Parameters:
        param1 (type): Description
        param2 (type): Description
        param3 (type, optional): Description. Defaults to None.
        param4 (bool, optional): Description. Defaults to False.
    """
    pass
```

## Examples

### Example 1: Basic Keyword Arguments
```python
def introduce_person(greeting, title, first_name, last_name):
    """Print a formal introduction."""
    print(f"{greeting} {title} {first_name} {last_name}")

# Positional - order matters
introduce_person("Hello", "Dr", "Jane", "Smith")

# Keyword - order doesn't matter
introduce_person(
    last_name="Smith",
    first_name="Jane",
    greeting="Hello",
    title="Dr"
)

# Mixed - positional first, then keyword
introduce_person("Hello", "Dr", last_name="Smith", first_name="Jane")

# Output for all: Hello Dr Jane Smith
```

### Example 2: Configuration Function
```python
def configure_server(hostname, port, ssl=True, timeout=30, 
                     max_connections=100, debug=False):
    """
    Configure server settings.
    
    Parameters:
        hostname (str): Server hostname
        port (int): Port number
        ssl (bool): Enable SSL (default: True)
        timeout (int): Timeout in seconds (default: 30)
        max_connections (int): Max concurrent connections (default: 100)
        debug (bool): Enable debug mode (default: False)
    """
    print(f"Server Configuration:")
    print(f"  Host: {hostname}:{port}")
    print(f"  SSL: {ssl}")
    print(f"  Timeout: {timeout}s")
    print(f"  Max Connections: {max_connections}")
    print(f"  Debug: {debug}")

# Basic configuration
configure_server("api.example.com", 443)

# Enable debug mode
configure_server("localhost", 8000, debug=True)

# Full customization with keyword arguments
configure_server(
    hostname="prod.example.com",
    port=443,
    ssl=True,
    timeout=60,
    max_connections=500,
    debug=False
)
```

### Example 3: Email Sending Function
```python
def send_email(recipient, subject, body, sender="noreply@company.com",
               cc=None, bcc=None, attachments=None, priority="normal"):
    """
    Send an email with various options.
    
    Parameters:
        recipient (str): Recipient email address
        subject (str): Email subject
        body (str): Email body content
        sender (str): Sender email (default: noreply@company.com)
        cc (str): CC address (default: None)
        bcc (str): BCC address (default: None)
        attachments (list): List of file paths (default: None)
        priority (str): Email priority (default: normal)
    """
    print(f"Sending email:")
    print(f"  From: {sender}")
    print(f"  To: {recipient}")
    if cc:
        print(f"  CC: {cc}")
    if bcc:
        print(f"  BCC: {bcc}")
    print(f"  Subject: {subject}")
    print(f"  Priority: {priority}")
    if attachments:
        print(f"  Attachments: {', '.join(attachments)}")
    print(f"  Body: {body[:50]}...")

# Simple email
send_email("user@example.com", "Hello", "This is a test message")

# With CC and priority
send_email(
    recipient="user@example.com",
    subject="Important Update",
    body="Please review the attached document",
    cc="manager@example.com",
    priority="high"
)

# Complex email with all options
send_email(
    recipient="client@example.com",
    subject="Project Proposal",
    body="Please find attached our project proposal...",
    sender="sales@company.com",
    cc="team@company.com",
    bcc="archive@company.com",
    attachments=["proposal.pdf", "budget.xlsx"],
    priority="high"
)
```

### Example 4: Database Query Builder
```python
def build_query(table, columns="*", where=None, order_by=None, 
                limit=None, offset=0):
    """
    Build a SQL SELECT query.
    
    Parameters:
        table (str): Table name
        columns (str): Columns to select (default: *)
        where (str): WHERE clause (default: None)
        order_by (str): ORDER BY clause (default: None)
        limit (int): LIMIT number (default: None)
        offset (int): OFFSET number (default: 0)
    
    Returns:
        str: SQL query string
    """
    query = f"SELECT {columns} FROM {table}"
    
    if where:
        query += f" WHERE {where}"
    
    if order_by:
        query += f" ORDER BY {order_by}"
    
    if limit:
        query += f" LIMIT {limit}"
        if offset:
            query += f" OFFSET {offset}"
    
    return query

# Simple query
print(build_query("users"))
# SELECT * FROM users

# With WHERE clause
print(build_query("users", where="age > 18"))
# SELECT * FROM users WHERE age > 18

# Complex query with keyword arguments
print(build_query(
    table="products",
    columns="id, name, price",
    where="category = 'electronics'",
    order_by="price DESC",
    limit=10
))
# SELECT id, name, price FROM products 
# WHERE category = 'electronics' ORDER BY price DESC LIMIT 10

# Pagination
print(build_query(
    table="posts",
    order_by="created_at DESC",
    limit=20,
    offset=40
))
# SELECT * FROM posts ORDER BY created_at DESC LIMIT 20 OFFSET 40
```

### Example 5: Image Processor
```python
def process_image(filename, resize=None, rotate=0, flip=None,
                  brightness=1.0, contrast=1.0, output_format="jpg"):
    """
    Process an image with various transformations.
    
    Parameters:
        filename (str): Input file path
        resize (tuple): New size as (width, height) (default: None)
        rotate (int): Rotation degrees (default: 0)
        flip (str): Flip direction 'horizontal' or 'vertical' (default: None)
        brightness (float): Brightness multiplier (default: 1.0)
        contrast (float): Contrast multiplier (default: 1.0)
        output_format (str): Output format (default: jpg)
    """
    print(f"Processing: {filename}")
    
    if resize:
        print(f"  Resizing to {resize[0]}x{resize[1]}")
    
    if rotate != 0:
        print(f"  Rotating {rotate} degrees")
    
    if flip:
        print(f"  Flipping {flip}")
    
    if brightness != 1.0:
        print(f"  Adjusting brightness: {brightness}")
    
    if contrast != 1.0:
        print(f"  Adjusting contrast: {contrast}")
    
    print(f"  Output format: {output_format}")

# Simple processing
process_image("photo.jpg")

# Resize only
process_image("photo.jpg", resize=(800, 600))

# Multiple transformations using keyword arguments
process_image(
    filename="photo.jpg",
    resize=(1920, 1080),
    rotate=90,
    brightness=1.2,
    output_format="png"
)

# Complete transformation
process_image(
    "landscape.jpg",
    resize=(1200, 800),
    rotate=180,
    flip="horizontal",
    brightness=1.1,
    contrast=1.3,
    output_format="webp"
)
```

### Example 6: API Request Function
```python
def api_request(endpoint, method="GET", headers=None, params=None,
                data=None, timeout=30, verify_ssl=True):
    """
    Make an API request (simulated).
    
    Parameters:
        endpoint (str): API endpoint URL
        method (str): HTTP method (default: GET)
        headers (dict): Request headers (default: None)
        params (dict): URL parameters (default: None)
        data (dict): Request body data (default: None)
        timeout (int): Timeout in seconds (default: 30)
        verify_ssl (bool): Verify SSL certificate (default: True)
    """
    print(f"API Request:")
    print(f"  URL: {endpoint}")
    print(f"  Method: {method}")
    print(f"  Timeout: {timeout}s")
    print(f"  SSL Verification: {verify_ssl}")
    
    if headers:
        print(f"  Headers: {headers}")
    if params:
        print(f"  Params: {params}")
    if data:
        print(f"  Data: {data}")

# Simple GET request
api_request("https://api.example.com/users")

# GET with parameters
api_request(
    endpoint="https://api.example.com/search",
    params={"q": "python", "limit": 10}
)

# POST request with data
api_request(
    endpoint="https://api.example.com/users",
    method="POST",
    data={"name": "Alice", "email": "alice@example.com"},
    headers={"Content-Type": "application/json"}
)

# Complex request
api_request(
    endpoint="https://api.example.com/data",
    method="PUT",
    headers={
        "Authorization": "Bearer token123",
        "Content-Type": "application/json"
    },
    data={"status": "active"},
    timeout=60,
    verify_ssl=False
)
```

### Example 7: Advanced Reporting Function
```python
def generate_report(title, data, report_type="summary", 
                    include_charts=True, include_stats=True,
                    page_size="A4", orientation="portrait",
                    font_size=12, color_scheme="default"):
    """
    Generate a customizable report.
    
    Parameters:
        title (str): Report title
        data (list): Report data
        report_type (str): Type of report (default: summary)
        include_charts (bool): Include charts (default: True)
        include_stats (bool): Include statistics (default: True)
        page_size (str): Page size (default: A4)
        orientation (str): Page orientation (default: portrait)
        font_size (int): Base font size (default: 12)
        color_scheme (str): Color scheme (default: default)
    """
    print(f"{'='*50}")
    print(f"GENERATING REPORT: {title}")
    print(f"{'='*50}")
    print(f"Type: {report_type}")
    print(f"Data points: {len(data)}")
    print(f"Page: {page_size} {orientation}")
    print(f"Font size: {font_size}pt")
    print(f"Color scheme: {color_scheme}")
    print(f"Include charts: {include_charts}")
    print(f"Include statistics: {include_stats}")

# Basic report
sales_data = [100, 150, 200, 175, 225]
generate_report("Monthly Sales", sales_data)

# Customized report
generate_report(
    title="Annual Financial Report",
    data=sales_data,
    report_type="detailed",
    page_size="Letter",
    orientation="landscape",
    color_scheme="corporate"
)

# Minimal report (no charts/stats)
generate_report(
    "Quick Summary",
    sales_data,
    include_charts=False,
    include_stats=False,
    font_size=10
)
```

## Practice Exercises

### Beginner Level

1. **Person Profile**: Create a function `create_profile(name, age, city, country)` and call it using keyword arguments in different orders.

2. **Pizza Order**: Write `order_pizza(size, crust, toppings)` and practice calling it with keyword arguments.

3. **Book Info**: Create `display_book(title, author, year, pages)` and call it with mixed positional and keyword arguments.

4. **Calculator**: Write `calculate(num1, num2, operation)` and call it using keyword arguments for clarity.

5. **Color Mixer**: Create `mix_colors(color1, color2, ratio)` where ratio defaults to 0.5, use keyword arguments.

### Intermediate Level

6. **Event Scheduler**: Create a function with parameters for event name, date, time, location, attendees, and optional notes. Use keyword arguments for flexibility.

7. **Product Filter**: Write a function that filters products by category, price range, brand, and availability. Use keyword arguments to make filters optional.

8. **User Registration**: Create a registration function with required fields (username, email) and optional fields (phone, address, preferences). Demonstrate keyword argument usage.

9. **Chart Generator**: Write a function that creates charts with customizable title, data, chart type, colors, and legend. Use keyword arguments for customization.

10. **Notification System**: Create a function that sends notifications with type, message, recipient, priority, and optional scheduled time. Use keyword arguments.

### Advanced Level

11. **API Wrapper**: Create a comprehensive API wrapper function with method, endpoint, headers, params, body, auth, timeout, and retry logic. Use keyword-only arguments for optional parameters.

12. **Database ORM**: Write a query builder that uses keyword arguments for table, select, where, join, group_by, having, order_by, and limit clauses.

13. **Report Generator**: Create a complex report generator with 10+ optional parameters using keyword arguments, including output format, styling, filters, and sorting.

14. **Config Manager**: Write a configuration manager that accepts arbitrary keyword arguments and validates them against a schema.

15. **ML Model Trainer**: Create a function that trains a model with hyperparameters passed as keyword arguments (learning_rate, epochs, batch_size, optimizer, etc.).

## Common Mistakes to Avoid

### Mistake 1: Keyword Argument Before Positional

**Wrong:**
```python
def greet(greeting, title, first, last):
    print(f"{greeting} {title} {first} {last}")

# SyntaxError: positional argument follows keyword argument
greet(greeting="Hello", title="Mr", "John", "Doe")
```

**Correct:**
```python
# Positional arguments must come first
greet("Hello", "Mr", first="John", last="Doe")

# Or use all keyword arguments
greet(greeting="Hello", title="Mr", first="John", last="Doe")
```

**Why:** Python requires positional arguments to come before keyword arguments in function calls.

### Mistake 2: Misspelling Parameter Names

**Wrong:**
```python
def create_user(username, email, age):
    pass

# TypeError: create_user() got an unexpected keyword argument 'user_name'
create_user(user_name="alice", email="alice@example.com", age=25)
```

**Correct:**
```python
# Use exact parameter names
create_user(username="alice", email="alice@example.com", age=25)
```

**Why:** Keyword argument names must exactly match parameter names. Typos cause errors.

### Mistake 3: Passing Same Argument Twice

**Wrong:**
```python
def greet(name, greeting):
    print(f"{greeting}, {name}!")

# TypeError: greet() got multiple values for argument 'name'
greet("Alice", name="Bob")
```

**Correct:**
```python
# Choose one way to pass the argument
greet("Alice", greeting="Hello")
# or
greet(name="Alice", greeting="Hello")
```

**Why:** You can't pass the same parameter both positionally and by keyword.

### Mistake 4: Not Using Keyword Arguments When They Would Help

**Wrong:**
```python
# What do these mean?
configure_app(True, False, True, 30, "localhost", 8080, False)
# Very hard to understand!
```

**Correct:**
```python
# Much clearer with keyword arguments
configure_app(
    debug=True,
    testing=False,
    logging=True,
    timeout=30,
    host="localhost",
    port=8080,
    ssl=False
)
```

**Why:** Keyword arguments make code self-documenting and easier to maintain.

## Real-World Applications

### 1. **Django Web Framework**
Django extensively uses keyword arguments for clarity:

```python
# URL routing
path('articles/<int:year>/', views.year_archive, name='year_archive')

# Database queries
Article.objects.filter(pub_date__year=2024, status='published')

# Form creation
forms.CharField(max_length=100, required=True, label='Username')
```

### 2. **Data Science with Pandas**
Pandas functions use keyword arguments for flexible data manipulation:

```python
df.read_csv(
    'data.csv',
    sep=',',
    header=0,
    names=['col1', 'col2'],
    dtype={'col1': int},
    parse_dates=['date_column']
)
```

### 3. **Matplotlib Visualization**
Plotting functions use keywords for customization:

```python
plt.plot(
    x, y,
    color='blue',
    linestyle='--',
    linewidth=2,
    marker='o',
    label='Data'
)
```

### 4. **Machine Learning with scikit-learn**
ML models are configured with keyword arguments:

```python
model = RandomForestClassifier(
    n_estimators=100,
    max_depth=10,
    min_samples_split=5,
    random_state=42
)
```

## Challenge Projects

### 1. **Universal Logger**
Create a logging system with extensive keyword arguments.

**Requirements:**
- Required: message
- Keywords: level, timestamp, file, line_number, function_name, color, format
- Support different log levels
- Optional file output
- Colored console output
- Custom formatting

### 2. **Smart Search Function**
Build a search engine with flexible keyword arguments.

**Requirements:**
- Required: query, data
- Keywords: case_sensitive, fuzzy_match, max_results, sort_by, filters
- Support multiple search modes
- Ranking algorithm with keyword params
- Filter by multiple criteria

### 3. **Data Validator**
Create a comprehensive validation function.

**Requirements:**
- Required: data, schema
- Keywords: strict_mode, coerce_types, custom_validators, error_format
- Validate different data types
- Custom error messages
- Optional type coercion
- Nested validation support

### 4. **Template Engine**
Build a template renderer with keyword arguments.

**Requirements:**
- Required: template, context
- Keywords: autoescape, trim_blocks, cache, filters, globals
- Variable substitution
- Control structures
- Custom filters via keywords
- Template inheritance

### 5. **API Client Generator**
Create an API client builder using keyword arguments.

**Requirements:**
- Required: base_url
- Keywords: auth, headers, timeout, retries, verify_ssl, proxies, hooks
- Support different auth methods (passed as keywords)
- Configurable retry logic
- Custom request/response hooks
- Session management

---

## Navigation

- **Previous:** [32. Default Arguments](../32-default-arguments/README.md)
- **Next:** [34. Args and Kwargs](../34-args-kwargs/README.md)
- **[Back to Main README](../README.md)**
