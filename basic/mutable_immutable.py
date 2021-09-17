# mutable: 変更可能なオブジェクト list, dict, set
# fruits = ['apple', 'peach', 'banana']
# print(f"fruitsのIDは{id(fruits)}")
# fruits.append('lemon')
# print(fruits)
# print(f"fruitsのIDは{id(fruits)}")  # オブジェクトのIDが、値更新前と後で変わらない！　⇒mutableということ


# immutable: 変更不可能なオブジェクト int, float, str, bool, tuple
# fruit = 'apple'
# print(f"fruitのIDは{id(fruit)}")
# fruit += ', lemon'
# print(fruit)
# print(f"fruitのIDは{id(fruit)}")  # オブジェクトのIDが、値更新前と後で変わっている！　⇒immutableということ


text = ""  # 1-2-3-4-5-6-7-...　とforで追加していきたい場合
for i in range(1, 11):
    if i == 1:
        text += str(i)
    else:
        text += '-' + str(i)
print(text)  # textはimmutableなので、メモリ効率は悪い（ループするごとにIDが変わる）


text_list = []
for i in range(1, 11):
    text_list.append(str(i))

text = "-".join(text_list)
print(text)  # listはmutableなので、メモリ効率が良い