def digits(n):
   count = 0
   if n == 0:
      return 1
   while (n > 0):
      count += 1
      n = n//10
   return count


print(digits(25))
print(digits(144))
print(digits(1000))
print(digits(0))
