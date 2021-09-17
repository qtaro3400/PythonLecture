# Type annotation
def add_nums(num1: int, num2: int) -> int:  # 引数、戻り値の型をそれぞれ指定して関数を定義することができる
    return num1 + num2

# 動的型付け言語 <-> 静的型付け言語
print(add_nums(1, 2))
print(add_nums("1", "2"))  # type_annotationで指定した型でなくても、エラーにはならない