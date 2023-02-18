"""
Author: Your Name, login@purdue.edu
Assignment: 06.3 - Random Vowels
Date: MM/DD/YYYY

Description:
    Describe your program here.

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


def draw_a():
    # Draws an 'a'
    forward(6*12)
    left(90)

    pendown()
    forward(6*12)
    backward(3*12)
    circle(3*12,360)
    penup()

    backward(3*12)
    right(90)


def draw_e():
    # Draws an 'e'
    forward(6*12)
    left(90)
    forward(3*12)
    left(90)
    
    pendown()
    forward(6*12)
    backward(6*12)
    penup()

    left(90)
    angle = 45
    circle(-3*12,angle)
    pendown()
    circle(-3*12,360-angle)
    penup()

    forward(3*12)
    left(90)


def draw_i():
    # Draws an 'i'
    pendown()
    left(90)
    forward(6*12)

    penup()
    forward(2*12)
    pendown()
    dot(12)
    penup()

    backward(8*12)
    right(90)
    forward(2*12)


def draw_o():
    # Draws an 'o'
    forward(1.5*12)

    pendown()
    circle(3*12,360)
    penup()

    forward(1.5*12)


def draw_u():
    # Draws a 'u'
    left(90)
    forward(6*12)
    left(180)

    pendown()
    forward(3 * 12)
    circle(3*12,180)
    forward(3*12)
    left(180)

    forward(6*12)
    left(90)

    penup()


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
    """You can use this function for your own testing. It will not be checked
    by the auto-grader."""
    pass


"""Do not change anything below this line."""
if __name__ == "__main__":
    start()
    main()
    done()
