"""
P:  create a function that takes a list of integers as an argument
    The function should return the minimum sum of 5 consecutive numbers
    in the list. if the list contains fewer than 5 elements the function 
    should return None.

    I: list of integers
    O: integer (minimum sum of 5 consecutive numbers in that list)

    Rules:
    if less than 5 elements return none 

E:
print(minimum_sum([1, 2, 3, 4]) is None)
print(minimum_sum([1, 2, 3, 4, 5, -5]) == 9)
print(minimum_sum([1, 2, 3, 4, 5, 6]) == 15)
print(minimum_sum([55, 2, 6, 5, 1, 2, 9, 3, 5, 100]) == 16)
print(minimum_sum([-1, -5, -3, 0, -1, 2, -4]) == -10)

D: array and some variable pointers 

A: 
    1. create a 5 element sub array
    2. find the sum of the sub array
    3. store the sum in an answer array 
    4. slide the array to the right until we reach the end 
    5. repeat steps 2,3
    6. find the minimum value in the answer array
"""
def minimum_sum(int_list):
    if len(int_list) < 5:
        return None
    elif len(int_list) == 5:
        return min(int_list)
    else:
        ans = []
        i = 0
        j = 4
        while j < len(int_list):
            ans.append(sum(int_list[i:j+1]))
            i += 1
            j += 1
        return min(ans)

print(minimum_sum([1, 2, 3, 4]) is None)
print(minimum_sum([1, 2, 3, 4, 5, -5]) == 9)

print(minimum_sum([1, 2, 3, 4, 5, 6]) == 15)
print(minimum_sum([55, 2, 6, 5, 1, 2, 9, 3, 5, 100]) == 16)
print(minimum_sum([-1, -5, -3, 0, -1, 2, -4]) == -10)