def diff_keys(old_dict, new_dict):
    """
    Returns a dictionary that represents the difference between two dictionaries in terms of keys.

    Args:
        old_dict (dict): The original dictionary.
        new_dict (dict): The updated dictionary.

    Returns:
        dict: A dictionary containing the following key-value pairs:
              - 'kept': A set of keys that exist in both old_dict and new_dict.
              - 'added': A set of keys that are present in new_dict but not in old_dict.
              - 'removed': A set of keys that are present in old_dict but not in new_dict.

    Examples:
        >>> diff_keys({"name": "Bob", "age": 42}, {})
        {'kept': set(), 'added': set(), 'removed': {'name', 'age'}}

        >>> diff_keys({}, {"name": "Bob", "age": 42})
        {'kept': set(), 'added': {'name', 'age'}, 'removed': set()}

        >>> diff_keys({"a": 2}, {"a": 1})
        {'kept': {'a'}, 'added': set(), 'removed': set()}
    """
    old_set = set(old_dict.keys())
    new_set = set(new_dict.keys())

    kept_val = old_set & new_set
    added_val = new_set - old_set
    removed_val = old_set - new_set

    new_dict = {}
    new_dict["kept"] = kept_val
    new_dict["added"] = added_val
    new_dict["removed"] = removed_val
    return new_dict
