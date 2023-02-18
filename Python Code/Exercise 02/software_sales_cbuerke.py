"""
Author: Cameron Buerke, cbuerke@purdue.edu
Assignment: 02.2 - Software Sales
Date: 09/07/2022

Description:
    Tells the user how much a certain number of packages will cost,
    including discounts.

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
    number = int(input('How many packages will be purchased: '))  #takes input 
        #input validation
    if (number < 0):
        print('  Invalid Input!')
        return
        

    #Calculation
    cost = 880. #how much the packages cost with no discount ($)
    
    if (number < 4):
        discount_written = 'No'
        discount = 0
    elif (number < 40):
        discount_written = '10%'
        discount = 0.1
    elif (number < 200):
        discount_written = '15%'
        discount = 0.15
    elif (number < 1000):
        discount_written = '30%'
        discount = 0.3
    else:
        discount_written = '42%'
        discount = 0.42

    price = number * cost * (1 - discount)

      
    #Printing 
    print(f'  {discount_written} discount applied.')
    print('  The total price to purchase {} packages is ${:,.2f}.'.format(number,price))








"""Do not change anything below this line."""
if __name__ == "__main__":
    main()