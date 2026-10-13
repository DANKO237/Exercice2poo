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

    def show_info(self):
        return f"Voiture : {self.brand}{self.model} - {self.doors} portes"

class Motorbike(Vehicle):
    def __init__(self, brand, model, year, engine_size):
        super().__init__(brand, model, year)
        self.engine_size = engine_size

    def show_info(self):
        return f"Moto : {self.brand}{self.model} - 689 cc"

vehicles = [ Car("Toyota", "Corolla", 4), Motorbike("Yamaha", "MY-07", 689),
Car("Honda", "Civic", 4)]
for vehicle in vehicles:
    vehicle.show_info()

#python n'execute pas la methode show_info() de Vehicle pour un object Car
# parceque 