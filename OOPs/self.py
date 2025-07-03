class employee:


    language='python'          # this is class attribute
    grade='A+'
    salary='75 rupay'


    def __init__(self):  # dunder method which is automatically called  , __init__ is called onstructor
        print('he is creating langauge') 

    def getinfo(self):
        print(f'The language is {self.language} and the salary is {self.salary}')

    @staticmethod

    def greet():           #in staticmethod we cant type in (this)
        print('Good Morning!')

Ali=employee()

# Ali.langauge='Js'                #THIS IS INSTANCE OR OBJECT ATTRIBUTE

Ali.greet()

Ali.getinfo()

# employee.getinfo(Ali)
