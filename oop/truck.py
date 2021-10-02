from car import Car
# print(dir())


class Truck(Car):
    def __init__(self, model_name, milage, manufacturer, max_loadings):
        super().__init__(model_name=model_name, milage=milage, manufacturer=manufacturer)
        self._max_loadings = max_loadings
        self._loading = 0

    # overrideingは、superクラスで定義したメソッドと同じものをsubクラスでも定義すればよい（先に同class内にあるか探される）
    def gas(self):
        if self._loading > self._max_loadings:
            print("※注意！　重量オーバーのため、発車出来ません")
            print(f"※注意！　荷物をあと{self._loading - self._max_loadings}t下ろしてください")
        else:
            # print("積載量は問題ありません。発車します")
            super().gas()

    def load(self, weights):
        if weights > 0:
            print(f"{weights}tの荷物を積みました")
            self._loading += weights
        else:
            if self._loading <= -weights:
                print(f"現在{weights}tなので、荷物を全て下ろします")
                self._loading = 0
            else:
                print(f"{-weights}tの荷物を下ろしました")
                # weightは負の値なので、+=で足し算をする
                self._loading += weights

        print(f"現在の積載量:{self._loading}")
        if self._loading > self._max_loadings:
            print(f"最大積載量{self._max_loadings}をオーバーしています")



if __name__ == "__main__":
    isuzu_truck = Truck("トラックA", 30, "いすゞ", 50)
    isuzu_truck.gas()
    isuzu_truck.load(20)
    isuzu_truck.load(100)
    isuzu_truck.gas()
    isuzu_truck.load(-150)
    isuzu_truck.gas()
    isuzu_truck.load(20)

