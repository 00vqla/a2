class Dog:
    def __init__(self, name, breed, age):
        self.__name = name
        self.__breed = breed
        self.__age = age

    def get_age(self):
        return self.__age

    def get_breed(self):
        return self.__breed

    def get_name(self):
        return self.__name


dog1 = Dog("bob", "chihuahua", 12)
print(dog1.get_name())
