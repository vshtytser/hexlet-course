def fizz_buzz(a, b):

    i = 0

    num_str = ''

    while i <= (b - a):
        current_num = a + i

        if current_num % 3 + current_num % 5 == 0:
            num_str = f'{num_str} FizzBuzz'
        elif current_num % 3 == 0:
            num_str = f'{num_str} Fizz'
        elif current_num % 5 == 0:
            num_str = f'{num_str} Buzz'
        else:
            num_str = f'{num_str} {current_num}'

        i += 1

        # print(i)
        # print(current_num)
        # print(num_str)
    return num_str.strip()

# fizz_buzz(1, 5)
# fizz_buzz(11, 20)
# fizz_buzz(7, 7)
