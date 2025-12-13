# String formatting examples

# Format with named variables
# "{var1} {var2}".format(var1=value1, var2=value2)

# Format with positional arguments
# "{:exp1} {:exp2}".format(value1, value2)

# Example: Integer formatting
# Note: {:d} requires an integer value
# '{:d}'.format(10)  # Correct - converts float to int first
result = '{:d}'.format(int(10.5))
print(result)  # Output: 10

# Alternative: use with actual integer
result2 = '{:d}'.format(10)
print(result2)  # Output: 10
