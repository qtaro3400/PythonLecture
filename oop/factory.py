import time

class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def create_from_dob(cls, name, year, month, date):
        today = time.localtime()
        diff = (today.tm_mon, today.tm_mday) < (month, date)
        # if (today.tm_mon, today.tm_mday) < (month, date):
        #     age = today.tm_year - year - 1
        # else:
        #     age = today.tm_year - year - 0
        age = today.tm_year - year - diff

        return cls(name=name, age=age)


# __init__で作ったjohnインスタンスと、clasmethodで作ったemmaインスタンス
john = Person('John', 20)
emma = Person.create_from_dob('Emma', 1989, 4, 3)

print(john.name)
print(john.age)
print(emma.name)
print(emma.age)
print(type(john))
print(type(emma))