"""
Work in pairs to solve this problem involing File I/O
Bonus points if you use the method that allows you to skip step 5 & step 8
Have fun
"""

def read_file(counter_a, counter_e, counter_i, counter_o, counter_u, counter_total):
    #Step 1: Open the file


    #Step 2: Read the file line by line
    
        
    #Step 3: Get rid of extra leading/ending whitespace and stupid terminating characters
        
        
    #Step 4: Break the line up iterate through them
    #Hint: Are you iterating through each word or each character in every word
        

    #Step 5: Close the file
    

    return counter_a, counter_e, counter_i, counter_o, counter_u, counter_total

def write_file(counter_a, counter_e, counter_i, counter_o, counter_u, counter_total):
    #Step 6: Open new file
    

    #Step 7: Write the amount of vowels to the new file
    

    #Step 8: Close the file

    #Delete this word when answering the problem - it is useless
    pass

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