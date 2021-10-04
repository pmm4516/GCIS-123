"""
Author: Patrick Marchione

Arrays and shit

Goal of this
    - have the user input what their fav number is from 0 - 100
    - have the user input what their least fav number is from 0 - 100
    - build two random arrays (size 25) filled with random numbers
    - search through both arrays using linear search looking for their
    fav number in first array and least fav in second array
    - time both searches and see which is quicker

Write some TDD tests for it for extra practice
"""
import arrays
import random
import time

def build_array():
    fav_array = arrays.Array(25, int)
    for i in range(len(fav_array)):
        fav_array[i] = random.randint(0, 100)

    least_array = arrays.Array(25, int)
    for i in range(len(least_array)):
        least_array[i] = random.randint(0, 100)

    return fav_array, least_array

def run(fav, least_fav, fav_array, least_array):
    fav_result = False
    least_result = False
    fav_time = 0
    least_time = 0

    begin = time.perf_counter()
    for i in range(len(fav_array)):
        if fav_array[i] == fav:
            fav_result = True
            break
    end = time.perf_counter()
    fav_time = end - begin
    
    begin = time.perf_counter()
    for i in range(len(least_array)):
        if least_array[i] == least_fav:
            least_result = True
            break
    end = time.perf_counter()
    least_time = end - begin

    print("\nYour fav number was in the array:", fav_result)
    print("It took", fav_time, "to search through the array\n")
    print("Your least fav number was in the array:", least_result)
    print("It took", least_time, "to search through the array")

def main():
    fav = int(input("What is your fav number [0-100]: "))
    least_fav = int(input("What is your least fav number [0-100]: "))
    fav_array, least_array = build_array()
    run(fav, least_fav, fav_array, least_array)

if __name__ == "__main__":
    main()