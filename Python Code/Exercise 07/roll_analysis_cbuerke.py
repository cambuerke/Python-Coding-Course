"""
Author: Cameron Buerke, cbuerke@purdue.edu
Assignment: 07.3 - Roll Analysis
Date: 10/17/2022

Description:
    Uses one function to simulate rolling 1 dice, then one that simulates roling two die a lot of times and shows the distribution.

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
import random as r

"""Write new functions below this line (starting with unit 4)."""


def roll_d6():
    roll = r.randint(1,6)
    return roll

def get_2d6_rolls(num):
    totals = [0] * num
    for i in range(num):
        totals[i] = roll_d6() + roll_d6()

    return totals

def main():
    # Generate list of rolls
    N = 1000000000
    list_totals = get_2d6_rolls(N)
    freq = [0] * 11

    # Find all the frequencies                                            
    for i in range(2,13):
        for j in range(N):
            if list_totals[j] == i:
                freq[i - 2] += 1
        freq[i - 2] = freq[i - 2] * 100 / N

    # Print the outputs     
    print("Roll  Frequency")
    for i in range(2,13):
        print(f" {i:>2}  {freq[i - 2]:>7.2f}%")


"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
