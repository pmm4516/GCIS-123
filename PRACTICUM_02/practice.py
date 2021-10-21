"""
Author: Patrick Marchione

Practice exam for the practicum 02
"""

# Question 01: LOOPS
# Create a while and for loop to get every fourth character from the string and print it
def loops():
    word = "dkhflshfcnsdakjhfjladsfxdalshfcdajklhfdalxdmfjdhsmfxjdhlmjlkhmjdkhf kdlhcjkafdlshmfxjdhhdajdfmxajslmxajlhmfakxjdklxmdmhfxkjdlhfxljkdah"

    pass

# Question 02: FILES
# Read from the file "complete_nonsense.txt" and count the amount of vowels
# Then write the answers(total vowels, total As, total Es, etc) to another file

def file_problem():
    pass

# Question 03: RECURSION
# Determine if "KOBEEBOK" is an anagram using recursion
def recursion(word):
    pass

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

def main():
    loops()
    file_problem()
    recursion("KOBEEBOK")

main()