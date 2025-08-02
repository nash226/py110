""" Solved 17 min
P: Create a function that takes a list of integers as an argument. Determine are return the index N for which all numbers with an index less that N sum to the same value as the numbers with an index greater than N. If there is no index that would make this happen return - 1

    I: a list of integers
    O: integer index N 

E:
D: variables and list slicing

A:
    1. set my slice point (n)
    2. compare everything to lefts sum with the rights sum 
    3. return a (n) with a difference of 0
"""

def equal_sum_index(lst):
    n = 0
    left = lst[:n]
    right = lst[n + 1:]

    while n <= len(lst):
        left = lst[:n]
        right = lst[n + 1:]
        if sum(left) == sum(right):
            return n
        n += 1

    return -1

print(equal_sum_index([1, 2, 4, 4, 2, 3, 2]) == 3)
print(equal_sum_index([7, 99, 51, -48, 0, 4]) == 1)
print(equal_sum_index([17, 20, 5, -60, 10, 25]) == 0)
print(equal_sum_index([0, 2, 4, 4, 2, 3, 2]) == -1)

# The following test case could return 0 or 3. Since we're
# supposed to return the smallest correct index, the correct
# return value is 0.
print(equal_sum_index([0, 20, 10, -60, 5, 25]) == 0)