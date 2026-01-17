def firstDuplicate(a):
    seen = set()
    for item in a:
        if item in seen:
            return item
        seen.add(item)
    return -1


val = firstDuplicate([2, 1, 3, 5, 3, 2])
print(val)