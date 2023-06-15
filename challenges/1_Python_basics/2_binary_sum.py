def binary_sum(a, b):
    decimal_a = int(a, base=2)
    decimal_b = int(b, base=2)

    decimal_sum = decimal_a + decimal_b

    print(f'{decimal_sum:b}')
    return f'{decimal_sum:b}'


# 1 2 4 8 16 32

binary_sum('10', '1')      # 11
binary_sum('1101', '101')  # 10010
binary_sum('1000', '10')
