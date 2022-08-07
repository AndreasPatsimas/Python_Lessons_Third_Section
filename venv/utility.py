print(__name__)
class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def __str__(self):
        return f"Car = [brand: {self.brand}, color: {self.color}]"


def sum(num1, num2):
    return num1 + num2