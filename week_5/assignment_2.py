# Assignment 2
class Vehicle:
    def move(self):
        pass

class Car(Vehicle):
    def move(self):
        print(f"Driving")

class Plane(Vehicle):
    def move(self):
        print("Flying")

vehicles = [Car(), Plane()]
for v in vehicles:
    v.move()

