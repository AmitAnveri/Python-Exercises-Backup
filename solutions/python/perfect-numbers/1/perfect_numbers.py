def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number <= 0 :
        raise ValueError("Classification is only possible for positive integers.")
    aliquot_sumsum = 0
    for num in range(1, number//2 + 1):
        if number % num == 0 :
              aliquot_sumsum += num
    if aliquot_sumsum > number:
        return "abundant"
    elif aliquot_sumsum < number:
        return "deficient"
    else:
        return "perfect"
