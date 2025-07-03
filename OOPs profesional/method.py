class animal:
    def __init__ (self,name,age):
        self.name=name
        self.age=age

        
    def __str__(self): # str means string
        return f"Animal(name={self.name}, age={self.age})"
    
my_animal1=animal("dog",2)
print(my_animal1)

my_animal2=animal("cat",1.6)
print(my_animal2)