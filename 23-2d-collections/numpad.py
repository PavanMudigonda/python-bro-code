num_pad = (
    (7, 8, 9),
    (4, 5, 6),
    (1, 2, 3),
    ("*",0,"#")
)

for x in num_pad:
    for y in x:
        print(y, end=" ")
    print()