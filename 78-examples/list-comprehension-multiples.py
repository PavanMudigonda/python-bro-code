multiples=[]
for x in range(1,11):
    multiples.append(x*7)

print(multiples)

# Lists Comprehension

multiples=[x*7 for x in range(1, 11)]
print(multiples)


even=[x*2 for x in range(1, 20)]
print(even)


odd=[x+2 for x in range(1,20)]

print(odd)


languages=['pearl','python','java','ruby','go','C#']

length=[len(language) for language in languages ]

print(length)

z = [x for x in range(1,101) if x % 3 == 0]
print(z)
