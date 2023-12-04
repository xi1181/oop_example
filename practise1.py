class Car:
    def __init__(self, m1, m2, y):
        self.make = m1
        self.model = m2
        self.year = y
        self.speed = 0

    def accelerate(self, speedi):
        self.speed += speedi

    def decelerate(self, speedd):
        self.speed -= speedd

car1 = Car("Nissan", "ZoomZoom", 2023)
print("Current speed: " + str(car1.speed))
car1.accelerate(25)
print("New speed: " +str(car1.speed))

print(car1.make)
car1.make = "Toyota"
print(car1.make)