def print_dict(input_dict):
    for k, v in input_dict.items():
        print(f"key: {k}, value:{v}")
    # return None  # retuenを書かない関数は、実はretuen Noneを裏でしている

a = {"one": 1, "two": 2}
print(a)
print_dict(a)

return_value = print_dict(a)
print(return_value)


def get_first_last_word(text):
    text = text.replace(",", "")
    words = text.split()
    return words[0], words[-1]


text = "hello, My name is Mike"
first, last = get_first_last_word(text)  # 複数の値を返す場合は戻り値がtuple型なので、その個数分の変数を用意してあげて格納する
print(f"first word is {first}, last word is {last}")