from collections import Counter
from string import ascii_letters
def count_letters(s) :
    filtered = [c for c in s.lower() if c in ascii_letters]
    return Counter(filtered)
count_letters('Math is fun! 2+2=4')
