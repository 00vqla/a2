# Single inheritance

class Dog:
    def __init__(self, name):
        self.name = name

    def display_name(self):
        print(f"Dog's name: {self.name}")


class Labrador(Dog):  # Single Inheritance
    def sound(self):
        print("Labrador woofs")


# Multilevel inheritance
class GuideDog(Labrador):
    def guide(self):
        print(f"{self.name} guides the way")


# Multiple inheritance
class Friendly:
    def greet(self):
        print("Friendly")


class GoldenRetriever(Dog, Friendly):
    def sound(self):
        print("Golden Retriever barks")


lab = Labrador("Bob")
lab.display_name()
lab.sound()

gd = GuideDog("Bob2")
gd.display_name()
gd.sound()

gr = GoldenRetriever("Bob3")
gr.display_name()
gr.greet()
gr.sound()
