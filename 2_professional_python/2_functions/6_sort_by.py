def get_first_name(full_name):
    """
    Extracts the first name from a full name string.

    Args:
        full_name (str): The full name string containing the first and last names separated by an underscore.

    Returns:
        str: The extracted first name.

    Examples:
        >>> get_first_name("Vader_Darth")
        'Vader'
    """
    return full_name.split("_")[0]


def sort_by(get_first_name, users_list):
    """
    Sorts a list of users based on their first names extracted using a provided function.

    Args:
        get_first_name (function): A function that takes a full name string as input and returns the first name.
        users_list (list): A list of strings representing the full names of users.

    Returns:
        list: A new list containing the users sorted based on their first names.

    Examples:
        >>> users = ["Vader_Darth", "Luke_Skywalker", "Boba_Fett"]
        >>> sort_by(get_first_name, users)
        ["Boba_Fett", "Luke_Skywalker", "Vader_Darth"]
    """
    return sorted(users_list, key=get_first_name)
