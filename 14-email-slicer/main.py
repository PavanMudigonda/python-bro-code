# Email Slicer Program
# Extract username and domain from email address

email = input("Enter your email: ").strip()

# Check if email contains @
if "@" in email and email.count("@") == 1:
    # Find the position of @
    at_index = email.find("@")
    
    # Extract username (before @)
    username = email[:at_index]
    
    # Extract domain (after @)
    domain = email[at_index + 1:]
    
    # Check if both username and domain exist
    if username and domain:
        print(f"\n✅ Email Analysis:")
        print(f"   Username: {username}")
        print(f"   Domain: {domain}")
        
        # Bonus: Identify domain type
        if domain.endswith(".com"):
            print(f"   Type: Commercial")
        elif domain.endswith(".edu"):
            print(f"   Type: Educational")
        elif domain.endswith(".gov"):
            print(f"   Type: Government")
        elif domain.endswith(".org"):
            print(f"   Type: Organization")
    else:
        print("❌ Invalid email format - missing username or domain!")
else:
    print("❌ Invalid email format - email must contain exactly one @ symbol!")
