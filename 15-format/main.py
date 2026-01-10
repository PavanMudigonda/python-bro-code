# ============================================
# Chapter 15: Format Specifiers
# ============================================
# Format specifiers = {:flags} format a value based on flags
# Used with f-strings to control how values are displayed

# ============================================
# Common Format Specifiers:
# ============================================
# :.2f  → Round to 2 decimal places (fixed-point)
# :10   → Allocate 10 spaces (right-aligned by default)
# :>10  → Right justify within 10 spaces
# :<10  → Left justify within 10 spaces
# :^10  → Center align within 10 spaces
# :03   → Zero-pad to width 3
# :+    → Show + for positive numbers
# :=    → Place sign at leftmost position
# :     → Insert space before positive numbers
# :,    → Add comma as thousands separator

# Sample prices for demonstration
price1 = 3.234443
price2 = 4.234443
price3 = 5.234443
price4 = 1234567.234443

# ============================================
# Example 1: Decimal Places
# ============================================
# :.2f rounds to 2 decimal places
print(f'Price 1: $ {price1:.2f}')  # Output: $ 3.23

# ============================================
# Example 2: Right Justification
# ============================================
# :>10 allocates 10 spaces and right-aligns the number
print(f'Price 1 - right justified: $ {price1:>10}')  # spaces before number

# ============================================
# Example 3: Left Justification
# ============================================
# :<10 allocates 10 spaces and left-aligns the number
print(f'Price 1 - left justified: $ {price1:<10}')  # spaces after number

# ============================================
# Example 4: Thousands Separator
# ============================================
# :, adds commas every 3 digits
print(f'Price 4 with comma: $ {price4:,}')  # Output: $ 1,234,567.234443

# ============================================
# Example 5: Combined Formatting
# ============================================
# :,.2f combines comma separator with 2 decimal places
print(f'Price 4 with comma & 2 decimals: $ {price4:,.2f}')  # Output: $ 1,234,567.23

# ============================================
# Additional Format Examples:
# ============================================
# number = 42
# print(f'{number:05}')   # Output: 00042 (zero-padded to 5 digits)
# print(f'{number:+}')    # Output: +42 (show + sign)
# print(f'{number:^10}')  # Output: '    42    ' (centered in 10 spaces)

# percentage = 0.756
# print(f'{percentage:.1%}')  # Output: 75.6% (as percentage with 1 decimal)
