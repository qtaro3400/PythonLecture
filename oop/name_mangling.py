class Account:

    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, price):
        self.__balance += price
        self.show_balance()

    def withdraw(self, price):
        if self.__balance < price:
            print("残高が足りません")
        else:
            self.__balance -= price
            self.show_balance()

    def show_balance(self):
        print(f"残高は{self.__balance}円です")


myaccount = Account(10000)
# myaccount.deposit(1000)
# myaccount.withdraw(3000)
#
# myaccount.__balance = -1000  # インスタンス名.インスタンス変数を使えば、直接値を操作できてしまう ⇒ L4: balance を _balance と宣言する
# print(myaccount.__balance)


print(dir(myaccount))
myaccount.deposit(2000)
myaccount.withdraw(5000)
myaccount.withdraw(10000)

# print(myaccount.__balance)  # 名前修飾された __balance としても、変数は呼べない(dir関数で見ると、_Account__balance となっているので)
# print(myaccount._Account__balance)

myaccount.__balance = -10000
print(myaccount.__balance)  # 上のコードで __balance には値が代入されたので(新規で__balanceとう属性が作られたので)printできるが、元の_Account_balance は書き換えられないため、安全
print(myaccount._Account__balance)

myaccount.show_balance()
print(dir(myaccount))

myaccount._Account__balance = -20000  # __を付けても、結局パブリックな変数ではあるので、直接編集はできてしまうことに注意！
myaccount.show_balance()
