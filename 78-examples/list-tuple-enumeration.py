# Lists

animals=["monkey","donkey","tiger","lion","zebra","camel","fox","dog","cat","mouse"]

print(animals[1])

# Tuples

fruits=("apple","orange","banana","dates","peaches","grapes","pears","apricot","mango","guavue")
char = 0
for animal in animals:
    char += len(animal)
print("Total characters: {}, Average Length {}".format(char,char/len(animals)))


animals1=["monkey","donkey","tiger","lion","zebra","camel","fox","dog","cat","mouse"]
for index, animal in enumerate(animals1):
    print("{} - {}".format(index+1, animal))


