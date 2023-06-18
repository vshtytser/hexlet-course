def get_or_default(m, key, def_val):
    """
    Retrieves the value associated with a key from a map (dictionary) or returns a default value if the key is not found.

    Args:
        m (dict): The map (dictionary) from which to retrieve the value.
        key: The key to search for in the map.
        def_val: The default value to return if the key is not found.

    Returns:
        The value associated with the key in the map if found, or the default value if the key is not present.

    Examples:
        >>> m = make_map()
        >>> m.set("g", "bar")
        >>> m.set("e", "foo")
        >>> get_or_default(m, "g", "python")
        'bar'
        >>> get_or_default(m, "a", "python")
        'python'
    """
    value_index = get_hash(key)  # 2
    map_value = m[value_index]  # ('e', 'hello')
    if map_value is None:
        return def_val
    else:
        pair_key, pair_value = map_value
        return pair_value
