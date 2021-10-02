class Animal(object):

    def __init__(self, name):
        self.name = name
        print("Animal init is called")

    def breath(self):
        print(f"{self.name} is breathing")


class Dog(Animal):
    def __init__(self, name):
        super().__init__(name=name)
        print("Dog init is called")


# Dog/Catのクラスを呼ぶことでAnimalクラスのconstractor(__init__)が呼ばれるので、引数はnameを渡して上げることでインスタンスを作成できる
pochi = Dog("Pochi")
print(pochi.name)
pochi.breath()
