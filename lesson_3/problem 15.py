""" Solved 15 min 
P:  Create a function that takes a string argument that consists entirely of numeric digits and computes the greatest product of four consecutive digits.
    - the argument will always have more than 4 digits 
    I:string of numeric digits 
    O:integer greatest product of four consecutive digits 

E:

D: string and a variable 

A: 
    - create 4 string range 
    - iterate through my string with my range 
    - take each char from the range and multiply them 
    - only keep the largest product 
    - return the largest product 
"""

def greatest_product(string_number):
    k = len(string_number)
    i = 0 
    j = 4
    ans = 0
    product = 1

    while j <= k:
        for num in string_number[i:j]:
            product *= int(num)
        if product > ans:
            ans = product
        product = 1
        i += 1
        j += 1
    return ans






print(greatest_product('23456') == 360)      # 3 * 4 * 5 * 6
print(greatest_product('3145926') == 540)    # 5 * 9 * 2 * 6
print(greatest_product('1828172') == 128)    # 1 * 8 * 2 * 8
print(greatest_product('123987654') == 3024) # 9 * 8 * 7 * 6