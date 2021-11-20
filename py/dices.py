import random


def roll(dice_value):
    '''
    Simulate roling dices by returning random numbers between 1 and 4, 6, 8, 10, 20, 100, other values are excluded.
    '''
    dices = [4, 6, 8, 10, 20, 100]

    if dice_value in dices:
        dice_result = random.randint(1, dice_value)
    else:
        print('Enter a valid number: (4, 6, 8, 10, 20, 100)')
    return dice_result


rand = roll(20)

print(f'1d{str(rand)}')
