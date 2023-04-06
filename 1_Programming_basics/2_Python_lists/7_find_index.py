def find_index(search_item, sequence):
    """Searches for the first occurrence of the search_item in the sequence and returns its index.

    Args:
        search_item: The item to search for in the sequence.
        sequence: The sequence to search in. Can be a list, tuple or a string.

    Returns:
        The index of the first occurrence of the search_item in the sequence, or None if the item is not found
        or the sequence is None.

    Examples:
        find_index('t', 'cat')  # 2
        find_index(5, [1, 2, 3, 4, 5, 6, 7])  # 4
        find_index(42, []) is None  # True
        find_index('!', 'abc') is None  # True
    """
    if sequence is None:
        return None

    for (index, value) in enumerate(sequence):
        if value == search_item:
            return index

    return None
