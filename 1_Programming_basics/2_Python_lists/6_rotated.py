def rotated_left(item):
    """
    Rotate the elements of a sequence one position to the left.

    Args:
        item (sequence): A sequence of elements to be rotated.

    Returns:
        sequence: The input sequence with the first element moved to the end.

    Example:
        rotated_left("ABCD") # "BCDA"
    """
    return item[1:] + item[0:1]


def rotated_right(item):
    """
    Rotate the elements of a sequence one position to the right.

    Args:
        item (sequence): A sequence of elements to be rotated.

    Returns:
        sequence: The input sequence with the last element moved to the beginning.

    Example:
        rotated_right([1, 2, 3, 4])  # [4, 1, 2, 3]
    """
    return item[-1:] + item[0:-1]
