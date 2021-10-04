"""
Author: Patrick Marchione

Goal: Have the user enter a number
From that number, build a loop to determine how many multiples of 7 are less than that number
Then transform that loop in a recursive function that does the same thing

Have the user enter their favorite fruit
Build a loop to reverse the string
Then transform that loop into a recursive function

Write some TDD tests for it for extra practice
"""

def number_loop(number):
    counter = 0
    sevens = 0

    while True:
        if counter > number:
            break
        else:
            sevens += 1
            counter += 7
    
    return sevens

def number_recursion(number, sevens, counter):
    if counter > number:
        return sevens
    else:
        return number_recursion(number, sevens+1, counter+7)

def string_loop(word):
    answer = ""

    while True:
        if word == "":
            break
        else:
            answer = answer + word[-1]
            word = word[0:-1]

    return answer

def string_recursion(word, answer):
    if word == "":
        return answer
    else:
        return string_recursion(word[0:-1], answer = answer + word[-1])

def main():
    print(number_loop(43))
    print(number_recursion(43, 0, 0))
    print(string_loop("kobe"))
    print(string_recursion("kobe", ""))

if __name__ == "__main__":
    main()