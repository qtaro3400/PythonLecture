class MyClass:

    classmrthod_count = 0

    def mymethod(self):
        print("This is nomal method!")

    @staticmethod
    def mystaticmethod():  #staticmethod はインスタンスに紐づかないので、self が要らない
        print("This is staticmethod!")

    @classmethod
    def myclassmethod(cls):
        cls.classmrthod_count += 1
        print("This is classmethod")


c = MyClass()
c.mymethod()

MyClass.mystaticmethod()
# c.mystaticmethod()  # インスタンスから呼ぶ意味は無い