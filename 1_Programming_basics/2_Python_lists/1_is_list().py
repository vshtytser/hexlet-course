def is_list(value):
    if type(value) == list:
        # print(True)
        return True
    else:
        # print(False)
        return False

list_of_nums = [1, 2, 3] # создаём список

is_list(list_of_nums)  # True

is_list('string')  # False
