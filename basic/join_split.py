# join
text = " ".join(["Hi", "My", "name", "is", "john"])  # 接着文字に対してjoinでリストを渡してあげる
print(text)

text = "**".join(["Hi", "My", "name", "is", "john"])
print(text)

text = "_".join(["Hi", "My", "name", "is", "john"])
print(text)

# "Hi My name is john"

# split
print("Hi My name is john".split(" "))  # 文字列に対して、splitで区切る。joinの逆
print("Hi My name is john".split())  # ()はデフォルトが半角スペース

print("Hi My name is john".split("/"))


filename = "sample.py"
print(filename.split(".")[0])
print(filename.split(".")[-1])