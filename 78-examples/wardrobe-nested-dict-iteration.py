wardrobe = {"shirt":["red","blue","white"], "jeans":["blue","black"]}
for key, value in wardrobe.items():
    for i in value:
        print("{} {}".format(i, key))
