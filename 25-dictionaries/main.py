# ============================================
# CHAPTER 25: DICTIONARIES
# ============================================
# Dictionaries store data as key:value pairs
# - Ordered (as of Python 3.7+)
# - Changeable (mutable)
# - No duplicate keys allowed
# - Fast lookup by key
#
# Key Concepts:
# - Keys must be immutable (strings, numbers, tuples)
# - Values can be any data type
# - Efficient for lookups, insertions, and deletions
# - Similar to hash maps or associative arrays in other languages

# =============================================
# CREATE A DICTIONARY
# =============================================
# Dictionary syntax: {key1: value1, key2: value2, ...}
# Here, country names are keys, capitals are values
capitals = {"USA": "Washington D.C",
            "China": "Beijing",
            "India": "New Delhi",
            "Canada": "Ottawa",
            "Russia": "Moscow"
            }

# =============================================
# EXPLORE DICTIONARY METHODS
# =============================================
# Uncomment these to see all available dictionary methods and help
# print(dir(capitals))   # Lists all methods and attributes
# print(help(capitals))  # Shows detailed documentation

# =============================================
# ACCESSING VALUES
# =============================================
# get() method safely retrieves values by key
# Returns None if key doesn't exist (instead of raising an error)
# print(capitals.get("Canada"))  # Output: Ottawa

# =============================================
# UPDATING DICTIONARIES
# =============================================
# update() method adds new key-value pairs or updates existing ones
# Can pass a dictionary to update multiple entries at once
capitals.update({"Germany": "Berlin"})

# =============================================
# VERIFY THE UPDATE
# =============================================
# Retrieve the newly added entry
print(capitals.get("Germany"))  # Output: Berlin