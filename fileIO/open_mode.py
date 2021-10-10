# mode='a' (append):ファイルの最後尾に内容を追加
# with open("writing_file.txt", mode='a') as f:
#     f.write("mode=a appends text")

# node='r+': 読み書きどちらも可能
# with open("writing_file.txt", mode='r+') as f:
#     f.write("You can write and read with r+ mode!!\n")
#     print(f.read())
#     f.write("This should be the last sentence.\n")
#     print(f.read())


# mode='w+': 読み書きどちらも可能　※Truncateされることに注意
# with open("writing_file.txt", mode='w+') as f:
#     print(f.read())
#     f.write("You can write and read with w+ mode!!")
#     f.seek(0)
#     print(f.read())


# mode='a+': 読み書きどちらも可能で、positionが最後尾から始まり、truncateされない
with open("writing_file.txt", mode='a+') as f:
    print(f.read())
    f.write("\nYou add sentences ton the last do the file content with a+ mode")
    f.seek(0)
    print(f.read())