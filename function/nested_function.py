# 関数の中で関数を定義（nested function）
# def outer():
#     outer_param = "outer arg"
#     def inner():
#         inner_variable = "inner var"
#         print("This is inner function")
#         print(outer_param)
#     print(inner_variable)  # inner関数のローカル変数は、outer関数で使えない
#     inner()


# outer()
# inner()  # 外からは使えない関数


msg = "I am global"


def outer():
    # global msg
    msg = "I am outer"

    def inner():
        nonlocal msg
        msg = "I am inner"
        print("This is inner function")
        print(msg)
    inner()
    print(msg)

outer()
print(msg)