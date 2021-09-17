# Closure

# 関数もオブジェクト
def compute_square(num):
    return num * num


# print(compute_square)  # 定義した関数もfunction objectというオブジェクトの一種
f = compute_square
print(type(f))
print(f(10))


function_list = ["1", 1, True, f]
print(function_list[-1](10))

# 関数も引数として渡せる
def execute_func(func, param):
    return func(param)


print(execute_func(f, 10))


# 関数をreturnする
def return_func():

    def inner_func():
        print("this is an inner function")
    return inner_func  # カッコがついてないので、inner_funcの実行結果ではなく、inner_funcオブジェクトそのものをreturnしていることになる


f = return_func()
print(f)
print(type(f))
f()


# Closure: 状態をキープした関数を作ることができる
# 状態が静的
def power(exponent):
    def inner_power(base):
        return base ** exponent
    return inner_power


power_four = power(4)  # 関数power_fourは、exponentが4の状態をキープしている
print(power_four(3))

power_five = power(5)
print(power_five(2))

power_two = power(2)
print(power_two(2))


# 状態が動的
def average():
    nums = []

    def inner_average(num):
        nums.append(num)
        return sum(nums) / len(nums)

    return inner_average  # かっこをつけないように注意


average_nums = average()
print(average_nums(5))
# print(id(average()))
print(average_nums(15))
# print(id(average()))