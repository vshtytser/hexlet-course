def is_degenerated(line_tuple):
    # should return true if the segment degenerates into a point
    # (beginning and end are the same)
    (x1, y1), (x2, y2) = line_tuple

    if x1 == x2 and y1 == y2:
        # print('True')
        return True
    # print('False')
    return False


def is_vertical(line_tuple):
    # is_vertical() must return true if the segment is vertical
    (x1, y1), (x2, y2) = line_tuple

    if x1 == x2 and y1 != y2:
        # print('True')
        return True
    # print('False')
    return False


def is_horizontal(line_tuple):
    # is_horizontal() must return true if the segment is horizontal
    (x1, y1), (x2, y2) = line_tuple

    if x1 != x2 and y1 == y2:
        # print('True')
        return True
    # print('False')
    return False


def is_inclined(line_tuple):
    # is_inclined() should return true if the segment is slanted
    # (not vertical or horizontal)
    (x1, y1), (x2, y2) = line_tuple

    if x1 != x2 and y1 != y2:
        # print('True')
        return True
    # print('False')
    return False


line1 = (0, 10), (100, 130)
# is_vertical(line1)  # False
# is_horizontal(line1)  # False
# is_degenerated(line1)  # False
# is_inclined(line1)  # True

line2 = (42, 1), (42, 2)
# is_vertical(line2)  # True

line3 = (100, 50), (200, 50)
# is_horizontal(line3)  # True
