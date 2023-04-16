"""A set of methods used to properly score a Yahtzee game.
Most, if not, all of these functions have been rolled (pun intended) into the scorecard class but left here for
debugging and reference"""


def score_ones(dice):
    """Used for when a user elects to take the ones in their hand."""
    return sum(die for die in dice if die == 1)


def score_twos(dice):
    """Used for when a user elects to take the twos in their hand."""
    return sum(die for die in dice if die == 2)


def score_threes(dice):
    """Used for when a user elects to take the threes in their hand."""
    return sum(die for die in dice if die == 3)


def score_fours(dice):
    """Used for when a user elects to take the fours in their hand."""
    return sum(die for die in dice if die == 4)


def score_fives(dice):
    """Used for when a user elects to take the fives in their hand."""
    return sum(die for die in dice if die == 5)


def score_sixes(dice):
    """Used for when a user elects to take the sixes in their hand."""
    return sum(die for die in dice if die == 6)


def score_yahtzee(dice):
    """Used to determine if the player has achieved a yahtzee."""
    # Placeholder variable assumes there is a Yahtzee
    is_yahtzee = True
    # Sets a placeholder die equal to the first die in the hand
    placeholder = dice[0]
    for die in dice:
        if placeholder != die:
            is_yahtzee = False
            break
        else:
            placeholder = die
    return is_yahtzee
