
print("Welcome to rock Paper scissors")

player1_input = input("Player 1 - please select your hend: S for scissors, R for rock and P for paper (capital letters) ")
if (player1_input != 'S' and player1_input != 'R' and player1_input != 'P'):
    print("This is a bad input. Exiting")
    exit()

player2_input = input("Player 2 - please select your hend: S for scissors, R for rock and P for paper (capital letters) ")
if (player2_input != 'S' and player2_input != 'R' and player2_input != 'P'):
    print("This is a bad input. Exiting")
    exit()

# Tie condition
if player1_input == player2_input:
    print("It's a tie!!!")


# All 6 winning conditions
if player1_input == 'S' and player2_input == 'P':
    print("Player 1 wins!!!")

if player1_input == 'P' and player2_input == 'R':
    print("Player 1 wins!!!")

if player1_input == 'R' and player2_input == 'S':
    print("Player 1 wins!!!")

# actually, Now I know for sure that the second player has won. Do you understand why?
print("Player 2 wins!!!")


