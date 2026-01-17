import random

def find_missing(input_list):
    """Find the missing number in the array."""
    # Calculate sum of all elements in input list
    sum_of_elements = sum(input_list)
    # There is exactly 1 number missing
    n = len(input_list) + 1
    actual_sum = (n * (n + 1)) // 2
    return actual_sum - sum_of_elements


def test(n):
    """Test the find_missing function."""
    missing_element = random.randint(1, n)
    v = [i for i in range(1, n + 1) if i != missing_element]
    actual_missing = find_missing(v)
    print(f"Expected Missing = {missing_element}, Actual Missing = {actual_missing}")


if __name__ == "__main__":
    for i in range(1, 10):
        test(100000)