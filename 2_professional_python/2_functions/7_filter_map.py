def filter_map(f, iter_obj):
    """
    Applies the function `f` to each element of `iter_obj` and filters the results based on a boolean value.

    Args:
        f: A function that takes an element from `iter_obj` as input and returns a tuple consisting of a boolean value
           and a value.
        iter_obj: An iterable containing the elements to be processed by `f`.

    Returns:
        A list of values obtained by applying `f` to each element of `iter_obj` and filtering the results based on the
        boolean value.

    Examples:
        # Example 1: Generate stars based on positive numbers
        def make_stars(x):
            if x > 0:
                return True, "*" * x
            return False, ""

        for s in filter_map(make_stars, [1, 0, 5, -5, 2]):
            print(s)
        # Output:
        # *
        # *****
        # **

        # Example 2: Safe square root calculation
        from math import sqrt

        def safe_sqrt(x):
            if x < 0:
                return False, 0
            return True, sqrt(x)

        print(filter_map(safe_sqrt, [4, -5, -2, 9]))
        # Output: [2.0, 3.0]
    """
    result = []
    for obj in iter_obj:
        boolean, value = f(obj)
        if bool(value):
            result.append(value)

    return result
