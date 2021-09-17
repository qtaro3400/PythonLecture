class MyClass:

    def mymethod(self):
        print("This is nomal method!")

    @staticmethod
    def mystaticmethod():  #staticmethod はインスタンスに紐づかないので、self が要らない
        print("This is staticmethod!")


c = MyClass()
c.mymethod()

MyClass.mystaticmethod()
# c.mystaticmethod()  # インスタンスから呼ぶ意味は無い