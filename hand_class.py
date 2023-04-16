import random

"""A class to handle working with a 'hand' of 5 dice"""


class Hand:
    def __init__(self):
        self.dice = [random.randint(1, 6) for die in range(5)]
        self.roll_count = 1
        self.is_yahtzee = self.check_yahtzee()

    def show_hand(self):
        """Displays the hand to the user"""
        print("---")
        num = 1
        for die in self.dice:
            print(f"Die #{num} -->  {die}")
            num += 1
        print("---")
        print(f"This is roll #{self.roll_count} of 3")

    def roll_again(self, indices):
        """Used to allow the user to roll specific dice from their hand again, up to 3 times total"""
        # Ensures a max of three rerolls
        if self.roll_count >= 3:
            print("You have reached your roll limit for this hand.")
        else:
            for index in indices:
                self.dice[index] = random.randint(1, 6)
        self.roll_count += 1
        # Checks to see if the hand constitutes a "Yahtzee!" or 5-of-a-kind
        self.is_yahtzee = self.check_yahtzee()

    def check_yahtzee(self):
        """Determines if the hand contains a 5 of a kind (AKA a 'Yahtzee!')"""
        possible_yahtzees = [[1, 1, 1, 1, 1],
                             [2, 2, 2, 2, 2],
                             [3, 3, 3, 3, 3],
                             [4, 4, 4, 4, 4],
                             [5, 5, 5, 5, 5],
                             [6, 6, 6, 6, 6]]
        if self.dice in possible_yahtzees:
            self.is_yahtzee = True
            return True
        else:
            self.is_yahtzee = False
            return False
