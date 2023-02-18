"""
Author: Cameron Buerke, cbuerke@purdue.edu
Assignment: 08.2 - Phone Number Converter
Date: 10/26/2022

Description:
    Converts a given phone number that has characters in it to an entirely numeric phone number. 

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


def convert_number(string):
    string = string.upper()
    alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    nums = ['2'] * 3 + ['3'] * 3 + ['4'] * 3 + ['5'] * 3 + ['6'] * 3 + ['7'] * 4 + ['8'] * 3 + ['9'] * 4
    for j in range(len(alphabet)):
        string = string.replace(alphabet[j],nums[j])
    return string



def main():
    # Prompt for input string from user
    input_string = str(input("Enter a telephone number: "))

    # Print the converted phone number
    print(f"The phone number is {convert_number(input_string)}")
    
    


"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
