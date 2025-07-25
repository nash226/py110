def less_than(upper_limit):
    numbers = []

    for candidate in range(1, upper_limit):
        numbers.append(candidate)

    return numbers

print(less_than(5))