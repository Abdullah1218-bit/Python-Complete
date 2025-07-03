class employee:
    language= 'Python'
    salary= '5 rupay'
    name='Agu'                 #THIS IS CLASS ATTRIBUTE
    

Ali = employee ()
Ali.salary='17.8 rupay'  
print(Ali.language , Ali.salary,Ali.name)

Ahmed = employee ()
Ahmed.name=('mein','tum','you','me')           #This is object or instance attribute        
Ahmed.salary='10 rupay'   
print(Ahmed.language , Ahmed.salary,Ahmed.name)

Ahmer = employee ()
Ahmer.name=('Ah','mer')                          #This is object or instance attribute      
print(Ahmer.language , Ahmer.salary,Ahmer.name)

# Instance attrivute take preference over class attribute during assignment or retrieval

