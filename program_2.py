#title:car class
#author: michael stoll
#date:4/2/2025
class Car:
    def __init__(self, speed, make, year_model):
        self.year_model = year_model
        self.make = make
        self.speed = speed

    def accelerate(self, speed):
        self.speed += speed

    def brake(self, speed):
        self.speed -= speed

    def get_speed(self):
        return self.speed