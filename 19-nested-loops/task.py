rows = int(input("enter the number of rows: "))

columns = int(input("enter the number of columns: "))

symbol = str(input("enter the symbol to use: "))

for x in range(rows):
    for y in range(columns):
        print(symbol,end="")
    print("\n")
