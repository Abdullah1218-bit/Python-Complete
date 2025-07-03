class Animal:         # Parent class
    def __init__(self, name, color, age, weight):
        self.name = name
        self.color = color
        self.age = age
        self.weight = weight

class Dog(Animal):  # inheritance of Animal  # Child class
    def __init__(self, name, color, age, weight, breed):
        super().__init__(name, color, age, weight)  # super means upper
        self.breed = breed

    def __str__(self):
        return f"Dog(name={self.name}, color={self.color}, age={self.age}, weight={self.weight}, breed={self.breed})"

    # def bark(self):
    #     print("Woof woof")


dog1 = Dog("Candy", "Black", 3, 15, "German Sheperd")
print(dog1)
# dog1.bark()
