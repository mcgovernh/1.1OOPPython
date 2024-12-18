class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self, sound):
        return f"{self.name} says {sound}"

# Create an object
dog = Animal("Buddy", "Dog")
print(dog.make_sound("Woof"))  # Output: Buddy says Woof
