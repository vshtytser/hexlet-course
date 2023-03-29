import math


def get_square_roots(num):
    sq_root_num = math.sqrt(abs(num))

    if num == 0:
        # print([0])
        return [0]
    elif num > 0:
        # print([-sq_root_num, sq_root_num])
        return [-sq_root_num, sq_root_num]
    else:
        # print([])
        return []


get_square_roots(25)  # [-5.0, 5.0]
get_square_roots(0)  # [0]
get_square_roots(-25)  # []
