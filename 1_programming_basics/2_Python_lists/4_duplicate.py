def duplicate(list):
    """
    Extends the input list with a copy of itself, effectively duplicating its contents.

    Args:
        list: A list of elements to be duplicated.

    Returns:
        None. The input list is modified in place.

    Example:
        items = [1, 2]
        duplicate(items)  # nothing is returned
        print(items)  # => [1, 2, 1, 2]
    """
    list.extend(list)
