"""
Author: Cameron Buerke, cbuerke@purdue.edu
Assignment: 02.3 - Roulette Colors
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
    pocket = int(input('Please choose a pocket number: '))  #takes input 
        #input validation
    if ((pocket < 0) or (pocket > 36)):
        print('  Invalid Input!')
        return
        

    #if statements
    if (pocket):
        # (1-10) or (19-28)
        if ((pocket <= 10) or ((pocket >= 19) & (pocket <= 28))):
            if (pocket % 2):
                # odd
                color = 'red'
            else:
                # even
                color = 'black'
        # (11-18) or (29-36)
        else:
            if (pocket % 2):
                #odd
                color = 'black'
            else:
                #even
                color = 'red'
    # Zero
    else:
        color = 'green'
      
    #Printing 
    print(f'  Pocket number {pocket} is {color}.')
    






"""Do not change anything below this line."""
if __name__ == "__main__":
    main()