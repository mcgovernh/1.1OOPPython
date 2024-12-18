class Bird:
    def fly(self):
        return "Most birds can fly."

class Penguin(Bird):
    def fly(self):
        return "Penguins can't fly."

# Polymorphism in action
def bird_flight(bird):
    print(bird.fly())

sparrow = Bird()
penguin = Penguin()

bird_flight(sparrow)  # Output: Most birds can fly.
bird_flight(penguin)  # Output: Penguins can't fly.
