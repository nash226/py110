"""
P: Create a function that take a single integer argument and returns the sum of all the multiples of 7 or 11 that are less than the argument. if a number is a multiple of both 7 and 11 just count it once. 
    Rules:
        - multiples that are less than the argument 

    I: integer
    O: integer

D: list 

A:
    1. iterate through range of the argument integer exclusive 
    2. if multiple of 7 or 11 add that to my list 
    3. return sum of my list
"""


def seven_eleven(number):

    ans = []
    if number < 0:
        return 0

    return sum([num for num in range(number) 
                if num % 7 == 0 or num % 11 == 0])

    for num in range(number):
        if num % 7 == 0 or num % 11 == 0:
            ans.append(num)
    return sum(ans)

print(seven_eleven(10) == 7)
print(seven_eleven(11) == 7)
print(seven_eleven(12) == 18)
print(seven_eleven(25) == 75)
print(seven_eleven(100) == 1153)
print(seven_eleven(0) == 0)
print(seven_eleven(-100) == 0)