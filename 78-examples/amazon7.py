# String segmentation
def can_segment_string(s, dictionary):
    for i in range(1, len(s) + 1):
        first = s[:i]
        if first in dictionary:
            second = s[i:]
            if not second or second in dictionary or can_segment_string(second, dictionary):
                return True
    return False


# Test the function
result = can_segment_string('hellonow', set(["hello", "hell", "on", "now"]))
print(result)