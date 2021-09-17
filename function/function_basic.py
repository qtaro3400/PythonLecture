# 関数(function)
# ビルトインファンクション(元々組み込まれている関数)
# print()
# len()
# input()

# 華氏から摂氏に変換する
fahrenheit = 72


def fah_to_cel(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius
# def fah_to_cel(banana):
#     hoge = (banana - 32) * 5/9
#     return hoge


celsius = fah_to_cel(fahrenheit)
print(celsius)