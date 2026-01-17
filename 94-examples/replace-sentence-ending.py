def replace_ending(sentence, old, new):
    # Check if the old string is at the end of the sentence
    if sentence.endswith(old):
        # Using i as the slicing index, combine the part
        # of the sentence up to the matched string at the
        # end with the new string
        i = len(old)
        new_sentence = sentence[:-i]+new
        return new_sentence
    # Return the original sentence if there is no match
    return sentence

print(replace_ending("It's raining cats and cats", "cats", "dogs"))
# Should display "It's raining cats and dogs"

print(replace_ending("She sells seashells by the seashore", "seashells", "donuts"))
# Should display "She sells seashells by the seashore"

print(replace_ending("The weather is nice in May", "may", "april"))
# Should display "The weather is nice in May"

print(replace_ending("The weather is nice in May", "May", "April"))
# Should display "The weather is nice in April
