def reverse_words(sentence):
    # first split the string into words
    words = sentence.split(' ')
    print(words)
    # then reverse the split string list and join using space
    reverse_sentence = ' '.join(reversed(words))

    # finally return the joined string
    return reverse_sentence


s = reverse_words('Hello World!')
print(s)