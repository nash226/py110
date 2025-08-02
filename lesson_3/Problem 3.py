"""
P:  Create a function that takes a string argument and returns a copy of
    the string with every second character in every third word converted
    to uppercase. Other characters should remain the same.

    I: string 
    O: string with every second character in every third word (index 2) converted
        to uppercase
E:
original = 'Lorem Ipsum is simply dummy text of the printing world'
expected = 'Lorem Ipsum iS simply dummy tExT of the pRiNtInG world'
print(to_weird_case(original) == expected)

original = 'It is a long established fact that a reader will be distracted'
expected = 'It is a long established fAcT that a rEaDeR will be dIsTrAcTeD'
print(to_weird_case(original) == expected)

print(to_weird_case('aaA bB c') == 'aaA bB c')

original = "Mary Poppins' favorite word is supercalifragilisticexpialidocious"
expected = "Mary Poppins' fAvOrItE word is sUpErCaLiFrAgIlIsTiCeXpIaLiDoCiOuS"
print(to_weird_case(original) == expected)

D:  variable 
    list 

A:  1.  create empty string
        iterating through each main string and find the thrid word
        if not thrid word just add to string holder
    2. iterate through each third word and uppercase the second character
    3. return the new string 
"""


def to_weird_case(my_str):
    answer = my_str.split(' ')
    result = []
    for index, word in enumerate(answer):
        
        if index % 3 == 2:
            new_word = ''
            for pos, letter in enumerate(word):
                if pos % 2 == 1:
                    new_word += letter.upper()
                else:
                    new_word += letter
            result.append(new_word)
        else:
            result.append(word)
    print(result)
    return ' '.join(result)

original = 'Lorem Ipsum is simply dummy text of the printing world'
expected = 'Lorem Ipsum iS simply dummy tExT of the pRiNtInG world'
print(to_weird_case(original) == expected)

original = 'It is a long established fact that a reader will be distracted'
expected = 'It is a long established fAcT that a rEaDeR will be dIsTrAcTeD'
print(to_weird_case(original) == expected)

print(to_weird_case('aaA bB c') == 'aaA bB c')

original = "Mary Poppins' favorite word is supercalifragilisticexpialidocious"
expected = "Mary Poppins' fAvOrItE word is sUpErCaLiFrAgIlIsTiCeXpIaLiDoCiOuS"
print(to_weird_case(original) == expected)
