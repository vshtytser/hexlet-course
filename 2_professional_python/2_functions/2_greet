def greet(name, *names):
    """
    Generate a greeting message for one or more names.

    Args:
        name (str): The first name to be included in the greeting.
        *names (str): Additional names to be included in the greeting.

    Returns:
        str: The greeting message.

    Examples:
        >>> greet("Bob")
        'Hello, Bob!'

        >>> greet("Moe", "Mary")
        'Hello, Moe and Mary!'

        >>> greet(*"ABC")
        'Hello, A and B and C!'
    """
    names_list = [name]
    for n in names:
        names_list.append(n)
    names_str = " and ".join(names_list)
    return f"Hello, {names_str}!"
