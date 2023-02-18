"""
Author: Cameron Buerke, cbuerke@purdue.edu
Assignment: 09.2 - World Series
Date: 11/01/2022

Description:
    Imports a file that has World Series winners and then prints out which team won that year and how many times the team has won.

Contributors:
    Nathan Tollett, ntollett@purdue.edu [repeat for each]

My contributor(s) helped me:
    [ ] understand the assignment expectations without
        telling me how they will approach it.
    [ ] understand different ways to think about a solution
        without helping me plan my solution.
    [x] think through the meaning of a specific error or
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
def load_winners_data():
    # Get the info from the text file
    winner_data = []
    with open("WorldSeriesWinners.txt") as fo:
        for line in fo:
            winner_data.append(line.strip())

    years = [0] * len(winner_data)
    year = 1903
    for i in range(len(winner_data)):
        if (year == 1904) or (year == 1994):
            year += 1
        years[i] = year
        year += 1

    years_winners = dict(zip(years,winner_data))

    all_teams = []

    for i in range(len(winner_data)):
        included = 0
        for j in range(len(all_teams)):
            if winner_data[i] == all_teams[j]:
                included = 1
        if included == 0:
            all_teams.append(winner_data[i])

    wins = [0] * len(all_teams)
    for i in range(len(all_teams)):
        wins[i] = winner_data.count(all_teams[i])
    
    winners_count = dict(zip(all_teams,wins))

    return winners_count, years_winners



def main():
    # Call the function to make the dictionaries
    [win_count, year_win] = load_winners_data()
    
    # Take input from the user
    year = int(input("Enter a year in the range 1903 -- 2021: "))

    if (year > 2021) or (year < 1903):
        print(f"  Data for the year {year} is not included in this system.")
    elif (year == 1904) or (year == 1994):
        print(f"  The World Series wasn't played in the year {year}.")
    else:
        print(f"  The {year_win[year]} won the World Series in {year}.")
        print(f"  They have won the World Series {win_count[year_win[year]]} times.")
            

    
"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
