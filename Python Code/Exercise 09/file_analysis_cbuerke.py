"""
Author: Cameron Buerke, cbuerke@purdue.edu
Assignment: 09.4 - File Analysis
Date: 11/03/2022

Description:
    Prints out to a file a specific analysis of all the words in the file. Compares two files given in this course ('common words' and 'either but not both').

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
import string as s

"""Write new functions below this line (starting with unit 4)."""
def get_file_words(filename):
    all_lines = []
    with open(filename) as fo:
        for line in fo:
            all_lines.append((line.strip()).split())

    words = []
    punct = '.!"'+"'(),-/:;?[]^_++)'"
    
    for i in range(len(all_lines)):
        for j in range(len(all_lines[i])):
            for k in punct:
                all_lines[i][j] = all_lines[i][j].strip(k)
            words.append((all_lines[i][j]).lower())
    return words

def find_unique_words(words):
    set_words = sorted(set(words))
    count = [0] * len(set_words)
    index = 0

    for i in set_words:
        for j in words:
            if i == j:
                count[index] += 1
        index += 1
    return set_words, count

def print_sets(name, set):
    words = list(set)
    with open(name, 'w') as fo:
        for i in range(len(words)):
            fo.write(words[i] + '\n')

def main():
    # Get the data from the function                                                                                                                                                                                                                                                                
    file_1_words = get_file_words("python_1.txt")
    file_2_words = get_file_words("python_2.txt")
    [unique_words_1, counts_1] = find_unique_words(file_1_words)
    [unique_words_2, counts_2] = find_unique_words(file_2_words)

    unique_words = [unique_words_1, unique_words_2]
    counts = [counts_1, counts_2]
    outputs = [[''] * len(unique_words_1), [''] * len(unique_words_2)]

    # Printing the first two textfiles
    for i in range(2):
        for j in range(len(outputs[i])):
            if j != (len(outputs[i]) - 1):
                outputs[i][j] = unique_words[i][j] + ': ' + str(counts[i][j]) + '\n'
            else:
                outputs[i][j] = unique_words[i][j] + ': ' + str(counts[i][j])
        with open(f"python_{i+1}_word_frequency.txt", 'w') as fo:
            fo.writelines(outputs[i])
        unique_words[i] = set(unique_words[i])
    
    # Printing the last two textfiles
    print_sets("common_words.txt", sorted(unique_words[0] & (unique_words[1])))
    print_sets("eitherbutnotboth.txt", sorted(unique_words[0] ^ (unique_words[1])))
    
"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
