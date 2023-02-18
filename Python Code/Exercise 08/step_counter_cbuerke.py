"""
Author: Cameron Buerke, cbuerke@purdue.edu
Assignment: 08.6 - Step Counter
Date: 10/26/2022

Description:
    Imports a file and prints out how many average steps were taken in each month of the year. 

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
    # Open the file and store it as a variable
    steps = []
    with open("steps.txt") as fo:
        for line in fo:
            steps.append(int(line.rstrip()))
    
    # Months written out
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    # Days in each month
    days_each = [31,28,31,30,31,30,31,31,30,31,30,31]
    ave_steps = [0] * len(months)
    # First print
    print("The average steps taken each month were:")
    # Get the average steps and print them
    for i in range(len(months)):
        for days in range(days_each[i]):
            ave_steps[i] += steps[days]
        del steps[0:days_each[i]]
        ave_steps[i] /= days_each[i]
        # Print the average steps
        print(f"{months[i]:>10} : {ave_steps[i]:.2f}")
    

    
"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
