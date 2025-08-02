"""
P:  Create a function that takes a list of integers as an arg
    The function should determine the minimum integer value that can be appended to the list so the sum of all elements equals the closest prime number that is greater than the sum of the numbers. 
    I: list of integer
    O: integer 
    Rules:
        - the list always contains at least 2 integers
        - the list values are positive
        - we can have repeats in the list

D: list 

A:
    1. calculate the sum of the list 
    2. calculate the closest prime number greater than sum
    3. return the difference between (2) and (1)
"""

def is_prime(number):

    for num in range(2, number):
        if number % num == 0:
            return False 
    return True 


def nearest_prime_sum(lst):

    list_sum = sum(lst)
    counter = list_sum + 1

    while not is_prime(counter):
        counter += 1
    
    return counter - list_sum


print(nearest_prime_sum([1, 2, 3]) == 1)        # Nearest prime to 6 is 7
print(nearest_prime_sum([5, 2]) == 4)           # Nearest prime to 7 is 11
print(nearest_prime_sum([1, 1, 1]) == 2)        # Nearest prime to 3 is 5
print(nearest_prime_sum([2, 12, 8, 4, 6]) == 5) # Nearest prime to 32 is 37

# Nearest prime to 163 is 167
print(nearest_prime_sum([50, 39, 49, 6, 17, 2]) == 4)