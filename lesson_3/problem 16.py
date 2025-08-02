""" Solved in 7 minutes 
P: Create a function that returns the count of distinct case - insensitive alphabetic characters and numeric digits that occur more than once in the input string. 
    Rules:
    - you may assume that the input string only contains alphanumeric characters

E: 

D: Dictionary 
A:
    1. create a dictionary with the counts of lowercase char
    2. iterate through key value pairs 
    3. if value > 1 then add to count 
    4. return count 
"""

def distinct_multiples(string):

    count_dict = {}
    count = 0
    
    for letter in string.lower():
        count_dict[letter] = count_dict.get(letter, 0) + 1
    
    for v in count_dict.values():
        if v > 1:
            count += 1

    return count


print(distinct_multiples('xyz') == 0)               # (none)
print(distinct_multiples('xxyypzzr') == 3)          # x, y, z
print(distinct_multiples('xXyYpzZr') == 3)          # x, y, z
print(distinct_multiples('unununium') == 2)         # u, n
print(distinct_multiples('multiplicity') == 3)      # l, t, i
print(distinct_multiples('7657') == 1)              # 7
print(distinct_multiples('3141592653589793') == 4)  # 3, 1, 5, 9
print(distinct_multiples('2718281828459045') == 5)  # 2, 1, 8, 4, 5