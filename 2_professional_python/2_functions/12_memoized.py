def memoized(function):
    """
    Memoizes the results of a function based on its input values.

    Args:
        function: The function to be memoized.

    Returns:
        A memoized version of the input function.

    Examples:
        >>> @memoized
        ... def f(x):
        ...     print("Calculating...")
        ...     return x * 10

        >>> f(1)
        Calculating...
        10
        >>> f(1)
        10
        >>> f(42)
        Calculating...
        420
        >>> f(42)
        420
        >>> f(1)
        10
    """
    numbers = {}

    def inner(num):
        if num in numbers:
            return numbers[num]
        else:
            numbers[num] = function(num)
            return numbers[num]

    return inner
