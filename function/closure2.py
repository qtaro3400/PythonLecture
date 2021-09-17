# Closure: クロージャ

# 関数(function)もオブジェクト
def compute_square(num):
    return num * num


f = compute_square
print(type(f))
print(f(10))

function_list = ["1", 1, True, f]
print(function_list[-1](15))

# 関数も引数として渡せる
def execute_func(func, param):
    return func(param)


print(execute_func(f, 10))


# 関数をreturnする
def retunr_func():

    def inner_func():
        print("This is an inner function")
    return inner_func  # inner_funcそのものをreturnしたいので、かっこは付けない


f = retunr_func()
print("--------")
print(f)
print(type(f))
f()

print("--------")
# Closure: 状態をキープした関数を作ることができる
# 状態が静的のクロージャ
def power(exponent):
    def inner_power(base):
        return base ** exponent
    return inner_power


power_four = power(4)
print(power_four(3))

power_five = power(5)
print(power_five(2))


# 状態が動的のクロージャ
def average():
    nums = []

    def inner_average(num):
        nums.append(num)
        return sum(nums) / len(nums)
    return inner_average


average_nums = average()
print(average_nums(5))
print(average_nums(15))
print(average_nums(4))
print(average_nums(12))
