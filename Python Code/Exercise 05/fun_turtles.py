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
from PIL import Image
import numpy as np

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
    image = Image.open('maze.png')
    data = np.array(image)
    data = data % 254
    data = data[:,:,1]
    print(data[40,40])

    k = 0
    l = 0
    position = [[0 for a in range(47)] for b in range(47)]

    for i in range(0,len(data),12):
        print('')
        for j in range(0,len(data[1]),12):
            print(data[i,j], end= '')
            #position[int(k),int(l)] = data[int(i),int(j)]
            #l += 1
        #k += 1
    
    #print(position)
    






"""Do not change anything below this line."""
if __name__ == "__main__":
    #start()
    main()
    #done()
