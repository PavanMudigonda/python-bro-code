word = "supercalifragilisticexpialidocious"
for position in range(len(word)):
    if word[position] == "x":
        print(position)
    else:
            position+=position
