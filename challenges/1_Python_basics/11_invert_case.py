def invert_case(str):
    """
    Inverts the case of each character in the given string.

    This function takes a string as input and returns a new string with the case of each
    character inverted. Uppercase characters are converted to lowercase, and lowercase
    characters are converted to uppercase. Non-alphabetic characters remain unchanged.

    Args:
        (str): The input string for which the case of each character needs to be inverted.

    Returns:
        str: A new string with the case of each character in the input string inverted.

    Example:
        >>> invert_case("Hello, World!")
        'hELLO, wORLD!'
        >>> invert_case("I love Python")
        'i LOVE pYTHON'
    """
    inverted_case_str = ''

    for letter in str:
        if letter.isupper():
            inverted_case_str += letter.lower()

        elif letter.islower():
            inverted_case_str += letter.upper()

        else:
            inverted_case_str += letter
    return inverted_case_str
