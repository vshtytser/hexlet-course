def chunked(num, sq):
    """
    Divides a sequence into equally sized chunks, with the last chunk possibly being smaller.

    Args:
        num (int): The number of elements in each chunk.
        sq (str, list, or tuple): The input sequence to be divided.

    Returns:
        list: A list of chunks, where each chunk is a sublist, substring, or sub-tuple of the input sequence.

    Examples:
        >>> chunked(2, ['a', 'b', 'c', 'd'])
        [['a', 'b'], ['c', 'd']]
        >>> chunked(3, ['a', 'b', 'c', 'd'])
        [['a', 'b', 'c'], ['d']]
        >>> chunked(3, 'foobar')
        ['foo', 'bar']
        >>> chunked(10, (42,))
        [(42,)]
        >>> chunked(2, 'abcdef') == ['ab', 'cd', 'ef']
        ['ab', 'cd', 'ef']
    """
    if not sq:
        return []

    if len(sq) <= num:
        return [sq]

    chunk = []

    for i in range(0, len(sq), num):
        chunk.append(sq[i:i + num])

    return chunk
