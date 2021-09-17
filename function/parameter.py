def func(first, second, third):  # 関数定義時のかっこの中の変数のことを、parameterという
    print(f"first: {first}, second: {second}, third: {third}")

func("1", "2", "3")  # 関数呼び出し時のかっこの中の値のことを、argumentという
func("1", third="3", second="2")



def func(first, second, third="3"):  # parameterには、関数呼び出し時に引数が呼ばれなかった際のデフォルト値を指定できる
    print(f"first: {first}, second: {second}, third: {third}")

func("1", "2", "three")
func("1", "2")