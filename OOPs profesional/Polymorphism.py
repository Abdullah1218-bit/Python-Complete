#Same function or method name, but different behavior depending on the object.

class Dog:
    def speak (self):
        print('BHAU BHAU BHAU')

class Cat:
    def speak (self):
        print('MEOW MEOW MEOW')


 # Polymorphic function - works with any animal
def animal_sound(animal):
        animal.speak()

d=Dog()
c=Cat()

animal_sound(d)
animal_sound(c)
