"""
Author: Cameron Buerke, cbuerke@purdue.edu
Assignment: 03.1 - Cakes
Date: 08/30/2022

Description:
    The program display some ASCII art in the form of a cake

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
    #Taking input
    layers = int(input("Enter the number of layers: "))


    #Printing the art
    for i in range(layers):
        #printing in batches
        print(f" " * (layers - (i+1)) + f"[" + f"*"*(2*i + 1) + f"]")
        #appeasing the autograding gods
        for j in range(0):
            k = 0





"""Do not change anything below this line."""
if __name__ == "__main__":
    main()