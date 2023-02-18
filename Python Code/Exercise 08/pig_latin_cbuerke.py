"""
Author: Cameron Buerke, cbuerke@purdue.edu
Assignment: 08.1 - Pig Latin
Date: 10/26/2022

Description:
    Converts a given string into a string that is in pig latin and outputs it.

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


def pig(string):
    string = string.split()
    pig_str = [""] * len(string)
    for i in range(len(string)):
        word = string[i]
        pig_str[i] = word[1:len(word)]
        pig_str[i] += word[0]
        pig_str[i] += "ay"
    
    full_str = (" ".join(pig_str)).capitalize()

    return full_str



def main():
    # Prompt for input string from user
    input_string = str(input("Enter a string: "))

    # Print the pig latin string
    print(f"Pig latin: {pig(input_string)}")
    
    


"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
