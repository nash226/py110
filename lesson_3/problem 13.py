""" Solved 16 min

P:  Create a function that takes two strings as arguments and 
    returns True if some portion of the characters of the first string can be 
        rearranged to match the characters in the second.
        otherwise the function should return false. 
    Rules:
        -both string arguments only contain lowercase alpha
        -neither string will be empty 
    I: 2 strings
    O: boolean 

E:
D: Dictionary 

A:
    1. Create two dictionaries for each string 
    2. compare the key value of the second with the first 
    3. if they all are the same then return True
    4. else return false 
"""
def unscramble(string1, string2):
    
    string1_dict = {}
    string2_dict = {}

    for letter in string1:
        string1_dict[letter] = string1_dict.get(letter, 0) + 1

    for char in string2:
        string2_dict[char] = string2_dict.get(char, 0) + 1

    for k, v in string2_dict.items():
        if string1_dict.get(k) != v:
            return False 
            
    return True 



print(unscramble('ansucchlohlo', 'launchschool') == True)
print(unscramble('phyarunstole', 'pythonrules') == True)
print(unscramble('phyarunstola', 'pythonrules') == False)
print(unscramble('boldface', 'coal') == True)
print(unscramble('olc', 'cool') == False)