[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/PavanMudigondaTR/python-bro-code/blob/main/14-email-slicer/14-email-slicer.ipynb) [![Kaggle](https://kaggle.com/static/images/open-in-kaggle.svg)](https://kaggle.com/kernels/welcome?src=https://raw.githubusercontent.com/PavanMudigondaTR/python-bro-code/main/14-email-slicer/14-email-slicer.ipynb)

# Chapter 14: Email Slicer Program

## 📺 Video Tutorial

**Python email slicer program 📧** (4:07)

[![Watch on YouTube](https://img.shields.io/badge/Watch-YouTube-red?style=for-the-badge&logo=youtube)](https://youtu.be/6MAufQ6vGtI)

## 📚 What You'll Learn
Extract username and domain from email addresses using string slicing - a practical application of string indexing!

## 🎯 Learning Objectives
- Apply string indexing to extract specific parts of strings
- Use the `find()` method to locate characters
- Split email addresses into username and domain
- Work with string slicing in real-world scenarios
- Create interactive programs with user input

## 📖 Concept Explanation

### Email Structure
An email address has two main parts separated by '@':
- **Username**: The part before '@' (e.g., "john.doe")
- **Domain**: The part after '@' (e.g., "example.com")

Example: `john.doe@example.com`
- Username: john.doe
- Domain: example.com

### Finding the @ Symbol
Use the `find()` method to locate the position of '@':
```python
email = "john.doe@example.com"
at_index = email.find("@")  # Returns 8
```

### Extracting Username
Use slicing from the start to the @ position:
```python
username = email[:at_index]  # Gets "john.doe"
```

### Extracting Domain
Use slicing from after @ to the end:
```python
domain = email[at_index + 1:]  # Gets "example.com"
```

## 💡 Examples

### Basic Email Slicer
```python
email = input("Enter your email: ")

# Find the @ symbol
at_index = email.find("@")

# Extract username and domain
username = email[:at_index]
domain = email[at_index + 1:]

print(f"Username: {username}")
print(f"Domain: {domain}")
```

**Output:**
```
Enter your email: alice@company.com
Username: alice
Domain: company.com
```

### With Error Handling
```python
email = input("Enter your email: ")

if "@" in email:
    at_index = email.find("@")
    username = email[:at_index]
    domain = email[at_index + 1:]
    
    print(f"Username: {username}")
    print(f"Domain: {domain}")
else:
    print("Invalid email format!")
```

### Enhanced Version
```python
email = input("Enter your email: ").strip()

if "@" in email and email.count("@") == 1:
    at_index = email.find("@")
    username = email[:at_index]
    domain = email[at_index + 1:]
    
    if username and domain:
        print(f"\n✅ Email Analysis:")
        print(f"   Username: {username}")
        print(f"   Domain: {domain}")
    else:
        print("❌ Invalid email format!")
else:
    print("❌ Email must contain exactly one @ symbol!")
```

## ✍️ Practice Exercises

### Exercise 1: Basic Slicer
Create a program that:
1. Prompts user for an email
2. Extracts and displays username
3. Extracts and displays domain

### Exercise 2: Domain Type Checker
Extend the program to identify the domain type:
- .com → Commercial
- .edu → Educational
- .gov → Government
- .org → Organization

```python
email = input("Enter your email: ")
at_index = email.find("@")
domain = email[at_index + 1:]

if domain.endswith(".com"):
    print("Commercial domain")
elif domain.endswith(".edu"):
    print("Educational domain")
# Add more...
```

### Exercise 3: Multiple Emails
Process multiple emails from a list:
```python
emails = [
    "john@company.com",
    "alice@school.edu",
    "bob@government.gov"
]

for email in emails:
    at_index = email.find("@")
    username = email[:at_index]
    domain = email[at_index + 1:]
    print(f"{email} → User: {username}, Domain: {domain}")
```

## 🔍 Common Mistakes

### 1. Forgetting to Add 1
```python
# ❌ Wrong - includes the @ symbol
domain = email[at_index:]

# ✅ Correct
domain = email[at_index + 1:]
```

### 2. Not Checking if @ Exists
```python
# ❌ Wrong - crashes if no @
at_index = email.find("@")
username = email[:at_index]

# ✅ Correct
if "@" in email:
    at_index = email.find("@")
    username = email[:at_index]
```

### 3. Multiple @ Symbols
```python
# Better to validate
if email.count("@") == 1:
    # Process email
else:
    print("Invalid email!")
```

## 🎮 Real-World Applications

1. **Email Validation**: Check if email format is correct
2. **User Registration**: Extract username for display
3. **Email Sorting**: Group emails by domain
4. **Spam Detection**: Analyze domain patterns
5. **Contact Management**: Organize contacts by email provider

## 🚀 Challenge Projects

### Challenge 1: Email Statistics
Create a program that analyzes a list of emails and shows:
- Most common domain
- List of all unique domains
- Number of emails per domain

### Challenge 2: Email Formatter
Convert emails to different formats:
- Original: john.doe@company.com
- Display name: John Doe (john.doe@company.com)
- Masked: j***e@company.com

### Challenge 3: Professional Email Generator
Generate professional emails from names:
```python
first_name = "John"
last_name = "Doe"
company = "techcorp"

# Generate: john.doe@techcorp.com
email = f"{first_name.lower()}.{last_name.lower()}@{company}.com"
```

## 📝 Key Takeaways

- Email structure: `username@domain`
- Use `find()` to locate the @ symbol
- Slice before @ for username: `email[:at_index]`
- Slice after @ for domain: `email[at_index + 1:]`
- Always validate email format before processing
- String slicing is powerful for text processing

## 🎓 Key Takeaways from Video

1. Variables store data values that can be reused
2. Test your code to ensure it works correctly
3. Follow along with the video for hands-on practice

> 💡 *These points cover the main concepts from the video tutorial to help reinforce your learning.*

## 🔗 Next Chapter

Continue to [Chapter 15: Format Specifiers](../15-format/) to learn advanced string formatting!

---

**Practice Tip:** Try extending this to validate email formats more thoroughly - check for valid characters, proper domain structure, etc!

