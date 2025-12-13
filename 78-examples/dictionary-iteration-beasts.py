cool_beasts = {"octopuses":"tentacles", "dolphins":"fins", "rhinos":"horns"}
for item in cool_beasts.items():
    key,value = item
    print("{} have {}".format(key,value))
