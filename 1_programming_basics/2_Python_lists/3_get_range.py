def get_range(num):
    if num <= 0:
        return []
    else:
        i = 0
        num_range = []

        while i < num:
            num_range.append(i)
            i += 1

        return num_range


get_range(5)  # [0, 1, 2, 3, 4]

print(get_range(5))
