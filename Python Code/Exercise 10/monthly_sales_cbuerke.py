"""
Author: Cameron Buerke, cbuerke@purdue.edu
Assignment: 10.1 - Monthly Sales
Date: 11/03/2022

Description:
    Takes user input for the sales of each month and then plots a pie chart with the data

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
import matplotlib.pyplot as plt

"""Write new functions below this line (starting with unit 4)."""
def get_textfile_data():
    week = [1]
    index = 0
    data = []
    with open('2008_Weekly_Gas_Averages.txt') as fo:
        for line in fo:
            data.append(int(line.strip()))
            index +=1
            week[index] = week[index-1] + 1
    print(week)
            
    





def main():
    # Write each month out                                        
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

    # Initilaize colors                                    
    CoalGray = '#4D4038'
    MoonDustGray = '#BAA892'
    EverTrueBlue = '#5B6870'
    SlayterSkyBlue = '#6E99B4'
    AmeliaSkyBlue = '#A3D6D7'
    LandGrantGreen = '#085C11'
    RossAdeGreen = '#849E2A'
    CeleryBogGreen = '#C3BE0B'
    SpringFestGreen = '#E9E45B'
    OakenBucketBrown = '#6B4536'
    BellTowerBrick = '#B46012'
    MackeyOrange = '#FF9B1A'
    c = [CoalGray, MoonDustGray, EverTrueBlue, SlayterSkyBlue, AmeliaSkyBlue, LandGrantGreen, RossAdeGreen, CeleryBogGreen, SpringFestGreen, OakenBucketBrown, BellTowerBrick, MackeyOrange]

    # Initialize the list for input
    sales = [0] * len(months)

    # Get input from the user
    for i in range(len(months)):
        sales[i] = float(input(f"Enter the sales for {months[i]}: "))
    
    # Print the Pie Chart
    fig, ax = plt.subplots()
    ax.pie(sales,labels=months, colors=c)
    ax.set_title("Monthly Sales Values")
    plt.show()
        


    
"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
