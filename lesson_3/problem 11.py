"""
P: Create a function that takes a non empty string as an argument and returns 
    a tuple consisting of a string and an integer 
    I: nonempty string 
    O: tuple consisting of a string and an integer 
    Rules:
        -if we call the string arguemnt s 
        - the string component of the tuple t and the integer is k
        - then s, t, and k must be related to each other such that s == t * k
        - we can assume string argument is only lowercase alphabet letters
        - t and k  (t should be the shortest substring) k should be the most repeated that satisfies this equation

D: dictionary to hold substrings and counts

A:  1. calculate all substrings and store counts in a dicitonary
    2. iterate through the dictionary and find the max count and return that with the substring 

"""

def repeated_substring (string):

    sub_dict = {}
    ans = []
    tuple = ()
    for i in range(len(string)):
        j = i + 1
        while j <= len(string):
            sub_dict[string[i:j]] = sub_dict.get(string[i:j], 0) + 1
            j+= 1
    for t, k in sub_dict.items():
        if t * k == string:
            return(t, k)


print(repeated_substring('xyzxyzxyz') == ('xyz', 3))
print(repeated_substring('xyxy') == ('xy', 2))
print(repeated_substring('xyz') == ('xyz', 1))
print(repeated_substring('aaaaaaaa') == ('a', 8))
print(repeated_substring('superduper') == ('superduper', 1))
