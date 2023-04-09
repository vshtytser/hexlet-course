def is_happy_ticket(num_str):
    """Check if a ticket number is "happy".

    A ticket number is considered "happy" if the sum of the digits in the first half
    is equal to the sum of the digits in the second half. The function takes a string
    representation of the ticket number as input and returns True if it is happy, or
    False otherwise.

    Args:
        num_str (str): A string representation of the ticket number.

    Returns:
        bool: True if the ticket number is happy, or False otherwise.
    
    Examples:
        is_happy_ticket('123123') # True
        is_happy_ticket('341800') # True
        is_happy_ticket('42') # False
        is_happy_ticket('12345678') # False
    """
    if len(num_str) % 2 != 0:
        return False

    middle_index = len(num_str) // 2  # // to get int, not float
    sum_1 = 0
    sum_2 = 0

    for first_half in num_str[:middle_index]:
        sum_1 += int(first_half)

    for second_half in num_str[middle_index:]:
        sum_2 += int(second_half)

    return sum_1 == sum_2
