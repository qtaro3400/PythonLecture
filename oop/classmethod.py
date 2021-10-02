class MyClass:

    classmethod_count = 0

    def mymethod(self):
        print("This is nomal method!")

    @staticmethod
    def mystaticmethod():  #staticmethod はインスタンスに紐づかないので、self が要らない
        print("This is staticmethod!")

    @classmethod
    def myclassmethod(cls):
        cls.classmethod_count += 1  #クラス変数は「Class.変数」で指定、クラスメソッドは「引数.変数」で指定
        print(f"This is classmethod and now the count is {cls.classmethod_count}")


c = MyClass()
c.mymethod()

MyClass.mystaticmethod()
# c.mystaticmethod()  # インスタンスから呼ぶ意味は無い

MyClass.myclassmethod()  # clsにはMyClassが自動で入るので、()で引数を渡す必要はない
MyClass.myclassmethod()
c.myclassmethod()