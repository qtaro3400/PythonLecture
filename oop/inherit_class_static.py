import time

class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def create_from_dob(cls, name, year, month, date):
        today = time.localtime()
        diff = (today.tm_mon, today.tm_mday) < (month, date)
        age = today.tm_year - year - diff
        return cls(name=name, age=age)

    @staticmethod
    def create_from_dob2(name, year, month, date):
        today = time.localtime()
        diff = (today.tm_mon, today.tm_mday) < (month, date)
        age = today.tm_year - year - diff
        return Person(name=name, age=age)


class Baby(Person):
    pass

# __init__で作ったjohnインスタンスと、classmethodで作ったemmaインスタンス
john = Baby('John', 20)
emma = Baby.create_from_dob('Emma', 1989, 4, 3)  # classmethodを使って生成したインスタンス
emily = Baby.create_from_dob2('Emily', 1999, 12, 3)  # staticmethodを使って生成したインスタンス


print(john.name)
print(john.age)
print(emma.name)
print(emma.age)
print(emily.name)
print(emily.age)
print(type(john))
print(type(emma))
print(type(emily))

# この状態でemilyインスタンスを生成すると、オブジェクトのtypeが"Baby"ではなく"Person"になってしまう　⇒バグの元！！
# classの情報をメソッドの中で使いたいときは、staticmethodではなくclassmethodを使う（cls引数で受け取って中で使う）べき