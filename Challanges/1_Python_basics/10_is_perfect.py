def is_perfect(num):
    """Check if a number is perfect.

    A perfect number is a positive integer that is equal to the sum of its proper divisors.
    For example, the number 28 is perfect because its proper divisors are 1, 2, 4, 7, and 14,
    and 1 + 2 + 4 + 7 + 14 = 28.

    Args:
        num (int): A positive integer to check.

    Returns:
        bool: True if the number is perfect, False otherwise.

    Examples:
        >>> is_perfect(6)
        True
        >>> is_perfect(28)
        True
        >>> is_perfect(1)
        False
    """
    if num <= 1 or num % 1 != 0:
        return False

    list_perf_divs = []
    for n in range(1, num):


    if num <= 1 or num % 1 != 0:
        return False

    list_perf_divs = []
    for n in range(1, num):
        if num % n == 0:
            list_perf_divs.append(n)

    return sum(list_perf_divs) == num
