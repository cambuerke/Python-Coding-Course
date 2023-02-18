"""
Author: Cameron Buerke, cbuerke@purdue.edu
Assignment: 08.3 - File Stats
Date: 10/26/2022

Description:
    Imports a file and prints out how many words and lines are in it. Along with what the average word count is per line. 

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
    with open("frontiero_v_richardson.txt") as fo:
        everything = fo.read()
    
    # Number of words
    words = len(everything.split())
    # Number of lines
    lines = len(everything.split("\n")) - 1
    # Average number of words per line
    ave_words_per_line = words / lines

    # Printing
    print(f"Total number of words: {words}")
    print(f"Total number of lines: {lines}")
    print(f"Average number of words per line: {ave_words_per_line:.1f}")
    

    


"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
