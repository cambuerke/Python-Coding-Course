"""
Author: Cameron Buerke, cbuerke@purdue.edu
Assignment: 08.5 - Number Reader
Date: 10/26/2022

Description:
    Reads from a text file of random numbers (how many is was determined by user input)

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
    # Read from the file
    numbers = []
    with open("random_numbers.txt", 'r') as fo:
        for line in fo:
            numbers.append(int(line.rstrip()))

    # Gather the useful numbers         
    num = len(numbers)
    min_value = min(numbers)
    max_value = max(numbers)
    total = sum(numbers)
    ave = total / num

    # Print off all the values           
    print(f"{num:,} numbers were read from the file.")
    print(f"Min: {min_value:,}")
    print(f"Max: {max_value:,}")
    print(f"Sum: {total:,}")
    print(f"Avg: {ave:,.1f}")


"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
