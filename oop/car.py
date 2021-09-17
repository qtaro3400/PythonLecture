class Car:
    def __init__(self, model_name, milage, manufacturer):
        self.model_name = model_name
        self.milage = milage
        self.manufacturer = manufacturer

    def gas(self):
        # print(f"{self.manufacturer}の{self.model_name}は、燃費{self.milage}で加速します")
        print("{0.manufacturer}の{0.model_name}は、燃費{0.milage}で加速します".format(self))

    def brakes(self):
        print("{0.manufacturer}の{0.model_name}は、燃費{0.milage}で減速します".format(self))


if __name__ == "__main__":
    prius = Car("Prius", 30, "TOYOTA")
    mirra = Car("Mirra", 40, "DAIHASTU")

    # インスタンス変数(インスタンス名.インスタンス変数　で呼び出す)
    print(prius.model_name)
    print(mirra.model_name)

    car_name = prius
    # car_name = mirra
    print(f"{car_name.manufacturer}の{car_name.model_name}は燃費が{car_name.milage}です")

    # インスタンスメソッド（インスタンス名.メソッド名　で呼び出す）
    prius.gas()
    mirra.brakes()
