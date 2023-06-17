def toggle(flag, cur_set):
    """
    Toggle the presence of a flag in the given set.

    If the flag is already present in the set, it is removed.
    If the flag is not present in the set, it is added.

    Args:
        flag: The flag to toggle.
        cur_set: The set to modify.

    Returns:
        None

    Examples:
        >>> flags = set()
        >>> toggle("read_only", flags)
        >>> "read_only" in flags
        True

        >>> toggle("read_only", flags)
        >>> "read_only" in flags
        False
    """
    if flag in cur_set:
        cur_set.discard(flag)
    else:
        cur_set.add(flag)


def toggled(flag, cur_set):
    """
    Toggle the presence of a flag in the given set, returning a new set.

    If the flag is already present in the set, it is removed in the new set.
    If the flag is not present in the set, it is added in the new set.

    Args:
        flag: The flag to toggle.
        cur_set: The set to operate on.

    Returns:
        set: A new set with the flag toggled.

    Examples:
        >>> flags = set()
        >>> new_flags = toggled("read_only", flags)
        >>> "read_only" in flags
        False
        >>> "read_only" in new_flags
        True
    """
    new_set = cur_set.copy()
    if flag in cur_set:
        new_set.discard(flag)
    else:
        new_set.add(flag)
    return new_set
