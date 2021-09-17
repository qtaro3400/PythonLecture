# ローカル変数
def print_name_local():
    first_name = "Taro"
    last_name = "Yamada"
    print(f"I'm {first_name} {last_name}")


print_name_local()
# print(first_name)

# グローバル変数（モジュール変数）
age = 30


def print_age():
    global age  # 関数の中でグローバル変数にアクセスしたい（上書きしたい）場合
    age = 20  # ローカル変数
    print(f"I'm {age} years old")  # ageはまずローカルスコープでageを探す。無ければ、グローバルスコープに探しに行く。


print_age()
print(age)