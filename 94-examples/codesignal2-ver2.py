def firstNotRepeatingCharacter(s):

    for i in range(0,len(s)):
        isRepeatFlag = False
        for j in range(1,len(s)):
            if (s[i] == s[j]) and (i != j):
                isRepeatFlag = True
        if not isRepeatFlag:
            return s[i]
    return '-'

val = firstNotRepeatingCharacter('abacabad')
print(val)