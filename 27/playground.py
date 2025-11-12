# def add(*args):
#     x = sum(args)
#     return x
#
#
# lol = add(1, 2)
# print(lol)


def calc(**kwargs):
    for key, value in kwargs.items():
        print(key)
        print(value)

class Car:
    def __init__(self,**kwargs):
        self.make = kwargs.get("make")
        self.model = kwargs.get("model")


calc(add=3, multiply=5)

car = Car(make="Ford", model="Mustang")
print(car.make)