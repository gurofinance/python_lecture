class Car :
    # 자동차의 필드(property)
    color = ""
    speed = 0

    # 자동차의 메서드(Method)
    def upSpeed(self, value) :
        self.speed += value

    def downSpeed(self, value) :
        self.speed -= value


car = Car()
print(car.speed)
car.upSpeed(500)
print(car.speed)