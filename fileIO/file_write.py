with open("writing_file.txt", mode='w') as f:
    # truncated ファイルが上書きされること（ファイルの中身がbyte=0に切り詰められる）
    f.write("You can write contents here\nuse 'backslash' to break the row.")
    f.write("New write() doesn't break row.")

    print("You can add a new row using 'file' parameter.", file=f)  # print関数の出力先を、file=で指定できる
    print("New print() method breaks the row for you!!", file=f)  # print文には最後に暗黙のend="\n"があるので、１行ずつ改行されるのが便利