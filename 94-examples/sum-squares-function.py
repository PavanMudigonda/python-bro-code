def square(n):
    return n*n

def sum_squares(x):
    sum = 0
    for n in range (0, x):
        sum += square(n)
    return sum

print(sum_squares(10)) # Should be 285


