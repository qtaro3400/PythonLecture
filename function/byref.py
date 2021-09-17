# 参照渡し(byref) <-> 値渡し(byvalue)
def add_nums(a, b):
    print(f"第一引数aのID:{id(a)}")
    print(f"第二引数bのID:{id(b)}")
    return a + b


one = 1
two = 2
print(f"oneのID:{id(one)}")
print(f"twoのID:{id(two)}")
print(add_nums(one, two))  # pythonはすべて参照渡しなので、aとone、bとtwoはそれぞれ同じIDを持つ

# immutableなオブジェクトの場合、関数内での変更は関数外に影響しない
def add_one(num):
    print(f"変更前のID:{id(num)}")
    num += 1
    print(f"変更後のID:{id(num)}")
    return num


one = 1
print(id(one))
print(f"関数呼び出し前のone:{one}")
add_one(one)
print(f"関数呼び出し後のone:{one}")


# mutableなオブジェクトの場合、関数内での変更が関数外にも影響する　⇒　バグにつながる！
def add_fruit(fruits, fruit):
    print(f"変更前のID:{id(fruits)}")
    fruits.append(fruit)
    print(f"変更後のID:{id(fruits)}")
    return fruits


myfruits = ['apple', 'banana', 'peach']
myfruit = 'lemon'
print(f"関数呼び出し前のmyfruits:{myfruits}")
add_fruit(myfruits, myfruit)
print(f"関数呼び出し後のmyfruits:{myfruits}")
