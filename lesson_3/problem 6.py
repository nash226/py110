"""
P: create a function that takes a string argument and returns a dict object
in which the keys represent the lowercase letters in the string and the values
represent how often the corresponding letter occurs in the string 
I: string 
O: Dictionary with the lowercase letters as keys and their count as values
    Rules:
    empty string returns an empty dictionary

E:

D: dictionary 

A:
    1. iterate through string
    2. if character is lowercase add it as a key and its count as the value
    3. continue iterating and updating count if already seen 
    4. return dictionary
"""

def count_letters(string):
    ans = {}
    for char in string:
        if char.islower():
            ans[char] = ans.get(char, 0) + 1
    return ans 


expected = {'w': 1, 'o': 2, 'e': 3, 'b': 1, 'g': 1, 'n': 1}
print(count_letters('woebegone') == expected)

expected = {'l': 1, 'o': 1, 'w': 1, 'e': 4, 'r': 2,
            'c': 2, 'a': 2, 's': 2, 'u': 1, 'p': 2}
print(count_letters('lowercase/uppercase') == expected)

expected = {'u': 1, 'o': 1, 'i': 1, 's': 1}
print(count_letters('W. E. B. Du Bois') == expected)

print(count_letters('x') == {'x': 1})
print(count_letters('') == {})
print(count_letters('!!!') == {})
