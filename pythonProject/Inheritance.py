class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass # will be overridden by child class

class Dog(Animal):
    def speak(self):
        return f"{self.name} barks"

class Cat(Animal):
    def speak(self):
        return f"{self.name} meows"


dog = Dog("doggo")
print(dog.speak())
cat1 = Cat("bob")
print(cat1.speak())