from functools import wraps
from collections import OrderedDict


def memoizing(arg):
    """
    Memoizes the results of a function based on its input values, with a specified cache size.

    Args:
        arg (int): The maximum number of input values to cache.

    Returns:
        A decorator function that memoizes the input function.

    Examples:
        >>> @memoizing(3)
        ... def f(x):
        ...     print("Calculating...")
        ...     return x * 10

        >>> f(1)
        Calculating...
        10

        >>> f(1)  # Recalls the previously cached result
        10

        >>> f(2)
        Calculating...
        20

        >>> f(3)
        Calculating...
        30

        >>> f(4)  # Evicts the cached result for "1"
        Calculating...
        40

        >>> f(1)  # Recalculates the result for "1"
        Calculating...
        10
    """

    def decorator(function):
        memory = OrderedDict()

        @wraps(function)
        def inner(x):
            if x in memory:
                return memory[x]
            elif len(memory) >= arg:
                memory.popitem(last=False)
            memory[x] = function(x)
            return memory[x]

        return inner

    return decorator
