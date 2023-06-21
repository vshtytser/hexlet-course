def get_unique(*lists):
    """
    Returns a list containing unique elements from the given input lists.

    Args:
        *lists: Variable number of lists.

    Returns:
        list: A new list containing only the unique elements from the input lists.

    Examples:
        >>> get_unique([1, 2, 3], [3, 4, 5], [5, 6, 7])
        [1, 2, 3, 4, 5, 6, 7]
    """
    all_items_list = []
    for item in lists:
        all_items_list.extend(item)

    unique_items_list = []
    for item in all_items_list:
        if item not in unique_items_list:
            unique_items_list.append(item)

    return unique_items_list
