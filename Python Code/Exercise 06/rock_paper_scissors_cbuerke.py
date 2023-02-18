"""
Author: Cameron Buerke, cbuerke@purdue.edu
Assignment: 06.2 - Rock Paper Scissors
Date: 10/07/2022

Description:
    This program plays rock paper scissors with the user.

Contributors:
    Name, login@purdue.edu [repeat for each]

My contributor(s) helped me:
    [ ] understand the assignment expectations without
        telling me how they will approach it.
    [ ] understand different ways to think about a solution
        without helping me plan my solution.
    [ ] think through the meaning of a specific error or
        bug present in my code without looking at my code.
    Note that if you helped somebody else with their code, you
    have to list that person as a contributor.

Academic Integrity Statement:
    I have not used source code obtained from any unauthorized
    source, either modified or unmodified; nor have I provided
    another student access to my code.  The project I am
    submitting is my own original work.
"""

"""Import additional modules below this line (starting with unit 6)."""
import random as r

"""Write new functions below this line (starting with unit 4)."""
def get_computer_choice():
    num = r.randint(0,2)
    if num == 0:
        choice = "rock"
    elif num == 1:
        choice = "paper"
    else:
        choice = "scissors"

    return choice

def get_player_choice():
    invalid = 1
    while invalid:
        choice = str(input("Choose rock, paper, or scissors: "))
        if (choice == "rock") or (choice == "paper") or (choice == "scissors"):
            invalid = 0
        else:
            print("You made an invalid choice. Please try again.")
    return choice
        
def get_winner(comp,play):
    if comp == "rock":
        if play == "paper":
            winner = "player"
        elif play == "rock":
            winner = "tie"
        else:
            winner = "computer"
    elif comp == "paper":
        if play == "scissors":
            winner = "player"
        elif play == "paper":
            winner = "tie"
        else:
            winner = "computer"
    else:
        if play == "rock":
            winner = "player"
        elif play == "scissors":
            winner = "tie"
        else:
            winner = "computer"
    return winner


def main():
    # Set tie equal to 1
    tie = 1

    while tie:
        # Now, set tie equal to zero so that the loop wont continue
        tie = 0

        # Get the choices from the computer and player
        computer = get_computer_choice()
        player = get_player_choice()

        #Print out the choices
        print(f"  The computer chose {computer}, and you chose {player}.")

        # Get the winner
        winner = get_winner(computer,player)

        # Correctly print out the outputs                         
        if winner == "tie":
            print("  It's a tie. Starting over.")
            print("")
            tie = 1
        else:
            if winner == "player":
                print(f"  {player} beats {computer}")
                print("  You won the game!")
            else:
                print(f"  {computer} beats {player}")
                print("  You lost.  Better luck next time.")
            print("Thanks for playing.")







"""Do not change anything below this line."""
if __name__ == "__main__":
    main()