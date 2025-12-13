# Determine if the sum of two integers is equal to the given value
def find_sum_of_two(A, val):
    found_in_array = set()
    for item in A:
        diff = val - item
        if diff in found_in_array:
            return True
        found_in_array.add(item)
    return False

# Test the function
result = find_sum_of_two([2, 1, 8, 4, 7, 3], 3)
print(result)