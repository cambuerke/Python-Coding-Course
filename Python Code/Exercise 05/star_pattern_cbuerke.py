"""
Author: Your Name, login@purdue.edu
Assignment: 05.3 - Star Pattern
Date: MM/DD/YYYY

Description:
    Draw a shape with an inputted number of points                                           

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
    width(7)
    side_length = 60 # Also the radius of a circle enclosed by the star.
    penup()
    goto(0, -side_length) # Start at the bottom of the star.
    pendown()


def main():
    """Write your mainline logic below this line (then delete this line)."""
    # Taking input
    num_points = float(input("How many points are being drawn? "))
    A = 360.0 / num_points
    B = 2 * A

    # Set the speed
    speed(10)

    #Change the color
    color('blue','cyan')

    #Draw the shape correctly, without fail
    right(90)
    left(A)
    begin_fill()
    for i in range(int(num_points)):
        forward(60)
        left(180)
        right(A)
        forward(60)
        right(180)
        left(B)
    end_fill()
    
        





"""Do not change anything below this line."""
if __name__ == '__main__':
    start()
    main()
    done()
