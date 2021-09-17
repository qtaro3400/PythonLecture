# Decorator: 関数に機能を付属する（デコレートする）

def greeting(func):
    # def inner(name):
    def inner(*args, **kwargs):  # Dacoratorを渡す場合は、不特定多数の引数を受けられるように:args, **kwargs とすることが多い
        print("Hello!")
        func(*args, **kwargs)
        print("Nuce to meet you!")
    return inner


@greeting  # これを書くことで、say_name = greeting(say_name)　の1行が入れる必要が無くなる
def say_name(name):
    print(f"I'm {name}")

@greeting
def say_name_and_origin(name,origin):
    print(f"I'm {name}, I'm from {origin}")


# say_name = greeting(say_name)
say_name("jiro")
# say_name_and_origin("Taro", "Tokyo")
say_name_and_origin(name="Taro", origin="Tokyo")


# say_name("Jiro")



