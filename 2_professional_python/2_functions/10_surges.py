def greet(name, surname):
    return f"Hello, {name} {surname}!"


def partial_apply(func, first_arg):
    """Returns a new function that partially applies the given function 'func' with the provided 'first_arg'.

    Args:
        func (function): The function to be partially applied.
        first_arg (Any): The first argument to be passed to 'func' when the new function is called.

    Returns:
        function: A new function that takes a second argument and applies 'func' to 'first_arg' and the second argument.

    Example:
        >>> f = partial_apply(greet, "Dorian")
        >>> f("Grey")
        'Hello, Dorian Grey!'
    """

    def second_function(second_arg):
        return func(first_arg, second_arg)

    return second_function


def flip(function):
    """Returns a new function that flips the order of arguments when calling the given 'function'.

    Args:
        function (function): The function to be flipped.

    Returns:
        function: A new function that takes two arguments and applies 'function' to the arguments in reverse order.

    Example:
        >>> f = flip(greet)
        >>> f("Christian", "Teodor")
        'Hello, Teodor Christian!'
    """

    def second_function(name, surname):
        return function(surname, name)

    return second_function
