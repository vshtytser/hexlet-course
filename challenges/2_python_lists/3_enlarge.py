def show(image):
    for line in image:
        print(line)


frame = [
    '****',
    '*  *',
    '*  *',
    '****'
]


def enlarge(list_input):
    """
    This function takes a list of strings as input and enlarges each string by duplicating each
    character horizontally and each row vertically. It returns the enlarged list of strings.
    If the input list is empty, an empty list will be returned.

    Args:
    list_input (List[str]): A list of strings, where each string represents a row of characters.

    Returns:
    List[str]: A new list of strings, where each row and character is enlarged by a factor of 2.

    Example:
    frame = [
    '****',
    '*  *',
    '*  *',
    '****'
    ]
    >>>enlarge(frame)
    # => ********
    # => ********
    # => **    **
    # => **    **
    # => **    **
    # => **    **
    # => ********
    # => ********
    """
    if not list_input:
        return []

    new_list = []

    for item in list_input:
        new_str_item = f'{"".join(item)}'

        new_str = ''
        for char in new_str_item:
            new_str += char * 2

        new_list += [new_str,
                     new_str,
                     ]

    return new_list
