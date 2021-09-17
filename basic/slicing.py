# 「:」を使って、複数の要素を取ってくることができる(slicing)
even = [2, 4, 6, 8, 10, 12]
# 基本は[開始:未満]
print(even[1:4])

print(even[0:4])
print(even[:4])  # 開始の0を省略すれば、最初の要素から取ってくる

print(even[3:5])
print(even[3:-1])

print(even[3:])  # 終了の数値を省略すれば、最後の要素まで取ってくる
print(even[:])  # 最初から最後まですべての要素を取ってくる

text = "hello world"
print(text[3:])  # 文字列に対してもslicingが可能

# []開始:未満:step]
print(text[2:10:2])  # ひとつ飛ばしで取ってくる

print(text[::-1])  # stepを負の値にすると、逆順で取ってくる