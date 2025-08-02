"""
P:  Create a function that takes two string arguments and returns the number 
    of times that the second string occurs in the first string 

    I: two strings
    O: integer (how many times the second string occurs in the first)

E:


D: 
    string or an array 

A: 
    1. compute the length of the second string arg 
    2. set two pointers with the width (1.)
    3. slide through the first string looking for substring match
    4. if match add to counter
    5. once finished iterating -- return counter
"""

def count_substrings(string1, string2):
    i = 0
    j = 0
    count = 0
    while i < len(string1):

        if string1[i] == string2[j]:
            j += 1 
            i += 1

        else:
            i += 1
        
        if j == len(string2):
            count += 1
            j = 0

    return(count)


print(count_substrings('babab', 'bab') == 1)
print(count_substrings('babab', 'ba') == 2)
print(count_substrings('babab', 'b') == 3)
print(count_substrings('babab', 'x') == 0)
print(count_substrings('babab', 'x') == 0)
print(count_substrings('', 'x') == 0)
print(count_substrings('bbbaabbbbaab', 'baab') == 2)
print(count_substrings('bbbaabbbbaab', 'bbaab') == 2)
print(count_substrings('bbbaabbbbaabb', 'bbbaabb') == 1)
