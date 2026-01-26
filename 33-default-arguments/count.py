# default arguments = A default value for certain parameters
#                     default is used when that argument is omitted
#                     make your functions more flexible, reduce # of arguments
#                     1. positional, 2. DEFAULT, 3. keyword, 4. arbitrary


import time

def count(end, start=0):
    for x in range(start,end+1):
        print(x)
        time.sleep(1)
    print("DONE")

count(30,10)

        