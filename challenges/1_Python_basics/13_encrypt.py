def encrypt(str):
    """
    Encrypt a given string by swapping adjacent characters starting from the second character.

    This function takes a string as input and encrypts it by concatenating the characters
    at odd indices with their adjacent even-indexed characters. If the length of the input
    string is even, the encrypted string is returned as-is. If the length of the input string
    is odd, the last character of the input string is appended to the encrypted string before
    returning it.

    Args:
        s (str): The input string to be encrypted.

    Returns:
        str: The encrypted string.

    Examples:
        >>> encrypt("move")
        'omev'
        >>> encrypt("attack")
        'taatkc'
        >>> encrypt("go!")
        'og!'
    """
    encrypted_str = ''
    index = 0

    for letter in str[1::2]:
        encrypted_str = encrypted_str + letter + str[index]
        index += 2

    if len(str) % 2 == 0:
        return encrypted_str

    return encrypted_str + str[-1]
