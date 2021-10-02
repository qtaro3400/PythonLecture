class Myclass(object):  # 全てのオブジェクトはobjectクラスを継承していて、そのobjectクラスに__str__()メソッドが元々定義されているので、最初から使える。明示的に下のように定義した場合は、オーバーライドしているだけ。
    pass
    def __str__(self):
        return "Myclassの__str__"


# mc = Myclass()
# print(mc)  # mcの__str__() というメソッドが裏で動いている。mcに対する__str__()の戻り値が帰ってきている
# print(mc.__str__())
#
# print(1)  # 1.__str__()
# print("1")  # "1".__str__()
# print(True)  # True.__str__()
# print([1, 2, 3])  # [1, 2, 3].__str__()
# print(dir(Myclass))

various_types = [1, "1", True, [1, 2, 3], (1,), {'1': 1}, {1}]
# for element in various_types:
    # print(element)  # listに存在している全てのオブジェクトが、.__str__()をobjectクラスから継承しているので、オブジェクトのデータ型を気にせずprintできる


def printvalue(arg):
    print(arg + 1)

printvalue(True)

