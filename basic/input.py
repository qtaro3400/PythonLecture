# input(): ユーザの入力した値(文字列)を取得する

# age = input("何歳ですか？")
# print("あなたは{}歳です".format(age))

# Challenge1/2
age = int(input("何歳ですか？"))
casino_age = 18
game_text = """プレイするゲームの番号を選択してください
1: ルーレット
2: ブラックジャック
3: ポーカー
"""

if age >= casino_age:
    print("どうぞお入りください")
    game = input(game_text)

    if game == "1":
        print("ルーレットが選択されました")
    elif game == "2":
        print("ブラックジャックが選択されました")
    elif game == "3":
        print("ポーカーが選択されました")
    else:
        print("1~3から番号を選択してください")

else:
    print("{}歳未満の方はカジノへは入れません".format(casino_age))




# if age >= casino_age:
#     print("どうぞお入りください")
#     print("1:ルーレット 2:ブラックジャック 3:ポーカー")
#     game_num = int(input("どのゲームで遊びますか？上から番号を選択してください"))
#
#     if game_num == 1:
#         print("ルーレットが選択されました")
#     elif game_num == 2:
#         print("ブラックジャックが選択されました")
#     elif game_num == 3:
#         print("ポーカーが選択されました")
#     else:
#         print("1~3から番号を選択してください")
#
# else:
#     print("{}歳未満の方はカジノへは入れません".format(casino_age))

