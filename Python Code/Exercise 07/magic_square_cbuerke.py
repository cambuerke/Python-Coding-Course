"""
Author: Cameron Buerke, cbuerke@purdue.edu
Assignment: 07.4 - Magic Square
Date: 10/20/2022

Description:
    Uses two functions, one that prints a square and one that determines if a sqaure is a magic square.

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
from random import sample as s

"""Write new functions below this line (starting with unit 4)."""


def print_square(nums):
    # Print the numbers correctly in a square
    for i in range(3):
        print(f"  {nums[i][0]} {nums[i][1]} {nums[i][2]}")

def is_magic(square):
    # If magic == 8 then it could be a magic sqaure
    magic = 0
    # If magic == 8 & check == one_thru_nine, then it must be a magic square
    check = [0] * 9
    one_thru_nine = [1,2,3,4,5,6,7,8,9]
    # Check for addition across rows and columns
    for i in range(3):
        if sum(square[i]) == 15:
            magic += 1
        if sum(square[:][i]) == 15:
            magic += 1
        for j in range(3):
            num = square[i][j]
            check[num - 1] = num
    # Check for diagonal additions
    if ((square[0][0] + square[1][1] + square[2][2]) == 15) :
        magic += 1
    if (square[0][2] + square[1][1] + square[2][0]) == 15:
        magic += 1

    # Final check for if condition
    if (magic == 8) & (check == one_thru_nine):
        magic = 1
    else:
        magic = 0
    
    # Return a boolean of True or False
    return bool(magic)
        

def main():
    # Initialize
    first_sq = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    second_sq = [[5, 5, 5], [5, 5, 5], [5, 5, 5]]
    third_sq = [[4, 9, 2], [3, 5, 7], [8, 1, 6]]
    squares = [first_sq, second_sq, third_sq]

    # Printing
    for i in range(3):
        print("Your square is:")
        print_square(squares[i])
        if is_magic(squares[i]):
            print("It is a Lo Shu magic square!")
        else:
            print("It is not a Lo Shu magic square.")
        if i < 3:
            print("")








"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
