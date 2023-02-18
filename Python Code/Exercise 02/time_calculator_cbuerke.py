"""
Author: Cameron Buerke, cbuerke@purdue.edu
Assignment: 02.4 - Time Calculator
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
    time = int(input('Please enter a time in seconds: '))  #takes input 
    time_initial = time
        #input validation
    if (time < 0):
        print('  Invalid Input!')
        return


    # Finding the values for each section of time
    if (time < 60):
        print(f'  {time} seconds is less than one minute.')
        return

    # Calculate days
    if ((time / 86400) >= 1):
        days = int(time / 86400)
        time -= days * 86400
    else:
        days = 0

    # Calculate hours
    if ((time / 3600) >= 1):
        hours = int(time / 3600)
        time = time - hours * 3600
    else: 
        hours = 0

    # Calculate minutes
    if((time / 60) >= 1):
        min = int(time / 60)
        time -= min * 60
    else:
        min = 0
    
    # Store the seconds
    sec = time


    # Building the string for displaying the time properly
    num_used = int(bool(sec)) + int(bool(min)) + int(bool(hours)) + int(bool(days))
    num_array = [sec,min,hours,days]
    time_array = [f'{sec} second(s)',f'{min} minute(s)',f'{hours} hour(s)',f'{days} day(s)']
    i = 0
    check = 0

    while (check < num_used):
        if (bool(num_array[i]) & (check == 0)):
            written_time = time_array[i]
            check += 1
        elif (bool(num_array[i]) & (check == 1)):
            written_time = time_array[i] + f' and ' + written_time
            check += 1
        elif (bool(num_array[i]) & (check > 1)):
            written_time = time_array[i] + f', ' + written_time
            check += 1
        i += 1


    #printing the correct outputs
    print('  {:,d} seconds equals '.format(time_initial) + written_time + f'.')


"""Do not change anything below this line."""
if __name__ == "__main__":
    main()