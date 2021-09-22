"""
Answers to the file problem
"""

def read_file(counter_a, counter_e, counter_i, counter_o, counter_u, counter_total):
    #Step 1: Open the file
    file = open("nonsense.txt", 'r')

    #Step 2: Read the file line by line
    for line in file:
        
    #Step 3: Get rid of extra leading/ending whitespace and stupid terminating characters
        line = line.strip()
        
    #Step 4: Break the line up iterate through them
    #Hint: Are you iterating through each word or each character in every word
        token = line.split()
        for token in line:
            for ch in token:
                if ch == 'a':
                    counter_a += 1
                    counter_total += 1
                elif ch == 'e':
                    counter_e += 1
                    counter_total += 1
                elif ch == 'i':
                    counter_i += 1
                    counter_total += 1
                elif ch == 'o':
                    counter_o += 1
                    counter_total += 1
                elif ch == 'u':
                    counter_u += 1
                    counter_total += 1

    #Step 5: Close the file
    file.close()

    return counter_a, counter_e, counter_i, counter_o, counter_u, counter_total

def write_file(counter_a, counter_e, counter_i, counter_o, counter_u, counter_total):
    #Step 6: Open new file
    file = open("file_answers.txt", 'w')

    #Step 7: Write the amount of vowels to the new file
    file.write("Total amount of vowels: "+str(counter_total)+"\n")
    file.write("Amount of A: "+str(counter_a)+"\n")
    file.write("Amount of E: "+str(counter_e)+"\n")
    file.write("Amount of I: "+str(counter_i)+"\n")
    file.write("Amount of O: "+str(counter_o)+"\n")
    file.write("Amount of U: "+str(counter_u)+"\n")

    #Step 8: Close the file
    file.close()

def main():
    counter_a = 0
    counter_e = 0
    counter_i = 0
    counter_o = 0
    counter_u = 0
    counter_total = 0

    #Don't worry about this mess, you'll learn about it later
    counter_a, counter_e, counter_i, counter_o, counter_u, counter_total = read_file(counter_a, counter_e, counter_i, counter_o, counter_u, counter_total)
    write_file(counter_a, counter_e, counter_i, counter_o, counter_u, counter_total)

main()