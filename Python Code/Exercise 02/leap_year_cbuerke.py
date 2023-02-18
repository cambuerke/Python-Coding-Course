"""
Author: Cameron Buerke, cbuerke@purdue.edu
Assignment: 02.1 - Leap Year
Date: 09/07/2022

Description:
    Calculates whihc years are leap years.

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
    year = int(input('Enter a year: '))  #takes input from the user for the number of cookies

    #Calculating the parts of the recipe
    if (year % 100):
        if (year % 4):
            leap_year = 0
        else:
            leap_year = 1
    else:
        if (year % 400):
            leap_year = 0
        else:
            leap_year = 1
    
    #Printing 
    if leap_year:
        print(f'The year {year} is a leap year.')
        print(f'February of {year} has 29 days.')
    else:
        print(f'The year {year} is not a leap year.')
        print(f'February of {year} has 28 days.')








"""Do not change anything below this line."""
if __name__ == "__main__":
    main()