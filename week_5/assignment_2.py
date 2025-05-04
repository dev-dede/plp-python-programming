# Assignment 2
class Object:
    def move(self):
        pass

class Car(Object):
    def move(self):
        print(f"Driving")

class Plane(Object):
    def move(self):
        print("Flying")

plane = Plane()
plane.move()
print(f"-------------")
car = Car()
car.move()