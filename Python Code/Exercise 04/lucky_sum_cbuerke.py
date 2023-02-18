"""
Author: Cameron Buerke, cbuerke@purdue.edu
Assignment: 04.2 - Lucky Sum
Date: 09/19/2022

Description:
    Calculates the sum of numbers between two given values that arent divisible by 3

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

def lucky_sum(first,second):
    # Initialize sum as zero
    sum = 0
    # Find if the first number or second number are bigger
    if (second or first):
        sign = second - first
        sign = int(sign / ((sign ** 2) ** 0.5))
    else:
        sign = 1


    for i in range(first,second + sign, sign):
        if (i % 3):
            # add the current value only if it isnt divisible by 3
            sum += i

    #return the value of sum
    return int(sum)
    
    




def main():
    # Intializes
    first_int = int(input("Enter the first integer: "))
    second_int = int(input("Enter the second integer: "))
    
    # Print out the calculated sum
    print(f"The sum of the lucky numbers is {lucky_sum(first_int,second_int):,}.")
    



"""Do not change anything below this line."""
if __name__ == "__main__":
    main()