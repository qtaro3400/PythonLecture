class Person(object):

    #クラス変数（Peasonクラスから作られる全てのインスタンスがアクセスできる変数）
    num_legs = 2
    count = 0

    # constructor
    def __init__(self, name, age, gender): #メソッドの第一引数には必ずselfが入る
        self.name = name
        self.age = age
        self.gender = gender
        Person.count += 1

    def walk(self):
        print(f"{self.name} is walking... with {Person.num_legs} legs!")

    def run(self):
        print(f"{self.name} is running... with {Person.num_legs} legs!!!")


john = Person("John", 28, 'male')
print(Person.count)
taro = Person("Taro", 18, 'male')
print(Person.count)
emma = Person("Emma", 40, 'female')
print(Person.count)


# インスタンス変数（インスタンスに紐づく）
# インスタンス名の後ろの[.]に続けてアクセス可能
print(john.name)
print(f"変更前: {john.age}")
john.age = 29
print(f"変更後: {john.age}")

# インスタンスメソッド
john.walk()
taro.walk()
emma.run()

print(john.num_legs)
print(taro.num_legs)
print(Person.num_legs)

print("Person.num_legs = 3 を実行")
Person.num_legs = 3
print(john.num_legs)
print(taro.num_legs)
print(emma.num_legs)

print("john.num_legs = 4 を実行")
john.num_legs = 4
print("taro.num_legs = 6 を実行")
taro.num_legs = 6
print(john.num_legs)
print(taro.num_legs)
print(emma.num_legs)

print("Person.num_legs = 10 を実行")
Person.num_legs = 10
print(john.num_legs)
print(taro.num_legs)
print(emma.num_legs)

print("emma.num_legs = 12 を実行")
emma.num_legs = 12
print(john.num_legs)
print(taro.num_legs)
print(emma.num_legs)

print("Person.num_legs = 20 を実行")
Person.num_legs = 20
print(john.num_legs)
print(taro.num_legs)
print(emma.num_legs)