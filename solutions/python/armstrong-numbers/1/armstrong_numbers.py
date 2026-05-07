def is_armstrong_number(number):
    copy = number
    number_of_digits = len(str(number))
    res = 0
    while copy:
        rem = copy % 10
        res += pow(rem,number_of_digits)
        copy = copy // 10
    return res == number