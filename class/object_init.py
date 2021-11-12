class Car :
    name = ""
    color = ""
    speed = 0

    def __init__(self, name="fff", color="ffwfwf", speed=10) :
        self.name = name
        self.color = color
        self.speed = speed

    def getName(self) :
        print("차종 :", self.name)
        return self.name

    def getColor(self) : 
        print("차량 색상 :",self.color)
        return self.color

    def getSpeed(self) :
        print("차량 속도 :",self.speed)
        return self.speed


car1 = Car()
car2 = Car("벤츠", "Black", 110)

print(f"==>{car1.getName()}의 현재 색상은 {car1.getColor()}, 현재 속도는 {car1.getSpeed()}km/h 입니다. \n")
print(f"==>{car2.getName()}의 현재 색상은 {car2.getColor()}, 현재 속도는 {car2.getSpeed()}km/h 입니다.")
print(type(4))