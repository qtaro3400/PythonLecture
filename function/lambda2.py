# lambda関数（無名関数）

def square(x):
    return x * x

s = lambda x: x * x

print(square(3))
print(s(5))


def power(exponent):
    # def inner_power(base):
    #     return base ** exponent
    # return inner_power
    return lambda base: base ** exponent


third_power = power(3)
print(third_power(2))


numbers = [6, 2, 5, 43, 5, 36, 67, 2]

def filterfunc(num):
    return not num % 2

filterd_num = filter(lambda num: num % 2, numbers)
print(list(filterd_num))
# for num in numbers:
#     print(filterfunc(num))