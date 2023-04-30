def is_continuous_sequence(list_sq):
    """
    Determines if the input list of integers forms a continuous sequence.

    Args:
        list_sq (list of int): The input list of integers to check.

    Returns:
        bool: True if the input list forms a continuous sequence, False otherwise.

    Examples:
        >>> is_continuous_sequence([10, 11, 12, 13])
        True
        >>> is_continuous_sequence([-5, -4, -3])
        True
        >>> is_continuous_sequence([1, 2, 2, 3])
        False
        >>> is_continuous_sequence([5, 3, 2, 8])
        False
        >>> is_continuous_sequence([7])
        False
        >>> is_continuous_sequence([])
        False
        >>> is_continuous_sequence([10, 11, 12, 14, 15])
        False
        >>> is_continuous_sequence([0, 1, 2, 3])
        True
    """
    if len(list_sq) <= 1:
        return False

    new_list = [list_sq[0]]

    for num in list_sq[1:]:
        if num == int(new_list[-1]) + 1:
            new_list.append(num)

    return len(new_list) == len(list_sq)
