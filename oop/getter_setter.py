class Person:

    def __init__(self, name, age):
        self.name = name
        self._age = age

    @property
    def age(self):
        print("get_age called!!")
        return self._age

    @age.setter
    def age(self, age):
        print("set_age called!!")
        if age < 0:
            print("0以上の値を入れてください")
        else:
            self._age = age

    # age = property(get_age, set_age)


john = Person("John", 10)
print(john.age)  # インスタンス名.変数名 のように直接アクセスされたときに、property のおかげで裏で動く処理を定義しておける
john.age = -10

john._age = -100  # ._age を指定すると、裏側の_ageに直接アクセスはできてしまうので、注意！
print(john.age)