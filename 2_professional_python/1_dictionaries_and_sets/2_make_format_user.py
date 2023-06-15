def make_user(user_name, user_age):
    return {
        "name": user_name,
        "age": user_age,
    }


phil = make_user("Phil", 25)

# print(phil)


def format_user(dict):
    dict_list = list(dict.values())
    str_output = ""
    for val in dict_list:
        str_output += f"{val}, "
    return str_output.rstrip(", ")


# print(format_user(phil))
