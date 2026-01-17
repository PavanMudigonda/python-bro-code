# first non occurrence of char

def firstNotRepeatingCharacter(s):
    for char in s:
        if s.index(char)== s.rindex(char):
            return char
    return '_'


val = firstNotRepeatingCharacter('abacabad')
print(val)