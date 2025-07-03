class Teacher:
    def __init__ (self,name,subject,experience):
        self.name=name
        self.subject=subject
        self.experience=experience

    def __str__ (self):
        return f'The teacher name is {self.name}, and his/her subject is {self.subject}, and his/her experience is {self.experience} years.'
    
teacher1= (Teacher('Rahul','Python',5))
teacher2=(Teacher('Asikawa','Java',10))

teacher3=(Teacher("Anasuth",'NodeJS',3))

print(teacher1)
print(teacher2)
print(teacher3)