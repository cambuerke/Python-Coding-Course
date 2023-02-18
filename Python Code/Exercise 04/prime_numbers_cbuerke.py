"""
Author: Cameron Buerke, cbuerke@purdue.edu
Assignment: 04.4 - Prime Numbers
Date: 09/19/2022

Description:
    Check to see if a number inputted is prime                                 

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

def is_prime(num):
    #initialize i as 2
    i = 2
    #initialize check as 0
    check = 0
    while ((i <= (num ** 0.5)) and (check == 0)):
        if (((num % i) == 0) and (i > 1)):
            check += 1
        
        i += 1
    # check for 1 or 0
    if num == 1 or num == 0:
        check = 1

    return not bool(check)
    

def main():
    integer = 0
    while (integer != -1):
        #take input from the user
        integer = int(input("Enter a positive integer (-1 to quit): "))
        #only exit if the input is = -1                                                      
        if integer == -1:
            return

        t_or_f = is_prime(integer)

        if t_or_f:
            print_state = f"prime!"
        else:
            print_state = f"not prime."
            
        print(f"  {integer} is " + print_state)
    

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()