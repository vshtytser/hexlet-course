from functools import reduce
from operator import truth, getitem


def keep_truthful(iter_obj):
    """
    Filter an iterable to keep only the truthy values.

    Arguments:
    - iter_obj: An iterable object.

    Returns:
    - A filter object containing only the truthy values from the input iterable.

    Example:
    >>> list(keep_truthful([True, False, "", "foo"]))
    [True, 'foo']
    """
    return filter(truth, iter_obj)


def abs_sum(iter_nums):
    """
    Calculate the sum of the absolute values of numbers in an iterable.

    Arguments:
    - iter_nums: An iterable object containing numbers.

    Returns:
    - The sum of the absolute values of numbers in the input iterable.

    Examples:
    >>> abs_sum([-3, 7])
    10
    >>> abs_sum([])
    0
    >>> abs_sum([42])
    42
    """
    abs_iter = map(abs, iter_nums)
    return sum(abs_iter)


def walk(dict_obj, keys):
    """
    Access nested elements within a dictionary using a list of keys.

    Arguments:
    - dict_obj: A dictionary object to traverse.
    - keys: A list of keys representing the path to the desired element within the dictionary.

    Returns:
    - The value of the nested element specified by the provided keys.

    Examples:
    >>> walk({"a": {7: {"b": 42}}}, ["a", 7, "b"])
    42
    >>> walk({"a": {7: {"b": 42}}}, ["a", 7])
    {'b': 42}
    """
    return reduce(getitem, keys, dict_obj)
