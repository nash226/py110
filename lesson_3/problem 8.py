"""
P: Create a function that takes a non empty string as an argument. 
    the string consists entirely of lowercase alphabetic characters.
    the function should return the lenght of the longest vowel substring. 
    the vowels of interest are a, e, i, o, u

    I: non empty string 
    O: integer (longest vowel substring)

E:
print(longest_vowel_substring('cwm') == 0)
print(longest_vowel_substring('many') == 1)
print(longest_vowel_substring('launchschoolstudents') == 2)
print(longest_vowel_substring('eau') == 3)
print(longest_vowel_substring('beauteous') == 3)
print(longest_vowel_substring('sequoia') == 4)
print(longest_vowel_substring('miaoued') == 5)

D: list / string

A: 
    1. iterate through my string 
    2. if it is a vowel increment counter 
    3. if it is not a vowel reset counter
    4. store counters in a list
    5. return the max counter 
"""

def longest_vowel_substring(string):

    ans = []
    vowel = 'aeiou'
    count = 0
    for char in string:
        if char in vowel:
            count += 1
        else:
            count = 0
        ans.append(count)
    return max(ans)

print(longest_vowel_substring('cwm') == 0)
print(longest_vowel_substring('many') == 1)
print(longest_vowel_substring('launchschoolstudents') == 2)
print(longest_vowel_substring('eau') == 3)
print(longest_vowel_substring('beauteous') == 3)
print(longest_vowel_substring('sequoia') == 4)
print(longest_vowel_substring('miaoued') == 5)
