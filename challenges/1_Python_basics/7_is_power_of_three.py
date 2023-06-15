import math


def is_power_of_three(num):
    """
    Determines whether a given number is a natural power of three.

    Args:
    num (int or float): The number to check.

    Returns:
    bool: True if the number is a power of three, False otherwise.

    Examples:
    # is_power_of_three(1)  # True
    # is_power_of_three(2)  # False
    # is_power_of_three(9)  # True
    # is_power_of_three(12)  # False
    """
    if num < 1:
        return False

    pow_of_3 = math.log(num) / math.log(3)

    if pow_of_3 % 1 == 0:
        return True

    return False
