import random

dice_dict = {'bet': '', 'balance': 100, 'dice_one': 0, 'dice_two': 0, 'goal': 0, 'num_of_rolls': 0, 'result': ''}
dice_dict['bet'] = input("Enter your bet between $0 and ${}:".format(dice_dict['balance']))
dice_dict['bet'] = int(dice_dict['bet'].replace('$', ''))
if dice_dict['bet'] > 100 or dice_dict['bet'] < 0:
    print("please enter bet amount between 100 dollars and greater than zero dollars ")
else:
    # First Roll of the two dices
    dice_dict['dice_one'] = random.randint(1, 7)
    dice_dict['dice_two'] = random.randint(1, 7)
    dice_sum = dice_dict['dice_one'] + dice_dict['dice_two']
    # First roll related logic
    if dice_dict['balance'] >= dice_dict['bet']:
        if dice_sum == 2 or dice_sum == 3 or dice_sum == 12:
            print("{},{}".format(dice_dict['dice_one'], dice_dict['dice_two']))
            dice_dict['result'] = 'You Lost'
            dice_dict['balance'] -= dice_dict['bet']
            dice_dict['num_of_rolls'] += 1
        elif dice_sum == 7 or dice_sum == 11:
            print("{},{}".format(dice_dict['dice_one'], dice_dict['dice_two']))
            dice_dict['result'] = 'You Won!'
            dice_dict['balance'] += dice_dict['bet']
        else:
            print("{},{}".format(dice_dict['dice_one'], dice_dict['dice_two']))
            dice_dict['goal'] = dice_sum
            dice_dict['num_of_rolls'] += 1
            # Subsequent Rolls related logic
            while dice_dict['balance'] >= dice_dict['bet'] and dice_dict['num_of_rolls'] > 0:
                # Throwing dice again
                dice_dict['dice_one'] = random.randint(1, 7)
                dice_dict['dice_two'] = random.randint(1, 7)
                print("{},{}".format(dice_dict['dice_one'], dice_dict['dice_two']))
                dice_sum = dice_dict['dice_one'] + dice_dict['dice_two']
                if dice_dict['goal'] == dice_sum and dice_sum != 7:
                    print("{},{}".format(dice_dict['dice_one'], dice_dict['dice_two']))
                    dice_dict['result'] = 'You Won!'
                    dice_dict['balance'] += dice_dict['bet']
                    dice_dict['num_of_rolls'] += 1
                    break
                elif dice_sum == 7:
                    print("{},{}".format(dice_dict['dice_one'], dice_dict['dice_two']))
                    dice_dict['balance'] -= dice_dict['bet']
                    dice_dict['result'] = 'You Lost.'
                    dice_dict['num_of_rolls'] += 1
                    continue
                else:
                    print("{},{}".format(dice_dict['dice_one'], dice_dict['dice_two']))
                    dice_dict['num_of_rolls'] += 1
                    continue
print(dice_dict['result'])
