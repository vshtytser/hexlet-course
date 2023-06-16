def count_all(iter_obj):
    """
    Count the number of occurrences of each unique object in the input iterable.

    Args:
        iter_obj (iterable): An iterable object containing the elements to count.

    Returns:
        dict: A dictionary where the keys represent unique objects in the input iterable
              and the values represent the number of times each object occurs.

    Examples:
        >>> count_all(["cat", "dog", "cat"])
        {'cat': 2, 'dog': 1}

        >>> count_all("hello")
        {'h': 1, 'e': 1, 'l': 2, 'o': 1}

        >>> count_all("*" * 20)
        {'*': 20}
    """
    unique_occurances = []
    for obj in iter_obj:
        if obj not in unique_occurances:
            unique_occurances.append(obj)
    # print(unique_occurances)

    times_occured = []
    for t in unique_occurances:
        times_occured.append(iter_obj.count(t))
    # print(times_occured)

    zipped = dict(zip(unique_occurances, times_occured))
    # print(zipped)
    return zipped
