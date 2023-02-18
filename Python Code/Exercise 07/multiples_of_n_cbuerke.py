"""
Author: Cameron Buerke, cbuerke@purdue.edu
Assignment: 07.1 - Multiples of N
Date: 10/17/2022

Description:
    Uses a function that takes in a numebr and a list and returns a list of all the elements from the list that are multiples of the number.

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


def multiples_of(num,list):
    # Initialize necessary variables
    length = len(list)
    multiples = [0] * length
    j = 0

    # Find the multiples 
    for i in range(length):
        if (list[i] % num) == 0:
            multiples[j] = list[i]
            j += 1
    
    multiples = multiples[0:j]

    return multiples


def main():
    # Initialize the Variables needed (number and list)
    N = 13
    original_list = [19, 1599, -546, 10, 39, -58, 1, 85, 201, -91, 286, 799, 406]

    # Call the function to get the list of multiples
    mults = multiples_of(N,original_list)

    # Print out all the outputs necessary
    print("Original list of numbers:")
    print(f"  {original_list}")
    print("Numbers in the list that are multiples of 13:")
    print(f"  {mults}")



"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
