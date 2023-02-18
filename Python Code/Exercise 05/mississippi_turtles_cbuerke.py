"""
Author: Cameron Buerke, cbuerke@purdue.edu
Assignment: 05.4 - Mississippi Turtles
Date: 09/30/2022

Description:
    A program that uses subfunctions to draw the entirety of "Mississippi turtles" using turtle code

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
    setup(600, 400)
    width(9)
    color("purple")


def draw_e():
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


def draw_l():
    left(90)
    pendown()
    forward(12*12)
    penup()

    backward(12*12)
    right(90)



def draw_M():
    pendown()

    left(90)
    forward(8*12)

    circle(-1.5*12,180)

    forward(8*12)
    backward(8*12)
    right(180)

    circle(-1.5*12,180)

    forward(8*12)
    left(90)

    penup()


def draw_p():
    right(90)
    forward(6*12)
    right(180)

    pendown()
    forward(9*12)

    circle(-2.5*12,360)

    forward(3*12)

    penup()
    backward(6*12)
    right(90)
    forward(5*12)



def draw_r():
    left(90)
    pendown()
    forward(6*12)
    backward(3*12)

    circle(-3*12,90)
    right(90)
    penup()

    forward(6*12)
    left(90)
    



def draw_s():
    pendown()
    forward(2*12)

    circle(1.5*12,180)

    forward(12)

    circle(-1.5*12,180)

    forward(2*12)

    penup()
    right(90)
    forward(6*12)
    left(90)


def draw_t():
    forward(6.5 / 2 * 12)
    left(90)

    pendown()
    forward(12*12)
    penup()

    backward(6.5 / 2 * 12)
    left(90)
    forward(6.5 / 2 * 12)
    left(180)

    pendown()
    forward(6.5*12)

    penup()
    right(90)
    forward((12 - 6.5 / 2 ) * 12)
    left(90)
    


def draw_u():
    left(90)
    forward(7*12)
    left(180)

    pendown()
    forward(3 * 12)
    circle(3*12,180)
    forward(3*12)
    left(180)

    forward(7*12)
    left(90)

    penup()



def main():
    """After these lines, call your letter drawing functions
    as needed to draw the words "Mississippi turtles".
    """
    # Pick the pen up and go to starting location
    penup()
    goto(-23.5*12,5*12)

    speed(10)

    space = 1.69 * 12

    # Draw Mississippi
    draw_M()
    forward(space)
    for i in range(2):
        draw_i()
        forward(space)
        draw_s()
        forward(space)
        draw_s()
        forward(space)
    draw_i()
    forward(space)
    draw_p()
    forward(space)
    draw_p()
    forward(space)
    draw_i()

    goto(-23.5*12,-15*12)
    setheading(0)
    
    # Draw turtles
    draw_t()    
    forward(space)
    draw_u()  
    forward(space)
    draw_r()
    forward(space)
    draw_t()
    forward(space)
    draw_l()
    forward(space)
    draw_e()
    forward(space)
    draw_s()
    forward(space)


"""Do not change anything below this line."""
if __name__ == '__main__':
    start()
    main()
    done()
