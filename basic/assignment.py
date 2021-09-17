# 変数へ代入：assignment
hello = "konnichiwa"
world = "sekai"
print(hello + world)
print("konnichiwa" + "sekai")  # ハードコーディング

# format
print("{} {}".format(hello, world))

name = "John"
print("Hey, {}!! How are you doing?".format(name))

balance = 100
print("balance: {}".format(balance))


# fstring
print(f"{hello} {world}")

name = "Emily"
print(f"Hey, {name}!! How are you doing?")

balance = 200
print(f"balance: {balance}")