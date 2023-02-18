"""
Author: Cameron Buerke, cbuerke@purdue.edu
Assignment: 01.3 - Cookie Recipe
Date: 08/30/2022

Description:
    The program will ask for the distance, price, and mpg for a trip
    and will estimate the cost of the trip.

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
    number = input('How many cookies do you want to make? ')  #takes input from the user for the number of cookies
    number = int(number) #changing the input to an integer

    #Calculating the parts of the recipe
    fraction_of_48 = number / 48
    butter = 1.25 * fraction_of_48
    sugar = 1.5 * fraction_of_48
    flour = 2.5 * fraction_of_48

    #Printing the outputs
    print('To make {:,} cookies, you will need:'.format(number))
    print('{0:>10,.2f} cups of butter'.format(butter))
    print('{0:>10,.2f} cups of sugar'.format(sugar))
    print('{0:>10,.2f} cups of flour'.format(flour))





"""Do not change anything below this line."""
if __name__ == "__main__":
    main()