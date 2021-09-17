# in演算子
fruits = ['apple', 'peach', 'grapes', 'banana']
# print('apple' in fruits)  # オブジェクトがリストにあるか、True or False を返す
# print('lemon' in fruits)
# print('lemon' not in fruits)
# print('h' in 'hello')

# Challenge
fruit = input("好きなフルーツを入力してください")
if fruit in fruits:
    fruits.remove(fruit)
    # print("{}をさしあげます。".format(fruit) + "フルーツリスト：{}".format(fruits))
    print("{}をさしあげます。".format(fruit))
else:
    fruits.append(fruit)
    # print("{}を仕入れます。".format(fruit) + "フルーツリスト：{}".format(fruits))
    print("{}を仕入れます。".format(fruit))

print("いまあるフルーツはこちらです。フルーツリスト：{}".format(fruits))
