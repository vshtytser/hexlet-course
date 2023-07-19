def length(list_):
    """
    Calculate the length of a given list recursively.

    Parameters:
        list_ (list): The list for which the length is to be calculated.

    Returns:
        int: The length of the list.

    Examples:
        >>> length([])
        0
        >>> length([1, 2, 3])
        3
        >>> length(['a', 'b', 'c', 'd'])
        4
    """
    if not list_:
        return 0
    else:
        return 1 + length(list_[1:])


def reverse_range(begin, end):
    """
    Generate a list of integers in reverse order within the specified range [begin, end].

    The function constructs a list of integers starting from 'end' and decrementing by 1 until 'begin' is reached,
    inclusively. The resulting list will have elements in reverse order from 'end' to 'begin'.

    Parameters:
        begin (int): The starting value of the range (inclusive).
        end (int): The ending value of the range (inclusive).

    Returns:
        list: A list of integers in reverse order within the specified range.

    Examples:
        >>> reverse_range(1, 1)
        [1]
        >>> reverse_range(1, 3)
        [3, 2, 1]
        >>> reverse_range(5, 9)
        [9, 8, 7, 6, 5]
    """
    if begin == end:
        return [begin]
    else:
        return [end] + reverse_range(begin, end - 1)


def filter_positive(list_):
    """
    Recursively filter positive integers from the given list.

    The function takes a list of integers as input and constructs a new list that contains only the positive
    integers from the original list. It does this by recursively checking each element in the list and adding
    the positive ones to the result list.

    Parameters:
        list_ (list): The list of integers to filter.

    Returns:
        list: A new list containing only the positive integers from the input list.

    Examples:
        >>> filter_positive([])
        []
        >>> filter_positive([-3])
        []
        >>> filter_positive([1, -2, 3])
        [1, 3]
        >>> filter_positive([-1, -2, -3])
        []
        >>> filter_positive([0, 1, 2, 3])
        [1, 2, 3]
    """
    if not list_:
        return []

    # Check if the first element is positive
    if list_[0] > 0:
        return [list_[0]] + filter_positive(list_[1:])
    else:
        return filter_positive(list_[1:])
