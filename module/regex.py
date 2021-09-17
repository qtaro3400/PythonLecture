import re

# Regular Expression(正規表現 通称RegEx)

# email = "myemail@gmail.com"
# print("@" in email)
#
# matched = re.search('@\w+\.', email)
# if matched:
#     print(matched)
#     print("Matched")
# else:
#     print("Not found!")


# # metacharacter
# # []
# print(re.search('[a-c]', 'apple'))
# print(re.search('[0-9]', 'a5sfve'))
#
# # ^ 最初の文字
# print(re.search('^[0-9]', '0test'))
#
# # {} n回リピート
# print(re.search('^[0-9]{2,4}', '2021/09/12'))
#
# # $ 最後の文字
# print(re.search('[0-9]{3}$', '2021/09/12'))
#
# # * 左のパターンを0回以上繰り返す
# print(re.search('a*b', 'aac'))
#
# # + 左のパターンを1回以上繰り返す
# print(re.search('a+b', 'a'))
#
# # ? 左のパターンを0回か1回繰り返す
# print(re.search('ab?c', 'abc'))
#
# # | or
# print(re.search('abc|012', 'abc'))
#
# # () グループ
# print(re.search('te(s|x)t', 'tet'))
#
# # . 任意の一文字
# print(re.search('h.t', 'hot'))
#
# # \ エスケープ
# print(re.search('h\.t', 'h.t'))
#
# # \w [a-zA-Z0-9_] すべてのアルファベット、数字およびアンダースコア
# print(re.search('h\wt', 'h_t'))


# Challenge1
# # pattern_birth = "'"^19|20[0-9]{2}/[0-9]{1,2}/[0-9]{1,2}"
# # pattern_birth = "'"^(19|20)[0-9]{2}/([1-9]|1[0-2])/([1-9]|[1-3][0-9])"
# pattern_birth = "^(19|20)[0-9]{2}/([1-9]|1[0-2])/([1-9]|1[0-9]|2[0-9]|3[01])$"
#
# while True:
#     birth = input("生年月日を入力してください(yyyy/mm/dd)")
#     result = re.search(pattern_birth, birth)
#     if result:
#         print(f"{birth}は正しいフォーマットです")
#         break
#     else:
#         print(f"{birth}は正しくないフォーマットです")



# Challenge2
# pattern_addr = "(\w+|\.|-)@\w+\.[a-zA-Z]{2,3}$"
pattern_addr = "^(\w|\.|-)+@(\w|\.|-)+\.[a-zA-Z]{2,3}$"

while True:
    addr = input("メールアドレスを入力してください")
    result2 = re.search(pattern_addr, addr)
    if result2:
        print(f"{addr}は正しいメールアドレスです")
        break
    else:
        print(f"{addr}は正しくないメールアドレスです")