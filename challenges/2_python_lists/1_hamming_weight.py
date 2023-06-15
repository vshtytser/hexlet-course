def hamming_weight(num):
    """
    Calculate the Hamming weight (number of set bits) of an integer.

    The function converts the input integer to its binary representation and
    counts the number of '1's (set bits) in the binary string.

    Args:
        num (int): The integer for which the Hamming weight is to be calculated.

    Returns:
        int: The Hamming weight (number of set bits) of the input integer.

    Examples:
        >>> hamming_weight(0)
        0
        >>> hamming_weight(4)
        1
        >>> hamming_weight(101)
        4
    """
    bi_num = f'{num:b}'

    return bi_num.count('1')
