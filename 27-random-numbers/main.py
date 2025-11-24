import random

# low = 1
# high = 100
# number = random.randint(low, high)

# number = random.random()

# print(number)

options = ["rock", "paper", "scissors"]

cards = ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]
option = random.choice(options)
print(option)
random.shuffle(cards)
print(cards)