"""
Final Practical Review 1
Units 1-5
"""

import turtle

# Question 1
# Enter your name and print it out
def name():
    print(input("Enter your name: "))

# Question 2
# Now draw a square
def tt():
    for x in range(4):
        turtle.forward(100)
        turtle.left(90)
    turtle.done()

# Question 3
# Read through the declaration of independence and grab every vowel and count em and write it to another file
def independence():
    count = 0
    a = 0
    e = 0
    i = 0
    o = 0
    u = 0

    file = open("C:/Users/march/Desktop/2021-22/Fall/GCIS123/GCIS-123/EXAM_REVIEW/UNIT 1-5/suck-it-england.txt")
    for line in file:
        for word in line.strip().split(" "):
            for ch in word:
                if ch == 'a':
                    a+=1
                    count+=1
                elif ch == 'i':
                    i+=1
                    count+=1
                elif ch == 'e':
                    e+=1
                    count+=1
                elif ch == 'o':
                    o+=1
                    count+=1
                elif ch == 'u':
                    u+=1
                    count+=1
    
    file = open("UNIT 1-5/answers.txt", 'w')
    file.write("Total count: "+str(count)+"\n")
    file.write("A count: "+str(a)+"\n")
    file.write("E count: "+str(e)+"\n")
    file.write("I count: "+str(i)+"\n")
    file.write("O count: "+str(o)+"\n")
    file.write("U count: "+str(u))


def main():
    name()
    tt()
    independence()

main()