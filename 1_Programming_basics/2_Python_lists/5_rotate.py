def rotate(list):
    """
    Rotates the given list one position to the right, moving the last element to the front of the list.

    Args:
    - lst: a list of elements to be rotated

    Returns:
    - The same list after being rotated one position to the right. If the input list is empty, it returns the same empty list.

    Example:
    >>> items = [1, 2, 3]
    >>> rotate(items)
    >>> print(items)
    [3, 1, 2]
    """
    if list == []:
        return list
    return list.insert(0, list.pop())


items = [1, 2, 3]
rotate(items)
print(items)  # => [3, 1, 2]
