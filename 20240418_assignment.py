#2번
class Car:
    color = ""
    speed = 0

    def upSpeed(self, value):
        self.speed += value

#4번
class Horse:
    speed = 0

    def __init__(self):
        self.speed = 50

#6번 답 : 3 (슈퍼 클래스 서브 클래스)
class Car :
    def method(self):
        print("슈퍼 클래스")

class Sedan(Car) :
    def method(self):
        print("서브 클래스")

myCar = Car()
mySedan = Sedan()
myCar.method()
mySedan.method()

#7번
class Car :
    speed = 0

    def upSpeed(self, value):
        self.speed = self.speed + value

class RVCar(Car) :
    seatNum = 0

    def getSeatNum(self):
        return self.seatNum