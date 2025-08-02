"""
P:  create a function that takes a string argument and returns the character
    that occurs most often in the string. If there are multiple characters with
    the same greatest frequency, return the one that appears first in the string
    when counting characters, consider uppercase and lowercase to be same 
    I: string
    O: string (char that occurs most)

    Rules:
    - consider uppercase char and lowercase to be the same 
E:

D: 
    Dictionary
    dictionary view object

A:
    1. get a count of all the letters in the string 
    2. find a max count
    3. compare all others to that count
    4. if there are no others greater 
    5. return the max count character

"""

def most_common_char(string):
    count = {}
    ans = ''
    for char in string.lower():
        count[char] = count.get(char, 0) + 1
    max = 0
    for key, value in count.items():
        if value > max:
            max = value
            ans = key
    return ans


print(most_common_char('Hello World') == 'l')
print(most_common_char('Mississippi') == 'i')
print(most_common_char('Happy birthday!') == 'h')
print(most_common_char('aaaaaAAAA') == 'a')

my_str = 'Peter Piper picked a peck of pickled peppers.'
print(most_common_char(my_str) == 'p')

my_str = 'Peter Piper repicked a peck of repickled peppers. He did!'
print(most_common_char(my_str) == 'e')
