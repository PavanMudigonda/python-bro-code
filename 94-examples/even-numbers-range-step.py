def even_numbers(maximum):
    return_string = ""
    for x in range(2, maximum + 1, 2):
        return_string += str(x) + " "
    return return_string.strip()


print(even_numbers(10)) # Should be 2 4 6 8 10

