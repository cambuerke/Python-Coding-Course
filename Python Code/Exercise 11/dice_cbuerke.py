"""
Author: Cameron Buerke, cbuerke@purdue.edu
Assignment: 11.1 - Dice
Date: 11/16/2022

Description:
    Doesnt matter

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
class Dice:
    def __init__(self,sides):
        self.sides = sides
    
    # Instance Method called n_rolls
    def n_rolls(self, n):
        rolls = f''
        for i in range(n):
            if i < (n-1):
                rolls += f'{r.randint(0,self.sides)}, '
            else:
                rolls += f'{r.randint(0,self.sides)}'
        print(f"Rolling a {self.sides} sided die {n} times: {rolls}")
        return


def main():
    six = Dice(6)
    ten = Dice(10)
    twenty = Dice(20)
    six.n_rolls(10)
    ten.n_rolls(10)
    twenty.n_rolls(10)


"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
