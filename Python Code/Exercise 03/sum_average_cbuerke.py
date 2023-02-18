"""
Author: Cameron Buerke, cbuerke@purdue.edu
Assignment: 03.2 - Sum Average
Date: 08/30/2022

Description:
    Takes input and sums and averages the inputs and displays them

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
    #initialize variables
    num = 0
    sum = 0
    count = 0
    
    #While loop
    while (num >= 0):
        #input
        num = float(input("Enter a non-negative number (negative to quit): "))
        if (num >= 0):
            sum += num
            count += 1
        elif (count == 0):
            #printing
            print("  You didn't enter any numbers.")
        elif ((count > 0) & (num < 0)):
            #calc average
            ave = sum / count
            #printing
            print(f"  You entered {count} numbers.")
            print(f"  Their sum is {sum:.3f} and their average is {ave:.3f}.")








"""Do not change anything below this line."""
if __name__ == "__main__":
    main()