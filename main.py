import input_functions as inp

# Welcomes the player and initiates the game.
print("Welcome to Yahtzee!")
# Generates a scorecard for each player entered
players = inp.new_players()
if len(players) == 0:
    print("No players were detected. Please try again!")

# Loop 13 times for the 13 categories a player may pick
for turn in range(13):
    # Each player gets a turn
    for player in players:
        print(f"It's now {player.player_name}'s turn! Good luck!")
        player.show_scorecard_new_method()
        # Rolls 5 dice and allows the player to reroll their hand up to three times total.
        current_hand = inp.take_turn()
        player.show_scorecard_new_method()
        print("Here is your hand and scorecard. Please pick where to take your points.")
        # User is provided with their scorecard and asked where they want to allocate points
        # The user may not allocate points to a category more than once per game
        while 1:
            option = input(f"{current_hand.dice}\n")
            success = inp.take_score(player, current_hand, option)
            if success:
                break
# The final score(s) are printed and a winner declared.
print("The game is now over. Here are the results!")
for player in players:
    player.show_scorecard_new_method()
final_scores = [player.total_score for player in players]
winning_score = max(final_scores)
winner = players[final_scores.index(winning_score)]
for player in players:
    print(f"{player.player_name}'s total is: {player.total_score}")
print(f"Congrats, {winner.player_name}!!!")
