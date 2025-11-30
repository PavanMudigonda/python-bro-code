# Iterables
# # Iterables = An object/collection that can return its elements one at a time.
#                allowing it to be iterated over in a loop


my_dictionary = { "A": "1", 
                 "B": "2",
                 "C": "3",
                 "D": "4",
                 "E": "5",
                 "F": "6",
                 "G": "7",                                                   
                 }

for key, value in my_dictionary.items():
    print(f'{key} : {value}')