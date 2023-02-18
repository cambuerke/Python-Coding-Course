"""
Author: Cameron Buerke, cbuerke@purdue.edu
Assignment: 08.4 - Number Writer
Date: 10/26/2022

Description:
    Writes to a text file of random numbers (how many is determined by user input)

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


def main():
    # Take input from the user on how many numbers to print
    num = int(input("How many numbers would you like? "))
    # Intialize an array 
    rand_nums = [0] * num
    # Make an array of random numbers 
    for i in range(num):
        rand_nums[i] = str(r.randint(1019,1215)) + "\n"

    # Write to the file
    with open("random_numbers.txt", 'w') as fo:
        fo.writelines(rand_nums)


"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
