# Implement a function that rotates a tuple of length 3 to the left and to the right.

def rotate_left(triple_tuple):
    A, B, C = triple_tuple
    # print(B, C, A)
    return B, C, A


def rotate_right(triple_tuple):
    A, B, C = triple_tuple
    # print(C, A, B)
    # print(type((C, A, B,)))
    return C, A, B


triple = ('A', 'B', 'C')
rotate_left(triple)  # ('B', 'C', 'A')
rotate_right(triple)  # ('C', 'A', 'B')
