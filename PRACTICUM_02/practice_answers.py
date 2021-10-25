"""
Author: Patrick Marchione

Practice exam for the practicum 02
"""

# Question 01: LOOPS
# Create a while and for loop to get every fourth character from the string and print it
def loops():
    word = "dkhflshfcnsdakjhfjladsfxdalshfcdajklhfdalxdmfjdhsmfxjdhlmjlkhmjdkhf kdlhcjkafdlshmfxjdhhdajdfmxajslmxajlhmfakxjdklxmdmhfxkjdlhfxljkdah"

    counter = 1
    answer = ""
    while counter < len(word):
        if counter % 4 == 0:
            answer = answer + word[counter-1]
        counter += 1
    
    print(answer)

    counter = 1
    answer = ""
    for i in range(len(word)):
        if counter % 4 == 0:
            answer = answer + word[i]
        counter += 1

    print(answer)

# Question 02: FILES
# Read from the file "complete_nonsense.txt" and count the amount of vowels
# Then write the answers(total vowels, total As, total Es, etc) to another file

def file_problem():
    total_vowels = 0
    total_a = 0
    total_e = 0
    total_i = 0
    total_o = 0
    total_u = 0
    
    with open("complete_nonsense.txt", 'r') as file:
        for line in file:
            for ch in line.strip():
                if ch == 'a':
                    total_a += 1
                    total_vowels += 1
                elif ch == 'e':
                    total_e += 1
                    total_vowels += 1
                elif ch == 'i':
                    total_i += 1
                    total_vowels += 1
                elif ch == 'o':
                    total_o += 1
                    total_vowels += 1
                elif ch == 'u':
                    total_u += 1
                    total_vowels += 1
    
    with open("answers.txt", 'w') as file:
        file.write("Answers to the Problem\n")
        file.write("Total Vowels: "+str(total_vowels)+"\n")
        file.write("Total As: "+str(total_a)+"\n")
        file.write("Total Es: "+str(total_i)+"\n")
        file.write("Total Is: "+str(total_e)+"\n")
        file.write("Total Os: "+str(total_o)+"\n")
        file.write("Total Us: "+str(total_u))

# Question 03: RECURSION
# Determine if "KOBEEBOK" is an anagram using recursion
def recursion(word):
    if word == '':
        return True
    elif word[0] != word[-1]:
        return False
    else:
        return recursion(word[1:-1])

# Question 04: ALGORITHMS
# Given the arrays and their associated algorithms, write on a separate piece of paper
# how the algorithm would run (sort/search) on that array and what the time complexity
# is for all three cases (best/average/worst)
def algos():
    # linear search (target = 42)
    arr1 = [7, 23, 6, 8, 4, 2, 6, 8, 23, 42, 87, 23, 7, 34]

    # binary search (target = 24)
    arr2 = [1, 65, 3, 6, 8, 9, 65, 87, 0, 34, 2, 54, 24]
    
    # insertion sort
    arr3 = [7,4,3,2,6,7,5,4,8,3,2,5,6]

    # merge sort
    arr5 = [8321, 54, 2, 6, 88, 79, 55, 22, 12, 54, 65, 1, 3, 90, 43]

    # quick sort
    arr6 = [43, 4324, 34, 4, 6, 2, 7, 78, 99, 45, 234, 654]