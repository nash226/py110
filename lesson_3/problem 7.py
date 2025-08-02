"""
P:  create a function that takes a list of integers as an argument and returns
    the number of identical pairs in that list

    i: list of int
    o: number of identical pairs 
    Rules:
        - if the list is empty or contains exactly one item return 0
    if a certain number occurs more than twice, count each pair once 
E:   
D: 
dictionary / set 

A: 
    1. iterate through my list 
    2. check if item is in set
    3. if item is not in set add to set 
    4. it item is in set then pop the item from set and add +1 to count 
    5. repeat 2 - 4 until through iteration
    6. return counter 
"""

def pairs(lst):

    holder = set()
    count = 0
    for num in lst:
        if num in holder:
            holder.remove(num)
            count += 1
        else:
            holder.add(num)
    return count

print(pairs([3, 1, 4, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7]) == 3)
print(pairs([2, 7, 1, 8, 2, 8, 1, 8, 2, 8, 4]) == 4)
print(pairs([]) == 0)
print(pairs([23]) == 0)
print(pairs([997, 997]) == 1)
print(pairs([32, 32, 32]) == 1)
print(pairs([7, 7, 7, 7, 7, 7, 7]) == 3)
