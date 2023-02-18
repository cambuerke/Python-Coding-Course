"""
Author: Cameron Buerke, cbuerke@purdue.edu
Assignment: 04.3 - Avg Grade
Date: 09/19/2022

Description:
    Calculates the average grade using three different functions

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

def get_valid_score():
    # Initialize score as -1
    score = -1
    while ((score < 0) or (score > 100)):
        score = float(input("Enter a score: "))
        if (score < 0) or (score > 100):
            print("  Invalid Input. Please try again.")
    
    # Return the score
    return score

def calc_average(list_scores):
    sum = 0
    for i in range(len(list_scores)):
        sum += list_scores[i]
    # Calculate average
    average = sum / (i + 1)

    # Return the average
    return average

def determine_grade(score):
    #determine the grade value
    if (score >= 92):
        grade = f"A"
    elif (score >= 82):
        grade = f"B"
    elif (score >= 73):
        grade = f"C"
    elif (score >= 64):
        grade = f"D"
    else:
        grade = f"F"
    
    #Return the grade value
    return grade

    
    




def main():
    # Initalize the scores array
    scores = [0,0,0,0,0]

    # For loop to fill the scores array
    for i in range(5):
        scores[i] = get_valid_score()
        print(f"  The letter grade for {scores[i]:.1f} is {determine_grade(scores[i])}.")
    
    average_score = calc_average(scores)

    print("\nResults:")
    print(f"  The average score is {average_score:.2f}.")
    print(f"  The letter grade for {average_score:.2f} is " + determine_grade(average_score) +".")

    


    
    



"""Do not change anything below this line."""
if __name__ == "__main__":
    main()