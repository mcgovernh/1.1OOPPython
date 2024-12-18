class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower

    def start(self):
        return "Engine started."

class Car:
    def __init__(self, brand, model, engine):
        self.brand = brand
        self.model = model
        self.engine = engine

    def start(self):
        return f"{self.brand} {self.model} is starting with {self.engine.start()}"

# Create an Engine object
engine = Engine(150)

# Create a Car object with the Engine
car = Car("Honda", "Civic", engine)
print(car.start())  # Output: Honda Civic is starting with Engine started.
