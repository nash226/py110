""" Solved in 7 min
P: Create a function that takes a list of integers as an argument and returns the integer that appears an odd number of times. 
    Rules:
        -there will always be exactly one such integer in the input list
    I: list of integers
    O: integer that appears an odd number of times 
E:

D: Dictionary

A:
    1. create a dictionary with the count of the list nums
    2. iterate through the dictionary to find the odd count 
    3. return the odd count integer
"""

def odd_fellow(lst):
    count = {}
    for num in lst:
        count[num] = count.get(num, 0) + 1
    
    for k, v in count.items():
        if v % 2 == 1:
            return k


print(odd_fellow([4]) == 4)
print(odd_fellow([7, 99, 7, 51, 99]) == 51)
print(odd_fellow([7, 99, 7, 51, 99, 7, 51]) == 7)
print(odd_fellow([25, 10, -6, 10, 25, 10, -6, 10, -6]) == -6)
print(odd_fellow([0, 0, 0]) == 0)