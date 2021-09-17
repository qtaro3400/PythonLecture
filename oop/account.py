import time

class Account(object):


    count = 0
    transaction = {}

    def __init__(self, balance, name):
        self.balance = balance
        self.name = name
        self.account_number = Account.count  # この行と下の += がポイント！！ こうすることでインスタンスごとにcount値を付与できる
        Account.count += 1



    def withdraw(self):
        wd_money = int(input(f"{self.name}に対する口座引き出し金額を入力してください(口座番号:{self.account_number})"))

        now_money = self.balance - wd_money
        if now_money < 0:
            print("残高不足です。引き下ろせません")
        else:
            self.balance -= wd_money
            print(f"引き下ろし後の口座{self.name}(口座番号:{self.account_number})の残高は{self.balance}です")
            Account.transaction['やり取り金額'] = wd_money
            Account.transaction['新しい残高'] = self.balance
            Account.transaction['やり取り日時'] = Account.get_time_str()
            print(Account.transaction)

    def deposit(self):
        ds_money = int(input(f"{self.name}に対する口座預け入れ金額を入力してください(口座番号:{self.account_number})"))
        self.balance += ds_money
        print(f"預け入れ後の口座{self.name}(口座番号:{self.account_number})の残高は{self.balance}です")
        Account.transaction['やり取り金額'] = ds_money
        Account.transaction['新しい残高'] = self.balance
        Account.transaction['やり取り日時'] = Account.get_time_str()
        print(Account.transaction)


    @staticmethod
    def get_time_str():
        current_time = time.localtime()
        return "{0.tm_year}年{0.tm_mon}月{0.tm_mday}日{0.tm_hour}時{0.tm_min}分".format(current_time)

    def show_transaction_history(self):
        for i in Account.transaction:
            for k, v in Account.transaction.items():
                print(k, v)




taro_acc = Account(20000, "Taro_acc")
jiro_acc = Account(30000, "Jiro_acc")

taro_acc.withdraw()
jiro_acc.withdraw()
taro_acc.deposit()
jiro_acc.deposit()

# print(Account.transaction['やり取り金額'])

print(Account.get_time_str())
print("--------------------")
taro_acc.show_transaction_history()