"""
Author: Cameron Buerke, cbuerke@purdue.edu
Assignment: 06.4 - Log Spiral
Date: MM/DD/YYYY

Description:
    Uses turtle code to draw a spiral calulated from the math module.

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
from math import *


"""Write new functions below this line (starting with unit 4)."""


def start():
    """This function initializes the window and the turtle.
    Do not modify this function or any of the properties it sets.
    """
    setup(564, 564)
    width(5)


def main():
    # Set the constants       
    a = 4
    b = 0.22
    
    # Move to the starting position and get the pen ready
    penup()
    goto(a,0)
    pendown()
    # Set the speed
    speed(10)

    # Calculate the spiral and move to the correct positions
    for theta in range(0,1081,1):
        theta *= pi / 180
        x = a * exp(b * theta) * cos(theta)
        y = a * exp(b * theta) * sin(theta)
        goto(x,y)



"""Do not change anything below this line."""
if __name__ == "__main__":
    start()
    main()
    done()
