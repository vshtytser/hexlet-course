def rgb(red=0, green=0, blue=0):
    """
    Generate an RGB color string based on the provided color values.

    Args:
        red (int): The red component of the RGB color (default: 0).
        green (int): The green component of the RGB color (default: 0).
        blue (int): The blue component of the RGB color (default: 0).

    Returns:
        str: The RGB color string in the format "rgb(red, green, blue)".

    Examples:
        >>> rgb(red=255)
        'rgb(255, 0, 0)'

        >>> rgb(green=255)
        'rgb(0, 255, 0)'

        >>> rgb(blue=255)
        'rgb(0, 0, 255)'
    """
    return f"rgb({red}, {green}, {blue})"


def get_colors():
    """
    Generate a dictionary of predefined RGB colors.

    Returns:
        dict: A dictionary with color names as keys and corresponding RGB color strings as values.

    Examples:
        >>> colors = get_colors()
        >>> colors.keys()
        dict_keys(['red', 'green', 'blue'])

        >>> colors["red"]
        'rgb(255, 0, 0)'

        >>> colors["blue"]
        'rgb(0, 0, 255)'
    """
    dict = {
        "red": rgb(red=255),
        "green": rgb(green=255),
        "blue": rgb(blue=255),
    }
    return dict
