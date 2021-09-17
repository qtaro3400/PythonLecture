# call_count = 0
CALL_COUNT = 0  # constant variable（グローバル変数を定義して、かつ書き換えられたくないときの目印。推奨）

def print_count1():
    global CALL_COUNT
    CALL_COUNT += 1
    print(f"関数1：{CALL_COUNT}回目")


def print_count2():
    global CALL_COUNT
    CALL_COUNT += 1
    print(f"関数2：{CALL_COUNT}回目")


print_count1()
print_count2()
print_count1()
print_count1()
print(CALL_COUNT)
