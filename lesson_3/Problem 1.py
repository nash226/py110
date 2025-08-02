"""
p:  create a function that takes a list of numbers as an argument
    for each number determine how many numbers in the list 
    are smaller than it, and place the ansewr in a list. 
    Return the resulting list
    I: list of numbers
    O: list of numbers smaller than that 

    rules we dont count duplicates 
    if all the numbers are the same we return 0
    if only one number we return 0


E:
print(smaller_numbers_than_current([8, 1, 2, 2, 3]) == [3, 0, 1, 1, 2])
print(smaller_numbers_than_current([7, 7, 7, 7]) == [0, 0, 0, 0])
print(smaller_numbers_than_current([6, 5, 4, 8]) == [2, 1, 0, 3])
print(smaller_numbers_than_current([1]) == [0])

my_list = [1, 4, 6, 8, 13, 2, 4, 5, 4]
result   = [0, 2, 4, 5, 6, 1, 2, 3, 2]
print(smaller_numbers_than_current(my_list) == result)

D:  list and dict

A:
    create an empty list
    create an empty dict
    store all the values in the dict 
    compare each value to see < or >=
    update a count if conditions are met 
    put the count in the list
"""

def smaller_numbers_than_current(num_list):
    ans = []
    number_dict = {}
    for num in num_list:
        number_dict[num] = number_dict.get(num, 0) + 1
    
    for num in num_list:
        count = 0
        for number in number_dict.keys():
            if num > number:
                count += 1
        ans.append(count)

    return ans



print(smaller_numbers_than_current([8, 1, 2, 2, 3]) == [3, 0, 1, 1, 2])
print(smaller_numbers_than_current([7, 7, 7, 7]) == [0, 0, 0, 0])
print(smaller_numbers_than_current([6, 5, 4, 8]) == [2, 1, 0, 3])
print(smaller_numbers_than_current([1]) == [0])

my_list = [1, 4, 6, 8, 13, 2, 4, 5, 4]
result   = [0, 2, 4, 5, 6, 1, 2, 3, 2]
print(smaller_numbers_than_current(my_list) == result)

