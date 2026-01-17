def reverse_sentence(sentence):
    words = sentence.split(' ')
    reversed_sentence= ' '.join(reversed(words))
    return reversed_sentence


s=reverse_sentence('Hello World!')
print(s)