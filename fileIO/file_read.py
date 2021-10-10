# for文でループを回す
# with open("pep8_introduction.txt") as f:
#     for line in f:
#         print(line, end="")


# .read()でファイルの中身の全てを一つのstringとして返す
# 要注意！大きなファイルではやらないこと（全ての行を一気にメモリに入れるので負荷大）
# with open("pep8_introduction.txt") as f:
#     print(f.read())


# .readline()で一行ずつ取得しstringで返す
# with open("pep8_introduction.txt") as f:
#     line = f.readline()
#     while line:  # lineにオブジェクトが入っていればTrue、Noneが入ればFalseになる（全業取得し終えたらループが止まる）
#         print(line, end="")
#         line = f.readline()


# .readlines()で全ての行をlistで返す
with open("pep8_introduction.txt") as f:
    lines = f.readlines()
    print(lines)