def sum_of_square_digits(num):
    """
    Calculate the sum of the squares of the digits of a given number.

    Args:
        num (int): The number for which the sum of the squares of its digits is to be calculated.

    Returns:
        int: The sum of the squares of the digits of the input number.

    Examples:
        >>> sum_of_square_digits(7)
        49
        >>> sum_of_square_digits(49)
        97
    """
    sum_sq = 0

    for n in str(num):
        sum_sq += int(n)**2

    return sum_sq


def is_happy_number(num):
    """
    Determine whether a given number is a happy number, with a limit of 10 iterations.

    A happy number is a number defined by the following process:
    Starting with any positive integer, replace the number by the sum of the squares of its digits,
    and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle
    which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

    This implementation limits the number of iterations to 10 instead of allowing for an endless loop.

    Args:
        num (int): The number to be checked for being a happy number.

    Returns:
        bool: True if the input number is a happy number within 10 iterations, False otherwise.

    Examples:
        >>> is_happy_number(7)
        True
        # 7 -> 7 ^ 2 = 49
        # 49 -> 4 ^ 2 + 9 ^ 2 = 97
        # 97 -> 9 ^ 2 + 7 ^ 2 = 130
        # 130 -> 1 ^ 2 + 3 ^ 2 + 0 ^ 2 = 10
        # 10 -> 1 ^ 2 + 0 ^ 2 = 1
    """
    i = 0
    iter_sum_sq = num

    while i < 10:
        iter_sum_sq = sum_of_square_digits(iter_sum_sq)
        i += 1
        if iter_sum_sq == 1:
            return True

    return False
