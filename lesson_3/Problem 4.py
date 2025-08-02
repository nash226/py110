"""
P:  Create a fucntion that takes a list of 
integeers as an argument and returns a tuple of two numbers that are
closest together in value (min difference). if there are multiple pairs that
are equally close, return the pair that occurs first in the list.

    I: list of integers
    O: a tuple of two numbers that are closest together

    Rules if there are multiple pairs that are equally close, return the 
    pair that occurs first in the list

E:
print(closest_numbers([5, 25, 15, 11, 20]) == (15, 11))
print(closest_numbers([19, 25, 32, 4, 27, 16]) == (25, 27))
print(closest_numbers([12, 22, 7, 17]) == (12, 7))
(1, 2, 4)


D: list 

A: 
    1. iterate through all the pairs in the list 
    2. find the difference for all the pairs 
    3. store the difference and the locations of the indexes
    4. return the values of the pair with the smallest difference 

"""
def closest_numbers(int_list):

    holder = []

    for i in range(len(int_list)):
        for j in range(i + 1, len(int_list)):
            diff = abs(int_list[i] - int_list[j])
            holder.append(((int_list[i], int_list[j]), diff))
  

    closest_pair = min(holder, key=lambda x: x[1])

    return(closest_pair[0])


print(closest_numbers([5, 25, 15, 11, 20]) == (15, 11))
print(closest_numbers([19, 25, 32, 4, 27, 16]) == (25, 27))
print(closest_numbers([12, 22, 7, 17]) == (12, 7))