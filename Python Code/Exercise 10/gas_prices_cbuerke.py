"""
Author: Cameron Buerke, cbuerke@purdue.edu
Assignment: 10.2 - Gas Prices
Date: 11/16/2022

Description:
    Plots Average Gas prices that have been taken from an input file.

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

"""Write new functions below this line (starting with unit 4)."""
def get_textfile_data():
    data = []
    with open('2008_Weekly_Gas_Averages.txt') as fo:
        for line in fo:
            data.append(float(line.strip()))
    return data


def main():
    # Take from the input file
    gas_prices = get_textfile_data()

    weeks = [0] * len(gas_prices)
    for i in range(len(gas_prices)):
        weeks[i] = i + 1

    # Make the plot
    fig, ax = plt.subplots()
    ax.plot(weeks,gas_prices)

    # Format title and axes
    ax.set_title('2008 Weekly Gas Prices')
    ax.set_xlabel('Weeks (by number)')
    ax.set_ylabel('Average Price (dollars/gallon)')
    ax.set_ylim(1.5,4.25)
    ax.set_xlim(1,52)

    # Show the grid
    ax.grid()

    # Show the plot
    plt.show()

    
"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
