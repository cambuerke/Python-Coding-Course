"""
Author: Cameron Buerke, cbuerke@purdue.edu
Assignment: 01.2 - Interest
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
    #Printing the first line
    print('Enter the following parameters.')

    #Inputs
    principal = input('  The initial deposit? ') #input for principal amount 
    principal = int(principal) #turning it into a integer
    interest_rate = input('  The annual interest rate in percent? ') #input for annual interest rate
    interest_rate = float(interest_rate) / 100 #making interst rate into a float
    years = input('  The number of years the account earn interest? ') #input for the years the account earns interst                
    years = float(years) #turning years into an integer
    compound = input('  The number of times interest is compounded each year: ') #input for compounding
    compound = int(compound) #turning the compound into an integer
    
    #Calculating the future value
    future_value = principal * (1 + interest_rate / compound) ** (compound * years)

    #Printing the last line
    print('The balance of this account will be ${:,.2f} after {:.1f} years.'.format(future_value,years))


"""Do not change anything below this line."""
if __name__ == "__main__":
    main()