# dictionary = a collection of {key:value} pairs
#              ordered and changeable. No duplicates

capitals = {"USA": "Washington D.C",
            "China": "Beijing",
            "India": "New Delhi",
            "Canada": "Ottawa",
            "Russia": "Moscow"
            }

# print(dir(capitals))
# print(help(capitals))

# print(capitals.get("Canada"))

capitals.update({"Germany": "Berlin"})

print(capitals.get("Germany"))