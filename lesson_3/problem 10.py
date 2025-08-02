"""
P:  Create a function that takes a string of digits as an argument and returns
    the number of even numbered substrings that can be formed.
    for example '1432' the even numbered substrings are 14, 1432, 4, 432, 32, 2
    for a total of 6 substrings
    Rules:
    - if a substring occurs more than once you should count each occurrance 
      as a seperate substring 
E:
D:
    have a list and store even substrings in the list

A:
    1. iterate through each substring
        a. have a nested iteration to count all the substrings possible 
    2. if a substring is even add it to my list
    3. return the length of the list
"""

def even_substrings(string):
    count = 0
    for i in range(len(string)):
        j = i + 1
        while j < len(string) + 1:
            if int(string[i:j]) % 2 == 0:
                count += 1
            j += 1

    return count



print(even_substrings('1432') == 6)
print(even_substrings('3145926') == 16)
print(even_substrings('2718281') == 16)
print(even_substrings('13579') == 0)
print(even_substrings('143232') == 12)