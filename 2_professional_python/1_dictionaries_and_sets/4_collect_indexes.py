from collections import defaultdict


def collect_indexes(iter_obj):
    """
    Collects and returns the indexes of items in the input iterable.

    Parameters:
        iter_obj (iterable): An iterable object containing items.

    Returns:
        dict: A dictionary where each key represents an item from the input iterable,
              and the corresponding value is a list of indexes where the item occurs.

    Example:
        >>> d = collect_indexes("hello")
        >>> d["h"]
        [0]
        >>> d["e"]
        [1]
        >>> d["l"]
        [2, 3]
    """
    res_dict = defaultdict(list)
    for i, key in enumerate(iter_obj):
        res_dict[key].append(i)
    return res_dict
