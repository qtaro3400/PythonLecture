# if文のNoneの取り扱い
a = None
# if a is None:
#     print("a is None!!")
# else:
#     print("a has value!!")

if a:  # a がNoneの時は、Falseになる（つまりスキップする）。None以外の値が入っていたら、Trueになる。
    print("a has value")
else:
    print("a is None")

if not a:
    print("a is None")

if not a:
    a = 10  # aがNoneだったら何かの値を入れる、という処理をしたい場合があるとき
    print(a)