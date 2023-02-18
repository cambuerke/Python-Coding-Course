"""
Author: Cameron Buerke, cbuerke@purdue.edu
Assignment: 02.5 - Fluid Mechanics
Date: 09/07/2022

Description:
    Calculates reynolds number based on the velocity of water, pipe diameter, and temperature

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


"""Write new functions below this line (starting with unit 4)."""


def main():
    #Input
    temp = float(input('Enter the temperature in °C as 5, 20, or 50: '))
    v_water = float(input('Enter the velocity of water in the pipe (m/s): '))
    pipe_diam = float(input("Enter the pipe's diameter (m): "))

    # Find the correct viscosity value
    if (temp == 5):
        visc = 1.52 * 10 ** -6
    elif (temp == 20):
        visc = 1.00 * 10 ** -6
    elif (temp == 50):
        visc = 5.54 * 10 ** -7
    else:
        print("  Invalid input!")
        return
    
    # Calculate the reynolds number
    reynold = v_water * pipe_diam / visc

    # Print
    print('At {:.1f}°C, the Reynolds number for flow at {} m/s in a {} m diameter pipe is {:.2e}.'.format(temp,v_water,pipe_diam,reynold))


"""Do not change anything below this line."""
if __name__ == "__main__":
    main()