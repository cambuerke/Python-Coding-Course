"""
Author: Cameron Buerke, cbuerke@purdue.edu
Assignment: 10.4 - Sin Cos
Date: 11/16/2022

Description:
    Plots Sine and Cosine on the same graph so that it can be seen (0 to 2pi)

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
import matplotlib.pyplot as plt
from math import pi, sin, cos

"""Write new functions below this line (starting with unit 4)."""


def main():
    # Make the x-values
    inc = 1000
    x = [0] * (inc + 1)
    x_labels = [pi/2, pi, 3*pi/2, 2*pi]
    x_written = ['$\\pi/2$', '$\\pi$', '$3\\pi/2$', '$2\\pi$']
    for i in range(inc):
        x [i + 1] = x[i] + 2 * pi / inc

    # Make the sine and cosine functions
    sin_values = [0] * len(x)
    cos_values = [0] * len(x)
    for i in range(len(x)):
        sin_values[i] = sin(x[i])
        cos_values[i] = cos(x[i])

    # Make the plots
    fig, ax = plt.subplots()

    # Graph both plots
    ax.plot(x, sin_values, color='r')
    ax.plot(x, cos_values,color='b')

    # Set the x and y limits
    ax.set_xlim(x[0],x[-1])
    ax.set_xlim(min(sin_values),max(sin_values))

    # Set the tick values and label them
    ax.set_xticks(x_labels,x_written)
    ax.set_yticks([-1,1],['−1','1'])

    # Center the x-axis on the figure
    for spine in ['top', 'right']:
        ax.spines[spine].set_visible(False)
    for spine in ['bottom', 'left']:
        ax.spines[spine].set_position('zero')

    # Show the plot           
    plt.show()


    
"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
