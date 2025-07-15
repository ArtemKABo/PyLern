#задача 15.2
class Transport:
    name ="Тачка"
    max_speed = 50
    mileage = 0

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
 

    def seating_capacity(self, capacity):
        return f"Вместимость одного автобуса {self.name}  {capacity} пассажиров"

 

class Autibus(Transport):
    seating_position = 50

    def seating_capacity(self):
        return f"Вместимость одного автобуса {self.name}: {self.seating_position} пассажиров"
     
t = Autibus("Renaul Logan", 120,5000)
print(t.seating_capacity())