"""
Author: Cameron Buerke, cbuerke@purdue.edu
Assignment: 05.1 - Maze
Date: 09/29/2022

Description:
    Get a turtle out of a maze. Using turtle commands and a template given

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
from turtle import *

"""Write new functions below this line (starting with unit 4)."""


def start():
    """This function initializes the window and the turtle.
    Do not modify this function or any of the properties it sets.
    """
    setup(564, 564)
    bgpic("maze.png")
    shape("turtle")
    color("green")
    width(5)


def main():
    """Write your mainline logic below this line (then delete this line)."""
    # Find the exit (hardcoded)                                                                                                                    
    forward(12)
    right(90)
    forward(3*12)
    right(90)
    forward(4*12)
    left(90)
    forward(2*12)
    left(90)
    forward(6*12)
    right(90)
    forward(4*12)
    left(90)
    forward(2*12)
    left(90)
    forward(2*12)
    right(90)
    forward(2*12)
    left(90)
    forward(6*12)
    right(90)
    forward(4*12)
    left(90)
    forward(2*12)
    left(90)
    forward(2*12)
    right(90)
    forward(4*12)
    right(90)
    forward(10*12)
    right(90)
    forward(5*12)
    left(90)
    forward(12)





"""Do not change anything below this line."""
if __name__ == "__main__":
    start()
    main()
    done()
