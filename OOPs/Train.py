from random import randint

class train:

    def __init__(slf,trainNo):

        slf.trainNo=trainNo

    def book( self,fro,to):


            print(f'Ticket is booked in {self.trainNo} , {fro} , {to}')
    def getstatus ( self,fro,to):


            print(f'Train {self.trainNo} , {fro} , {to} on time' )
    def getfare ( self,fro,to):


            print(f'Ticket fare of Train {self.trainNo}, From: {fro}, To: {to} is {randint(1500, 12500)}.Rs')

t=train(821)
print(f'Train Number: {t.trainNo}')

# Calling methods
t.book("Rawalpindi", "Karachi")
t.getstatus("Rawalpindi", "Karachi")
t.getfare("Rawalpindi", "Karachi")
