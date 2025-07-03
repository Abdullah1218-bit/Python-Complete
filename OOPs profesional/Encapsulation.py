class CPU:
    def __init__ (self,brand,price,ram,processor,gpu,cabnet):
        self.brand=brand
        self.price=price
        self.__ram=0      ## Private variable using double underscore
        self.processor=processor
        self.gpu=gpu
        self.cabnet=cabnet


        if ram>=16 :
            self.__ram=ram
        else:
            print('Ram must be between 16 and 32')

    def __str__(self):

        return f"CPU(brand={self.brand}, price={self.price}, ram={self.__ram} GB, processor={self.processor}, gpu={self.gpu}, cabnet={self.cabnet})"

    # def __repr__(self):
    #     return f"CPU(brand={self.brand}, price={self.price}, ram={self.ram}, processor={self.processor}, gpu={self.gpu}, cabnet={self.cabnet})"


a=input("Enter the Brand : ")
b=input('Enter the price : ')
c=int(input('Enter the Ram (in GB): '))
d=input('Enter the Processor : ')
e=input('Enter the GPU : ')
f=input('Enter the Cabnet : ')


cpu1 = CPU(a,b,c,d,e,f)
print(cpu1)
