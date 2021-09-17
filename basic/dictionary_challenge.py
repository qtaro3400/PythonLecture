age = int(input("何歳ですか？"))
casino_age = 18
game_dict = {'1': 'ルーレット', '2': 'ブラックジャック', '3': 'ポーカー', '4': 'スロット'}

if age >= casino_age:
    print("どうぞお入りください")
    while True:
        print("プレイするゲームを選択してください。")
        for num, game_name in game_dict.items():
            print(f"{num}: {game_name}")
        game = input(":")

        if game in game_dict:
            print(f"{game_dict[game]}が選択されました")
            break
        else:
            print("1~3から番号を選択してください")

else:
    print("{}歳未満の方はカジノへは入れません".format(casino_age))







# age = int(input("何歳ですか？"))
# casino_age = 18
# game_text = """プレイするゲームの番号を選択してください
# 1: ルーレット
# 2: ブラックジャック
# 3: ポーカー
# """
# game_dict = {'1': 'ルーレット', '2': 'ブラックジャック', '3': 'ポーカー'}
#
# if age >= casino_age:
#     print("どうぞお入りください")
#     while True:
#         print("プレイするゲームを選択してください。")
#         for num, game_name in game_dict.items():
#             print(f"{num}: {game_name}")
#         game = input(":")
#         if game == "1":
#             print("ルーレットが選択されました")
#             break
#         elif game == "2":
#             print("ブラックジャックが選択されました")
#             break
#         elif game == "3":
#             print("ポーカーが選択されました")
#             break
#         else:
#             print("1~3から番号を選択してください")
#
# else:
#     print("{}歳未満の方はカジノへは入れません".format(casino_age))