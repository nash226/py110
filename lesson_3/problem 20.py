def what_is_different(lst):

    count = {}
    for num in lst:
        count[num] = count.get(num, 0) + 1

    for k, v in count.items():
        if v == 1:
            return k





print(what_is_different([0, 1, 0]) == 1)
print(what_is_different([7, 7, 7, 7.7, 7]) == 7.7)
print(what_is_different([1, 1, 1, 1, 1, 1, 1, 11, 1, 1, 1, 1]) == 11)
print(what_is_different([3, 4, 4, 4]) == 3)
print(what_is_different([4, 4, 4, 3]) == 3)