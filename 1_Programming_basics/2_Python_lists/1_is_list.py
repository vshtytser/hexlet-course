def is_list(value):
    if type(value) == list:
        # print(True)
        return True
    else:
        # print(False)
        return False

list_of_nums = [5, 6, 7] # создаём список

is_list(list_of_nums)  # True

is_list('string')  # False

# optimize is_list function
def is_list(value):
    return type(value) == list  # return True or False