class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def start(self):
        return f"{self.brand} {self.model} is starting."

# Inheriting the Vehicle class
class Car(Vehicle):
    def __init__(self, brand, model, doors):
        super().__init__(brand, model)
        self.doors = doors

    def honk(self):
        return "Honk! Honk!"

# Create an object of Car
car = Car("Toyota", "Corolla", 4)
print(car.start())  # Output: Toyota Corolla is starting.
print(car.honk())   # Output: Honk! Honk!
