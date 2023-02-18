"""
Author: Cameron Buerke, cbuerke@purdue.edu
Assignment: 03.3 - Rainfall
Date: 08/30/2022

Description:
    Takes input for rainfall in a year and ouputs the moths, total, and average

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
    years = int(input("Enter the number of years: "))
    if (years < 1):
        print("Invalid input; years must be greater than 0.")
        return
    months = 12 * years
    months_written = [f"Jan",f"Feb",f"Mar",f"Apr",f"May",f"Jun",f"Jul",f"Aug",f"Sep",f"Oct",f"Nov",f"Dec"]
    sum = 0
    count = 0
    disp_year = 0
    for i in range(months):
        j = int (i % 12)
        if (j == 0):
            disp_year += 1
            print(f"  For year No. {disp_year}")
        check = 0
        while (check == 0):
            rain = float(input(f"    Enter the rainfall for " + months_written[j] + f".: "))
            if (rain >= 0):
                check = 1
            else:
                print("    Invalid input; rainfall cannot be negative.")
        sum += rain
        count += 1
    
    #printing out the outputs properly                                           
    print(f"There are {months} months.")
    print(f"The total rainfall was {sum:.2f} inches.")
    print(f"The monthly average rainfall was {(sum/count):.2f} inches.")





"""Do not change anything below this line."""
if __name__ == "__main__":
    main()