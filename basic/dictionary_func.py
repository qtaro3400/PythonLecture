fruits_colors = {'apple': 'red', 'lemon': 'yellow', 'grapes': 'purple'}

# もしpeachというキーがあれば取ってくる。無ければないことを返す。
if 'peach' in fruits_colors:
    print(fruits_colors['peach'])
else:
    print('The key not found')

# .get()
fruit = input("フルーツの名前を指定してください")  # ユーザからのinputを受けるときなどに使える
print(fruits_colors.get(fruit, 'Nothing'))


# .update()  # dictionary同士を結合できる
fruits_colors2 = {'peach': 'pink', 'kiwi': 'green'}
fruits_colors.update(fruits_colors2)

print(fruits_colors)