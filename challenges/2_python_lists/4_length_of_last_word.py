def length_of_last_word(word):
    """
    Calculate the length of the last word in a given string.

    The function takes a string as input and returns the length of the last word in that string.
    If the string is empty or contains only whitespace characters, the function returns 0.
    The function splits the input string at whitespace characters by default.

    Parameters:
    word (str): The input string.

    Returns:
    int: The length of the last word in the input string, or 0 if the string is empty or contains
    only whitespace characters.

    Examples:
    >>> length_of_last_word('')
    0
    >>> length_of_last_word('man in Black')
    5
    >>> length_of_last_word('hello, world!     ')
    6
    >>> length_of_last_word('hello\t\nworld')
    5
    """
    if not word:
        return 0

    word_list = word.split()

    return len(word_list[-1])
