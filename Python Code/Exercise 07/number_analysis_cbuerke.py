"""
Author: Cameron Buerke, cbuerke@purdue.edu
Assignment: 07.2 - Number Analysis
Date: 10/17/2022

Description:
    Uses a function that gives the highest, lowest, total, and average of a list passed to it.

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


def get_number_list():
    # Initialize the Variables needed (number and list)
    num = 10
    input_nums = [0] * num

    # Get the 10 numbers
    for i in range(num):
        input_nums[i] = float(input(f"  number {i + 1:>2} of {num}: "))

    return input_nums

def main():
    # First print
    print("Enter 10 numbers:")

    # Call the function to get the list of numbers
    list_nums = get_number_list()

    # Print out all the outputs necessary
    print(f"Highest number: {max(list_nums):.2f}")
    print(f"Lowest number: {min(list_nums):.2f}")
    print(f"Total: {sum(list_nums):.2f}")
    print(f"Average: {(sum(list_nums) / len(list_nums)):.2f}")



"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
