def triangle(row):
    """
    Generate a specific row of Pascal's Triangle.

    Pascal's Triangle is a triangular array of the binomial coefficients, where each number is the sum
    of the two numbers directly above it. This function generates and returns the row specified by
    the input argument. E.g.:
    # 0:      1
    # 1:     1 1
    # 2:    1 2 1
    # 3:   1 3 3 1
    # 4:  1 4 6 4 1

    Args:
        row (int): The index of the row to generate (0-based).

    Returns:
        list: A list of integers representing the specified row in Pascal's Triangle.

    Examples:
        >>> triangle(0)
        [1]
        >>> triangle(4)
        [1, 4, 6, 4, 1]
    """
    if row == 0:
        return [1]

    if row == 1:
        return [1, 1]

    prev_row = [1, 1]
    cur_row = []
    i = 0

    while i < row - 1:  # because prev_row is already the first row
        middle_values = []

        for num in zip(prev_row[:-1], prev_row[1:]):
            middle_values.append(sum(num))

        cur_row = [prev_row[0]] + middle_values + [prev_row[-1]]
        prev_row = cur_row[:]
        i += 1

    return cur_row
