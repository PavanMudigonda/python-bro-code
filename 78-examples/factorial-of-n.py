def factorial(n):
    result = 1
    for x in range(1,n+1):
        result = result * x
    print(result)

factorial(8)

#for n in range(0,9):
#    print(n, factorial(n))


def factorial(n):
    result = 1
    for x in range(1,n+1):
        result = result * x
    return result

for n in range(0,9):
    print(n, factorial(n))
