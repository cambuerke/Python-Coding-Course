"""
Author: Cameron Buerke, cbuerke@purdue.edu
Assignment: 03.4 - Organisms
Date: 08/30/2022

Description:
    Takes starting population and dailing increase in percent, and displays info about those things

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
    pop = float(input("Starting population, in thousands: "))
    daily_p = float(input("Average daily increase, in percent: "))
    days = int(input("Number of days to multiply: "))
    
    #Printing outputs properly
    print("Day   Approx. Pop")
    for i in range(days + 1):
        #printing again, as it is
        print(f"{i:>3d}    {pop:>10,.3f}")
        #calculate the population again
        pop += pop * daily_p / 100





"""Do not change anything below this line."""
if __name__ == "__main__":
    main()