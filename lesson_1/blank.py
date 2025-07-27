def join_or(lst, sep=', ', word = 'or'):
    if not lst:
        return ''
    if len(lst) == 1:
        return str(lst[0])
    if len(lst) == 2:
        return f"{lst[0]} {word} {lst[1]}"
    
    leading_items = sep.join((str(item) for item in lst[0:-1]))
    
    return f'{leading_items}{sep}{word} {lst[-1]}'



print(join_or([1, 2, 3]))               # => "1, 2, or 3"
print(join_or([1, 2, 3], '; '))         # => "1; 2; or 3"
print(join_or([1, 2, 3], ', ', 'and'))  # => "1, 2, and 3"
print(join_or([]))                      # => ""
print(join_or([5]))                     # => "5"
print(join_or([1, 2]))                  # => "1 or 2"
