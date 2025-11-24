# format specifers = {:flags} format a value based on what
#                             flags are inserted

# :.2f → Round to 2 decimal places (fixed-point notation).
# :10 → Allocate 10 spaces (default is right-aligned).
# :>10 → Right justify within 10 spaces.
# :<10 → Left justify within 10 spaces.
# :^10 → Center align within 10 spaces.
# :03 → Zero-pad to width 3.
# :+ → Show + for positive numbers.
# := → Place sign at the leftmost position.
# :  → Insert a space before positive numbers.
# : , → Add comma as thousands separator.

price1 = 3.234443
price2 = 4.234443
price3 = 5.234443
price4 = 1234567.234443

print(f'Price 1: $ {price1:.2f}')        # $ 3.23 (rounded to 2 decimals)
print(f'Price 1 - right justified: $ {price1:>10}')  # spaces before number
print(f'Price 1 - left justified: $ {price1:<10}')   # spaces after number
print(f'Price 4 with comma: $ {price4:,}')           # $ 1,234,567.234443
print(f'Price 4 with comma & 2 decimals: $ {price4:,.2f}') # $ 1,234,567.23
