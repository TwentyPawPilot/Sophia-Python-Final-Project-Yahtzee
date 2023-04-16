import hand_class
import input_functions as inp

"""A class to act as the scorecard for the game"""


class Scorecard:
    def __init__(self, name):
        self.player_name = name
        self.ones = ""
        self.played_ones = False
        self.twos = ""
        self.played_twos = False
        self.threes = ""
        self.played_threes = False
        self.fours = ""
        self.played_fours = False
        self.fives = ""
        self.played_fives = False
        self.sixes = ""
        self.played_sixes = False
        self.lower_hand_total = 0
        self.lower_hand_bonus = 0
        self.three_of_a_kind = ""
        self.played_three_of = False
        self.four_of_a_kind = ""
        self.played_four_of = False
        self.full_house = ""
        self.played_full_house = False
        self.small_straight = ""
        self.played_small_straight = False
        self.large_straight = ""
        self.played_large_straight = False
        self.yahtzee_score = ""
        self.chance = ""
        self.played_chance = False
        self.total_score = 0
        self.played_yahtzee = False
        self.bonus_eligible = False
        self.bonus_yahtzees = 0

    def check_lower_hand(self):
        """Checks the lower hand (ones - sixes) to see if the total has earned the 35 point bonus"""
        # All values start as a string for formatting purposes, and are converted to ints for calculations
        self.lower_hand_total = sum([
            inp.blank_to_zero(self.ones), inp.blank_to_zero(self.twos), inp.blank_to_zero(self.threes),
            inp.blank_to_zero(self.fours), inp.blank_to_zero(self.fives), inp.blank_to_zero(self.sixes)
        ])
        # If the lower hand total is 63 or above, the user is awarded 35 bonus points
        if self.lower_hand_total >= 63:
            self.lower_hand_bonus = 35

    def score_ones(self, dice):
        """Used for when a user elects to take the ones in their hand."""
        if self.played_ones:
            print("You have already played a hand in that spot. Select another spot to score.")
            return False
        elif dice.is_yahtzee and self.bonus_eligible:
            # If a yahtzee hs already been played and this hand contains a yahtzee, a 50 point bonus is awarded
            self.bonus_yahtzees += 1
        # Otherwise sum up all ones and add to scorecard
        self.ones = sum(die for die in dice.dice if die == 1)
        self.check_lower_hand()
        self.played_ones = True
        return True

    def score_twos(self, dice):
        """Used for when a user elects to take the twos in their hand."""
        if self.played_twos:
            print("You have already played a hand in that spot. Select another spot to score.")
            return False
        elif dice.is_yahtzee and self.bonus_eligible:
            # If a yahtzee hs already been played and this hand contains a yahtzee, a 50 point bonus is awarded
            self.bonus_yahtzees += 1
        # Otherwise sum up all ones and add to scorecard
        self.twos = sum(die for die in dice.dice if die == 2)
        self.check_lower_hand()
        self.played_twos = True
        return True

    def score_threes(self, dice):
        """Used for when a user elects to take the threes in their hand."""
        if self.played_threes:
            print("You have already played a hand in that spot. Select another spot to score.")
            return False
        elif dice.is_yahtzee and self.bonus_eligible:
            # If a yahtzee hs already been played and this hand contains a yahtzee, a 50 point bonus is awarded
            self.bonus_yahtzees += 1
        # Otherwise sum up all ones and add to scorecard
        self.threes = sum(die for die in dice.dice if die == 3)
        self.check_lower_hand()
        self.played_threes = True
        return True

    def score_fours(self, dice):
        """Used for when a user elects to take the fours in their hand."""
        if self.played_fours:
            print("You have already played a hand in that spot. Select another spot to score.")
            return False
        elif dice.is_yahtzee and self.bonus_eligible:
            # If a yahtzee hs already been played and this hand contains a yahtzee, a 50 point bonus is awarded
            self.bonus_yahtzees += 1
        # Otherwise sum up all ones and add to scorecard
        self.fours = sum(die for die in dice.dice if die == 4)
        self.check_lower_hand()
        self.played_fours = True
        return True

    def score_fives(self, dice):
        """Used for when a user elects to take the fives in their hand."""
        if self.played_fives:
            print("You have already played a hand in that spot. Select another spot to score.")
            return False
        elif dice.is_yahtzee and self.bonus_eligible:
            # If a yahtzee hs already been played and this hand contains a yahtzee, a 50 point bonus is awarded
            self.bonus_yahtzees += 1
        # Otherwise sum up all ones and add to scorecard
        self.fives = sum(die for die in dice.dice if die == 5)
        self.check_lower_hand()
        self.played_fives = True
        return True

    def score_sixes(self, dice):
        """Used for when a user elects to take the sixes in their hand."""
        if self.played_sixes:
            print("You have already played a hand in that spot. Select another spot to score.")
            return False
        elif dice.is_yahtzee and self.bonus_eligible:
            # If a yahtzee hs already been played and this hand contains a yahtzee, a 50 point bonus is awarded
            self.bonus_yahtzees += 1
        # Otherwise sum up all ones and add to scorecard
        self.sixes = sum(die for die in dice.dice if die == 6)
        self.check_lower_hand()
        self.played_sixes = True
        return True

    def score_yahtzee(self, dice):
        """Scores the Yahtzee category and sets the flag for if other hands are eligible for the Yahtzee bonus."""
        if self.played_yahtzee:
            print("You have already played a hand in that spot. Select another spot to score.")
            return False
        elif dice.is_yahtzee:
            self.yahtzee_score = 50
            self.bonus_eligible = True
        else:
            self.yahtzee_score = 0
        self.played_yahtzee = True
        return True

    def score_chance(self, dice):
        """Scores the sum of all dice regardless of hand type"""
        if self.played_chance:
            print("You have already played a hand in that spot. Select another spot to score.")
            return False
        elif dice.is_yahtzee and self.bonus_eligible:
            # If a yahtzee hs already been played and this hand contains a yahtzee, a 50 point bonus is awarded
            self.bonus_yahtzees += 1
        self.chance = sum(dice.dice)
        self.played_chance = True
        return True

    def overall_score(self):
        """Calculates the overall score of the card"""
        # All values start as blank strings for formatting purposes. blank_to_zero converts blanks back to ints of 0
        # for calculation purposes
        self.total_score = inp.blank_to_zero(self.ones) + inp.blank_to_zero(self.twos) + inp.blank_to_zero(self.threes)\
                           + inp.blank_to_zero(self.fours) + inp.blank_to_zero(self.fives)\
                           + inp.blank_to_zero(self.sixes) + inp.blank_to_zero(self.three_of_a_kind)\
                           + inp.blank_to_zero(self.four_of_a_kind) + inp.blank_to_zero(self.full_house) \
                           + inp.blank_to_zero(self.small_straight) + inp.blank_to_zero(self.large_straight)\
                           + inp.blank_to_zero(self.yahtzee_score) + inp.blank_to_zero(self.lower_hand_bonus)\
                           + inp.blank_to_zero(self.chance) + (self.bonus_yahtzees * 50)

    def score_large_straight(self, dice):
        """Scores a flat rate of 40 if the hand contains 5 values in a row"""
        # Only two large straight patterns exist. Sort the dice and check against those two patterns
        dice.dice.sort()
        if self.played_large_straight:
            print("You have already played a hand in that spot. Select another spot to score.")
            return False
        elif dice.is_yahtzee and self.bonus_eligible:
            # If a yahtzee hs already been played and this hand contains a yahtzee, a 50 point bonus is awarded
            self.bonus_yahtzees += 1
        elif dice.dice in [[1, 2, 3, 4, 5], [2, 3, 4, 5, 6]]:
            self.large_straight = 40
        else:
            self.large_straight = 0
        self.played_large_straight = True
        return True

    def score_small_straight(self, dice):
        """Scores a flat rate of 30 if the hand contains 5 values in a row"""
        # Sorts the dice in the hand and records the first 4 and last 4 sets to check for straights
        # Only three small straight patterns exist. If the first 4 or last 4 of the hand
        # do not contain one of the three patterns, no small straight exists.
        dice.dice.sort()
        # Takes the first 4 of the sorted dice
        first_slice = dice.dice[:-1]
        # Takes the last 4 of the sorted dice
        last_slice = dice.dice[1:]
        # Nested list of the 3 small straight patterns, in ascending order
        small_straights = [[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6]]
        if self.played_small_straight:
            print("You have already played a hand in that spot. Select another spot to score.")
            return False
        elif dice.is_yahtzee and self.bonus_eligible:
            # If a yahtzee hs already been played and this hand contains a yahtzee, a 50 point bonus is awarded
            self.bonus_yahtzees += 1
        elif (first_slice in small_straights) or (last_slice in small_straights):
            self.small_straight = 30
        else:
            self.small_straight = 0
        self.played_small_straight = True
        return True

    def score_full_house(self, dice):
        """Determines if the hand contains a full house (one three of a kind and one pair) and awards
        a flat 25 points."""
        # Sorts the dice
        dice.dice.sort()
        # Counts how many times the number on die 1 appears.
        first_count = dice.dice.count(dice.dice[0])
        # Counts how many times the number on die 2 appears.
        last_count = dice.dice.count(dice.dice[-1])
        if self.played_full_house:
            print("You have already played a hand in that spot. Select another spot to score.")
            return False
        elif dice.is_yahtzee and self.bonus_eligible:
            # If a yahtzee hs already been played and this hand contains a yahtzee, a 50 point bonus is awarded
            self.bonus_yahtzees += 1
        # A full house exists if there is a three-of-a-kind and a pair. This checks both possibilities.
        elif (first_count == 3 and last_count == 2) or (first_count == 2 and last_count == 3):
            self.full_house = 25
        else:
            self.full_house = 0
        self.played_full_house = True
        return True

    def score_three_of_a_kind(self, dice):
        """Determines if the hand contains at least three of one die, and then sums the entire hand."""
        # Creates a list to see how many times each number occurs
        counts = [dice.dice.count(dice.dice[num]) for num in range(0, 5)]
        if self.played_three_of:
            print("You have already played a hand in that spot. Select another spot to score.")
            return False
        elif dice.is_yahtzee and self.bonus_eligible:
            # If a yahtzee hs already been played and this hand contains a yahtzee, a 50 point bonus is awarded
            self.bonus_yahtzees += 1
        # if the maximum of the counted list is 3 or more, a three-of-a-kind is allowed. Note, a player
        # may choose to score a (four/five)-of-a-kind in this spot.
        elif max(counts) >= 3:
            self.three_of_a_kind = sum(dice.dice)
        else:
            self.three_of_a_kind = 0
        self.played_three_of = True
        return True

    def score_four_of_a_kind(self, dice):
        """Determines if the hand contains at least four of one die, and then sums the entire hand."""
        # Creates a list to see how many times each number occurs
        counts = [dice.dice.count(dice.dice[num]) for num in range(0, 5)]
        if self.played_four_of:
            print("You have already played a hand in that spot. Select another spot to score.")
            return False
        elif dice.is_yahtzee and self.bonus_eligible:
            # If a yahtzee hs already been played and this hand contains a yahtzee, a 50 point bonus is awarded
            self.bonus_yahtzees += 1
        # if the maximum of the counted list is 4 or more, a four-of-a-kind is allowed. Note, a player
        # may choose to score a five-of-a-kind in this spot.
        elif max(counts) >= 4:
            self.four_of_a_kind = sum(dice.dice)
        else:
            self.four_of_a_kind = 0
        self.played_four_of = True
        return True

    def show_scorecard_original_method(self):
        """Used to display the scorecard to the player. Depreciated but left for prototyping."""
        self.overall_score()
        print(f"""
        ----------------------------------------------
        |ONES:        {self.ones}\t\t\tTHREE OF A KIND:  {self.three_of_a_kind}  |
        |TWOS:        {self.twos}\t\t\tFOUR OF A KIND:   {self.four_of_a_kind}  |
        |THREES:      {self.threes}\t\t\tFULL HOUSE:       {self.full_house}  |
        |FOURS:       {self.fours}\t\t\tSMALL STRAIGHT:   {self.small_straight}  |
        |FIVES:       {self.fives}\t\t\tLARGE STRAIGHT:   {self.large_straight}  |
        |SIXES:       {self.sixes}\t\t\tYAHTZEE:          {self.yahtzee_score}  |
        |LOWER TOTAL: {self.lower_hand_total}\t\t\tCHANCE:           {self.chance}  |
        |LOWER BONUS: {self.lower_hand_bonus}\t\t\tTOTAL SCORE:      {self.total_score}  |
        ----------------------------------------------
        """)

    def show_scorecard_new_method(self):
        """A method for displaying the scorecard with better visuals and formatting"""
        # Calculates the total score each time it is called to display the card
        self.overall_score()
        # Various print statements to properly pad each line for aesthetics.
        print("-" * 60)
        print(f"{self.player_name}'s Card".center(55, " "))
        print("| A) ONES:".ljust(20, " ") + f"{self.ones}".rjust(3, " ") + "\t\t\t" +
              "G) THREE OF A KIND:".ljust(20, " ") + f"{self.three_of_a_kind}".rjust(3, " ") + " |")
        print("| B) TWOS:".ljust(20, " ") + f"{self.twos}".rjust(3, " ") + "\t\t\t" +
              "H) FOUR OF A KIND:".ljust(20, " ") + f"{self.four_of_a_kind}".rjust(3, " ") + " |")
        print("| C) THREES:".ljust(20, " ") + f"{self.threes}".rjust(3, " ") + "\t\t\t" +
              "I) FULL HOUSE:".ljust(20, " ") + f"{self.full_house}".rjust(3, " ") + " |")
        print("| D) FOURS:".ljust(20, " ") + f"{self.fours}".rjust(3, " ") + "\t\t\t" +
              "J) SMALL STRAIGHT:".ljust(20, " ") + f"{self.small_straight}".rjust(3, " ") + " |")
        print("| E) FIVES:".ljust(20, " ") + f"{self.fives}".rjust(3, " ") + "\t\t\t" +
              "K) LARGE STRAIGHT:".ljust(20, " ") + f"{self.large_straight}".rjust(3, " ") + " |")
        print("| F) SIXES:".ljust(20, " ") + f"{self.sixes}".rjust(3, " ") + "\t\t\t" +
              "L) YAHTZEE:".ljust(20, " ") + f"{self.yahtzee_score}".rjust(3, " ") + " |")
        print("| LOWER TOTAL:".ljust(20, " ") + f"{self.lower_hand_total}".rjust(3, " ") + "\t\t\t" +
              "M) CHANCE:".ljust(20, " ") + f"{self.chance}".rjust(3, " ") + " |")
        print("| LOWER BONUS:".ljust(20, " ") + f"{self.lower_hand_bonus}".rjust(3, " ") + "\t\t\t" +
              "YAHTZEE BONUS:".ljust(20, " ") + f"{self.bonus_yahtzees * 50}".rjust(3, " ") + " |")
        print("-" * 60)
        print(f"TOTAL SCORE: {self.total_score}".center(55, " "))
