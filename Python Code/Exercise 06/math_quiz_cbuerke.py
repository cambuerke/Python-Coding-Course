"""
Author: Cameron Buerke, cbuerke@purdue.edu
Assignment: 06.1 - Math Quiz
Date: 10/03/2022

Description:
    This program generates two random numbers and then asks the user a quiz on their addition.

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

def random_number(length):
    #initailize a few values
    digit = 1
    rand_num = 0

    for i in range(length):
        if i != (length - 1):
            rand_num += digit * r.randrange(0,10,1)
            digit *= 10

        else:
            rand_num += digit * r.randrange(1,10,1)
    
    return rand_num
        

def main():
    #find the first random values
    first = random_number(2)
    second = random_number(3)
    #find their totals
    total = first + second

    #print the outputs properly
    print(f"   {first:>2}")
    print(f"+ {second:>3}")
    print(f"-----")

    #take the input guess from the user
    guess = int(input("= "))

    #print out the correct response
    if guess == total:
        print(f"Correct -- Good Work!")
    else:
        print(f"Incorrect. The correct answer is {total}.")




"""Do not change anything below this line."""
if __name__ == "__main__":
    main()