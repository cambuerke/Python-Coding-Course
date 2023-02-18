"""
Author: Cameron Buerke, cbuerke@purdue.edu
Assignment: 06.3 - Random Vowels
Date: 10/14/2022

Description:
    Prints all vowels in a random order using turtle code to draw the vowels.

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

"""Import modules below this line (starting with unit 6)."""
from turtle import *
import vowels as v
import random as r


"""Write new functions below this line (starting with unit 4)."""
def start():
    """This function initializes the window and the turtle.
    Do not modify this function or any of the properties it sets.
    """
    setup(600, 400)
    width(9)
    speed(0)
    penup()
    goto(-220, -30)


def main():
    # Defines the spaces between the letters            
    spacing = 2.5 * 12

    # Makes an array with the vowels as characters            
    vowels = ['a','e','i','o','u']
    # Shuffles the array of vowels
    r.shuffle(vowels)

    # Uses turtle code to draw the vowels            
    for i in range(len(vowels)):
        if vowels[i] == 'a':
            v.draw_a()
            forward(spacing)
        elif vowels[i] == 'e':
            v.draw_e()
            forward(spacing)
        elif vowels[i] == 'i':
            v.draw_i()
            forward(spacing)
        elif vowels[i] == 'o':
            v.draw_o()
            forward(spacing)
        else:
            v.draw_u()
            forward(spacing)


"""Do not change anything below this line."""
if __name__ == "__main__":
    start()
    main()
    done()
