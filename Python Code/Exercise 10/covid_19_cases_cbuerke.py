"""
Author: Cameron Buerke, cbuerke@purdue.edu
Assignment: 10.3 - covid 19 cases
Date: 11/16/2022

Description:
    Plots Covid-19 cases that have been taken from an input file.

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
import datetime

"""Write new functions below this line (starting with unit 4)."""
def get_textfile_data():
    data = []
    with open('indiana_covid-19_data_fall_2022.txt') as fo:
        for line in fo:
            data.append((line.strip()))
            index = len(data) - 1
            data[index] = data[index].split()
    
    start_weeks = [''] * len(data)
    end_weeks = [''] * len(data)
    num_cases = [0] * len(data)
    num_deaths = [0] * len(data)
    total = [0] * len(data)

    for i in range(len(data)):
        start_weeks[i] = data[i][0]
        end_weeks[i] = data[i][1]
        num_cases[i] = float(data[i][2]) + num_cases[i - 1]
        num_deaths[i] = float(data[i][3]) + num_deaths[i - 1]
        total[i] = (num_cases[i] - num_deaths[i]) / 1000

    
    return start_weeks, end_weeks, total


def main():
    # Take from the input file             
    [start, end, cases] = get_textfile_data()

    # Format the dates properly for plotting     
    x = []
    for date in start:
        y, m, d = date.split('-')
        dt = datetime.date(int(y), int(m), int(d))
        x.append(dt)

    # Make the plots
    fig, ax = plt.subplots()
    ax.bar(x,cases, width=7)
    
    # Format the axes
    fig.autofmt_xdate()
    ax.set_title('Weekly Positive COVID-19 Cases in Indiana')
    ax.set_xlabel('Date')
    ax.set_ylabel('Number of Cases (in thousands)')

    # Show the plot           
    plt.show()


    
"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
