def square(number):
    if number < 1 or number > 64:
        raise ValueError("square must be between 1 and 64")
    res = 1
    for _ in range(number-1):
        res *= 2
    return res


def total():
    return sum(square(i) for i in range(1, 65))
