def find_second_index(search_item, sequence):
    """
    Returns the index of the second occurrence of the specified search item in the given sequence.

    Args:
        search_item: The element to search for.
        sequence: The sequence to search in.

    Returns:
        The index of the second occurrence of the search item, or None if it does not occur twice in the sequence.

    Examples:
        find_second_index('b', 'bob')  # 2
        find_second_index('a', 'cat') is None  # True
    """
    item_occurence = 0

    for index, value in enumerate(sequence):
        if value == search_item:
            item_occurence += 1
            if item_occurence == 2:
                return index

    return None
