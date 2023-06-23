def check_if_prime(number):
    """
    Check if a number is prime.

    Args:
        number (int): The number to check for primality.

    Returns:
        bool: True if the number is prime, False otherwise.

    Examples:
        print(check_if_prime(5))
        # Output: True

        print(check_if_prime(4))
        # Output: False
    """
    if number < 2:
        return False
    for n in range(2, number):
        if number % n == 0:
            return False
    return True


def say_prime_or_not(number):
    """
    Print whether a number is prime or not.

    Args:
        number (int): The number to check for primality.

    Returns:
        None

    Examples:
        say_prime_or_not(5)
        # Output: yes

        say_prime_or_not(4)
        # Output: no
    """
    if check_if_prime(number):
        print("yes")
    else:
        print("no")
