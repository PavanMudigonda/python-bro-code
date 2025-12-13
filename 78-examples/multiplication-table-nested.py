def multiplication_table(start, stop):
    for x in range(start,stop+1):
        for y in range(start,stop+1):
            print(str(x*y), end=" ")
        print()
multiplication_table(1, 3)
