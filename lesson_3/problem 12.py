"""
P:  Create a function that takes a string as an argument and 
    returns True if the string is a pangram, false if its not
    Rules:
        - pangram are sentences that contain every letter of 
        the alphabet once. 
        - case is irrrelvant 
    I:  String 
    O:  Bool
E:
D: set

A:  
    1. iterate through the lowercased string 
    2. add all alphabetical characters to a set
    3. return if set length is 26
"""
def is_pangram(string):
    ans = set()
    for letter in string.lower():
        if letter.isalpha():
            ans.add(letter)
    return len(ans) == 26






print(is_pangram('The quick, brown fox jumps over the lazy dog!') == True)
print(is_pangram('The slow, brown fox jumps over the lazy dog!') == False)
print(is_pangram("A wizard’s job is to vex chumps quickly in fog.") == True)
print(is_pangram("A wizard’s task is to vex chumps quickly in fog.") == False)
print(is_pangram("A wizard’s job is to vex chumps quickly in golf.") == True)

my_str = 'Sixty zippers were quickly picked from the woven jute bag.'
print(is_pangram(my_str) == True)