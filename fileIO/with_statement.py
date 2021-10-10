# try:
#     f = open("pep8_introduction.txt")
#     for line in f:
#         print(line, end="")
# finally:
#     f.close()

# with statement  ⇒これを使うと、openしたファイルは自動でcloseまでやってくれる
with open("pep8_introduction.txt") as f:
    for line in f:
        print(line, end="")


# print("hello", end=".")
# print("world", end=".")
