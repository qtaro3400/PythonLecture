class Person:
    def __init__(self, name):
        self.name = name
        self.__mymethod()  # ①superクラスの方で__mymethodとして名前修飾すればよい(こうすることで、subクラスでオーバーライドされなくなる)

    def mymethod(self):
        print("Person method is called")

    __mymethod = mymethod  # ③解決策：こうすれば、__mymethod()が呼ばれたときにmymethodが呼ばれるので、問題なく動く(subクラスでオーバーライドが可能)



class Baby(Person):
    def mymethod(self):
        print("Baby method id called")



taro_baby = Baby("Taro")
taro_person = Person("taro")
taro_person.mymethod()  # ②しかし、普通にPersonクラスのmymethodが呼べなくなる(_Person__mymethodで呼べるが、これはそもそもナンセンス)

print(taro_baby.name)
print(taro_person.name)

taro_baby.mymethod()
print(dir(taro_baby))