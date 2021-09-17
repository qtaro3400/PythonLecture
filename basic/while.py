# whileループ

# count = 0
# while count < 10:
#     print(count)
#     count += 1

# break と continue

# while True:
#     age = int(input("あなたは何歳ですか？"))
#     if not 0 <= age < 120:
#         print("入力された値は正しくありません")
#         continue
#     else:
#         print(f"あなたは{age}歳です")
#         break


# Challenge
age = int(input("何歳ですか？"))
casino_age = 18
game_text = """プレイするゲームの番号を選択してください
1: ルーレット
2: ブラックジャック
3: ポーカー
"""

if age >= casino_age:
    print("どうぞお入りください")
    while True:
        game = input(game_text)

        if game == "1":
            print("ルーレットが選択されました")
            break
        elif game == "2":
            print("ブラックジャックが選択されました")
            break
        elif game == "3":
            print("ポーカーが選択されました")
            break
        else:
            print("1~3から番号を選択してください")

else:
    print("{}歳未満の方はカジノへは入れません".format(casino_age))





# age = int(input("何歳ですか？"))
# casino_age = 18
#
# while game != "1" or "2" or "3":
#     game_text = """プレイするゲームの番号を選択してください
#     1: ルーレット
#     2: ブラックジャック
#     3: ポーカー
#     """
#
#     if age >= casino_age:
#         print("どうぞお入りください")
#         game = input(game_text)
#
#         if game == "1":
#             print("ルーレットが選択されました")
#         elif game == "2":
#             print("ブラックジャックが選択されました")
#         elif game == "3":
#             print("ポーカーが選択されました")
#         else:
#             print("1,2,3以外が選択されました")
#             print("1~3から番号を選択してください")
#
# else:
#     print("{}歳未満の方はカジノへは入れません".format(casino_age))
