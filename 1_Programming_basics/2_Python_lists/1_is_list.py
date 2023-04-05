def is_list(value):
    """
    Determines whether a given value is a list or not.

    Args:
        value: The value to check.

    Returns:
        True if the value is a list, False otherwise.
        
    Example:
        list_of_nums = [5, 6, 7]
        is_list([5, 6, 7]) # True
        is_list('string') # False
    """
    return type(value) == list
