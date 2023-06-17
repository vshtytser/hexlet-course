def all_unique(iter_obj):
    """
    Check if all elements in the given iterable object are unique.

    Args:
        iter_obj: An iterable object.

    Returns:
        bool: True if all elements are unique, False otherwise.

    Examples:
        >>> all_unique([])
        True

        >>> all_unique([1, 2, 3])
        True

        >>> all_unique(iter([1, 2, 3, 2]))
        True

        >>> all_unique([1, 2, 1])
        False
    """
    items_list = list(iter_obj)
    items_set = set(items_list)
    return len(items_list) == len(items_set)
