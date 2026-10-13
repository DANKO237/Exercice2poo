class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def show_info(self):
        return f"{self.brand} {self.model}"


class Car(Vehicle):
    def __init__(self, brand, model, doors):
        super().__init__(brand, model)
        self.doors = doors

class Motorbike(Vehicle):
    def __init__(self, brand, model, engine_size):
        super().__init__(brand, model)
        self.engine_size = engine_size

car = Car("Toyota", "corolla", 4)
motorbike = Motorbike("Yamaha", "MT-07", 689)

print(car.show_info())
print(motorbike.show_info())

# ils peuvent utiliser show_info() sans la redefinir car ils herite de la class Vehicle
# donc il heritent aussi de ces attributs



