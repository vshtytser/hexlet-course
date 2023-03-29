def fib(n):
    i = 0

    fib_0 = 0
    fib_1 = 1
    fib_current = 0

    if n == 0:
        print(n)
        return n
    elif n == 1:
        print(n)
        return n
    else:
        while i < n:
            fib_0 = fib_1
            fib_1 = fib_current
            fib_current = fib_0 + fib_1

            i += 1
            print(fib_current)
        return fib_current

# 0 	1 	2 	3 	4 	5 	6 	7 	8 	9 	10
# 0 	1 	1 	2 	3 	5 	8 	13 	21 	34 	55

#f(0) = 0
#f(1) = 1
#f(n) = f(n-1) + f(n-2)

fib(8)


#fib(3)  # 2
#fib(5)  # 5
#fib(10)  # 55
