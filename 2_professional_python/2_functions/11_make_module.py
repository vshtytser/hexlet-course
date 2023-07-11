def make_module(step=1):
    """Creates and returns a module-like object with 'inc' and 'dec' functions.

    Args:
        step (int, optional): The step value used for incrementing and decrementing. Defaults to 1.

    Returns:
        dict: A dictionary-like object with 'inc' and 'dec' functions.

    Example:
        >>> m = make_module()
        >>> m["inc"](10)
        11
        >>> m["dec"](20)
        19
        >>> m2 = make_module(step=2)
        >>> m2["inc"](1)
        3
    """
    return {
        "inc": lambda x: x + step,
        "dec": lambda x: x - step,
    }
