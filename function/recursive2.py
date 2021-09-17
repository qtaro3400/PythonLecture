# 再起関数（recursive function）: 関数内で自分の関数をcallする関数

# 階乗: 3! = 3 x 2 x 1 = 6
# n! = n * (n-1)!

# def factorial(n):
#     if n == 1:
#         return 1
#     else:
#         return n * factorial(n-1)
#
# print(factorial(4))



# Challenge1

num = 6

def fibonacchi_alt(n):
    if n < 2:
        return n
    else:
        return fibonacchi_alt(n-2) + fibonacchi_alt(n-1)

# print(fibonacchi_alt(num))


def fibonacchi(n):
    if n < 2:
        return n
    else:
        n_1 = 1
        n_2 = 0
        for _ in range(n-1):
            result = n_2 + n_1
            n_2 = n_1
            n_1 = result
        return result

# print(fibonacchi(7))

for i in range(50):
    print(i, fibonacchi(i))