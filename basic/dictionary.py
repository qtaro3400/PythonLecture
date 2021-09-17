# dictionary: キーと値の組み合わせを複数保持するデータ型

fruits_colors = {'apple': 'red', 'lemon': 'yellow', 'grapes': 'purple'}
print(fruits_colors['apple'])

fruits_colors['peach'] = 'pink'
print(fruits_colors)

dict_sample = {1: 'one', 'two': 2, 'three': [1, 2, 3], 'four': {'inner': 'dict'}}
print(dict_sample)
print(dict_sample['four'])
print(dict_sample['four']['inner'])  # nested dictionary の値を取得

colors = {}
colors[1] = 'blue'
colors[0] = 'red'
colors[2] = 'green'
print(colors)  # listやtupleとは違い、dictionaryはオブジェクトの順番は保持しない

# .keys()  あるdictionaryの key をforで回したいとき
# .values()  あるdictionaryの value をforで回したいとき
for fruit in fruits_colors.keys():
    print(fruit)

for color in fruits_colors.values():
    print(color)

for f in fruits_colors:  # dictionaryを直接forで回すと、デフォルトはkeyで回すのでfruitが羅列される
    print(f)


# .items()  # keyとvalueをセットにして、tupleでforを回す。enumerateと似たような動き
for fruit, color in fruits_colors.items():
    print(f"{fruit} is {color}")