def count_letters(text):
    result={}
    for letter in text:
        if letter not in result:
            result[letter] = 0
        result[letter] += 1
        return result
        print(result)

count_letters("tenant")



