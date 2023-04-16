import hand_class as hand
import scorecard_class as card

"""Set of functions designed to ensure all inputs are proper for the Yahtzee game"""


def get_dice_to_reroll():
    """Prompts the user to ask which dice they want to keep in their hand, and returns
    a list containing the dice indices. Ensures integer inputs.
    A result of 0 indicates no dice will be rerolled, otherwise a list of dice indices to reroll will
    be returned."""
    keepers = input("Enter the number of the dice you want to keep in your hand. "
                    "Separate the values with a comma ',' or enter 0 to proceed to scoring\n")
    # Continues indefinitely until given a set of proper inputs.
    while 1:
        restart = False
        if keepers == "0":
            return 0
        if len(keepers) == 0:  # Empty string error
            keepers = input("Oops. Seems like you hit enter by mistake. Try again\n")
            continue
        # Removes all spaces, commas, and repeated inputs
        keepers = keepers.replace(" ", "")
        keepers = keepers.replace(",", "")
        keepers = list(set(keepers))
        # Check to make sure only numbers 1-5 were entered. If anything else is detected, the loop will restart
        for val in keepers:
            if val not in "12345":
                keepers = input("You entered an invalid choice. Please select again.\n")
                restart = True
                break
        if restart:
            continue
        # Remove the selected elements from indices 0-4
        indices = [0, 1, 2, 3, 4]
        for val in keepers:
            indices.remove(int(val) - 1)
        # Returns a list that only contains the indices of the dice to be rerolled.
        return indices


def take_turn():
    """Executes a full 3 roll turn for one player and returns the hand object for scoring"""
    # New hand object of 5 dice
    dice = hand.Hand()
    # Rerolls only if the user elects to, up to three times total including original roll.
    while dice.roll_count < 3:
        # Shows the user the hand at each roll and asks if a reroll is desired
        dice.show_hand()
        indices = get_dice_to_reroll()
        if indices == 0:
            # No dice selected, go directly to scoring
            break
        else:
            # New dice have been rolled, repeat until complete
            dice.roll_again(indices)
    print("Time to score your hand!")
    return dice


def blank_to_zero(str):
    """Used exclusively by the scorecard to determine if a blank value needs to be turned into a zero
    for scoring purposes"""
    if str == "":
        return int(0)
    else:
        return str


def new_players():
    """Function to automatically generate new players at the start of a game."""
    players = []
    # Allows the user to input as many players as they desire.
    while 1:
        name = input("Please enter the name of the next player. Enter 0 when all players have been entered: \n")
        if name == "0":
            break
        else:
            # Creates a scorecard object for each player
            players.append(card.Scorecard(name))
    return players


def take_score(scorecard, dice, choice):
    """Allows the user to choose which category they are taking for points. Returns True if scoring was
    successful, or false if there was an error or the category had already been selected in previous turn."""
    # Simple switch case for selecting which category to allocate points.
    success = False
    match choice.upper():
        case "A":
            success = scorecard.score_ones(dice)
        case "B":
            success = scorecard.score_twos(dice)
        case "C":
            success = scorecard.score_threes(dice)
        case "D":
            success = scorecard.score_fours(dice)
        case "E":
            success = scorecard.score_fives(dice)
        case "F":
            success = scorecard.score_sixes(dice)
        case "G":
            success = scorecard.score_three_of_a_kind(dice)
        case "H":
            success = scorecard.score_four_of_a_kind(dice)
        case "I":
            success = scorecard.score_full_house(dice)
        case "J":
            success = scorecard.score_small_straight(dice)
        case "K":
            success = scorecard.score_large_straight(dice)
        case "L":
            success = scorecard.score_yahtzee(dice)
        case "M":
            success = scorecard.score_chance(dice)
        case _:
            print("You've entered an invalid choice. Try again.")
            success = False
    return success
