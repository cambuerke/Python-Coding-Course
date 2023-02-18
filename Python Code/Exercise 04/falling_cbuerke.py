"""
Author: Cameron Buerke, cbuerke@purdue.edu
Assignment: 04.1 - Falling
Date: 09/19/2022

Description:
    Calculates the distance that a falling object has fallen given the time
    (uses Venus's mean surface gravity)

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

def falling_dist(t):
    g = 8.87 #gravity of venus (m/s^2)
    dist = 0.5 * g * t ** 2 #calculates the distance
    return dist




def main():
    # Intializes time as 5
    time = 5

    # Prints out the titles
    print("Time (s)  Distance (m)")
    print("----------------------")

    # Prints out the correct values
    while (time <= 50):
        print(f"{time:>8}  {falling_dist(time):12.1f}")
        time += 5



"""Do not change anything below this line."""
if __name__ == "__main__":
    main()