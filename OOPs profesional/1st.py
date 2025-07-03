
# Method	Defined inside a class.


class Car :

    def __init__(self,brand,model):   #brand and model are parameters

        self.__brand=brand # brand is attribute
        self.model=model # model is attribute

    

    def name(self):
        return f'{self.__brand} {self.model}' 
    
    def get_brand(self):  # <-- Moved here
        return f'{self.__brand} {self.model}'

my_car=Car('Toyota','Revo')

print(my_car.get_brand)
print(my_car.model)
print(my_car.name())


my_new_car=Car('Lamborghini','Aventador') 

print(my_new_car.get_brand)
print(my_new_car.model)


class Electric_Car(Car) :
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)  # super means uper 
        self.battery_size=battery_size
my_tesla=Electric_Car('Tesla','Model S',75)

# print(my_tesla.__brand())         
print(my_tesla.get_brand())    
