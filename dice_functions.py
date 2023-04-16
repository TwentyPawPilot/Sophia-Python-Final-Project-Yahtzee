import random

"""A set of tools for working with dice in a Yahtzee game
Most, if not all, of these functions have been replaced by the hand class.
This file has been left for debugging and reference."""


def initial_roll():
    """Creates a list containing 5 randomly rolled, six-sided dice."""
    # Sets the blank list
    dice_set = []
    # Rolls the dice 5 times and returns the list to the user
    for num in range(1, 6):
        dice_set.append(random.randint(1, 6))
    return dice_set


def display_dice(dice):
    """Takes a list containing dice and displays it properly to the user."""
    numerals = ["I.)  ", "II.) ", "III.)", "IV.) ", "V.)  "]
    index_num = 0
    for die in dice:
        print(f"{numerals[index_num]}\t{die}")
        index_num += 1


def roll_again(dice, lst):
    """Allows the user to specify which dice to roll again."""
    for spot in lst:
        dice[spot - 1] = random.randint(1, 6)
    return dice
