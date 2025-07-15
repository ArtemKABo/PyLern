#задача 15.1

class Transport:
    nаme = "Телега"
    max_speed = 10
    mileage = 50
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

Autobus = Transport("Renoilt Logan", 180, 12)

print(f"Название автомобиля: {Autobus.nаme} Скорость: {Autobus.max_speed} Пробег: {Autobus.mileage}")