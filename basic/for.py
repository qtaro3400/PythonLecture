# forループ
fruits = ['apple', 'peach', 'grapes', 'banana']

# for fruit in fruits:
#     print(f"I love {fruit}!!")
#
# for char in "hello world!!":
#     print(f"char: {char}")

# iterationとiterable

# Challenge1
# favorite = input("好きなフルーツは何ですか？")
# for fruit in fruits:
#     if favorite == fruit:
#         print("{}は好き".format(fruit))
#     else:
#         print("{}は好きじゃない".format(fruit))

# Challenge2
favorite_fruits = []
normal_fruits = []
for fruit in fruits:
    choice = input(f"{fruit}は好きですか？ y/n")
    if choice == "y":
        favorite_fruits.append(fruit)
    else:
        normal_fruits.append(fruit)

print(f"好きなフルーツは{favorite_fruits}です")
print(f"{normal_fruits}は普通です")