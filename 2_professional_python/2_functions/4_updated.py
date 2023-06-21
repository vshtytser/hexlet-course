def updated(dict_in, **ys):
    """
    Merge the key-value pairs from `dict_in` and additional keyword arguments (`ys`) into a new dictionary.

    Parameters:
        dict_in (dict): The input dictionary containing key-value pairs to be merged.
        **ys: Additional keyword arguments representing key-value pairs to be merged.

    Returns:
        dict: A new dictionary containing the merged key-value pairs.

    Examples:
        d = {"a": 1, "b": False}

        updated(d, a=2, b=True, c=None)
        # {'a': 2, 'b': True, 'c': None}

        updated(d) == d
        # True

        updated(d) is d
        # False
    """
    new_dict = {}
    new_dict.update(dict_in)
    new_dict.update(ys)
    return new_dict
