def binary_sum(a, b):
    
    pointer = -1
    i = 0

    str_num = ''

    position_num_a = int(a[pointer:])
    position_num_b = int(b[pointer:])

    while i != len(a):
        if position_num_a + position_num_b <= 1:
            print(position_num_a + position_num_b)
            str_num = str(position_num_a + position_num_b)
            i += 1
            print(str_num)
        return str_num
        


# 1 2 4 8 16 32

#binary_sum('10', '1')      # 11
binary_sum('1101', '101')  # 10010


# Реализуйте функцию binary_sum(),
# которая принимает на вход два двоичных числа в виде строк
# и возвращает их сумму. Вычисленная сумма также должен быть бинарным числом
# в виде строки:
