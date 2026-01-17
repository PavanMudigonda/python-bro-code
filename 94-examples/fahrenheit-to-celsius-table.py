def to_celsius(x):
    return (x-32)*5/9

for x in range(0,101,10):
    print("{:>5} F | {:>10.2f} C".format(x,to_celsius(x)))
