"""
Author: Cameron Buerke, cbuerke@purdue.edu
Assignment: 01.1 - Road Trip
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
    print('Road trip fuel cost estimator:')

    #Inputs
    distance = input('  How far away is your destination (miles)? ')  #takes input from the user for the distance 
    distance = int(distance)              
    gas_price = input('  What is the average price of gas (dollars per gallon)? ')  #takes input from the user for the price of gas
    gas_price = float(gas_price)
    mpg = input('  What is the fuel efficiency of your vehicle (mpg)? ')            #takes input from the user for the mpg of their car               
    mpg = float(mpg)

    #Calculating the cost
    cost = (2.0 * distance * gas_price / mpg)
    cost = int(cost)

    #Printing the cost
    print(f'\nThe fuel cost for this trip is approximately ${cost}.')


"""Do not change anything below this line."""
if __name__ == "__main__":
    main()