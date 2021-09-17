fruits = ['apple', 'peach', 'grapes', 'banana']

# for else
# for fruit in fruits:
#     choice = input("あなたが探しているフルーツは{fruit}ですか？ y/n:")
#     if choice == "y":
#         print("見つかって良かったですね")
#         break
#     else:
#         print("そうですか...")
# else:
#     print("お探しのフルーツは見つかりませんでした")


# while else
# count = 0
# while count < 10:
#     print(count)
#     count += 1  # +1でインクリメントしている
# else:
#     print("countは10未満ではなくなりました")

balance = 1000
game_price = 200

while balance >= game_price:
    choice = input(f"1回{game_price}円のゲームに参加しますか？ y/n: (残高:{balance}円)")
    if choice == "y":
        balance -= game_price  # augmented assginmentによる書き方
    elif choice == "n":
        print("また遊びましょう")
        break
    else:
        print("yかnで答えてください")
else:
    print(f"残高が{balance}円になったのでゲームを終了します")