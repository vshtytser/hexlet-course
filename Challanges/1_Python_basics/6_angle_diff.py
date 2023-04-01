def diff(a, b):
    """
    Compute the smallest angle between two given angles.

    Args:
        a (float): The first angle in degrees.
        b (float): The second angle in degrees.

    Returns:
        The smallest angle between a and b in degrees.

    Examples:
        diff(0, 45) # 45
        diff(0, 180) # 180
        diff(0, 190)  # 170
        diff(120, 280) # 160
        diff(1080, -2030) # 130
        diff(720, 0) # 0
    """
    a = a % 360
    b = b % 360

    diff_angle = abs(a - b)

    if diff_angle > 180:
        diff_angle = 360 - diff_angle

    # print(diff_angle)
    return diff_angle
