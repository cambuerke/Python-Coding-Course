"""
Author: Cameron Buerke, cbuerke@purdue.edu
Assignment: 09.1 - Capital Quiz
Date: 10/31/2022

Description:
    Imports a file that has states and capitals and then quizes the user on the US State capitals.

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
def get_state_data():
    # Get the info from the text file
    state_data = []
    with open("state_capitals.txt") as fo:
        for line in fo:
            state_data.append(line.rstrip())

    # Split the capitals and states
    capitals = [''] * len(state_data)
    states = [''] * len(state_data)
    for i in range(len(state_data)):
        [capitals[i],states[i]] = state_data[i].split(',')
        states[i] = states[i].strip()

    # Make the dictionary & return it

    states_and_caps = dict(zip(states,capitals))

    return states_and_caps



def main():
    # Call the function to make the dictionary
    state_data = get_state_data()

    # Randomly shuffle
    states =  list(state_data.keys())

    i = 0
    correct = 0
    total = 0
    guess = ''
    while guess != '0':
        if len(states) != 0:
            num = r.randint(0,len(states) - 1)
            state = states[num]
            capital = state_data[state]
            guess = str(input(f"What is the capital of {state} (enter 0 to quit)? "))
            guess = guess.title()
        else:
            guess = '0'

        if (guess == '0') & (total > 0):
            print(f"You answered {correct} out of {total} questions correctly.")
        elif (guess == '0') & (total == 0):
            print("You answered 0 out of 0 questions correctly.")
        elif guess == capital:
            print("  That is correct!")
            del states[num]
            correct += 1
            total += 1
        else:
            print("  That is incorrect.")
            print(f"  The capital of {state} is {capital}.")
            total += 1
            

    
"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
