marks={
    "ali": 21,
    "abdullah": 45,              #THERE IS A COMA , AS A STATEMENT TERMINATOR AND THERE IS A RATIO B/W
    "DJ": 73,                    #THEM :
    "pubg": 98,
    ### 0:'items'

}
print(marks['ali'])               #THERE IS A [] BRACKET INSTEAD OF ()
print(marks['pubg'])
## print(marks[0])
                               
                                   #ITEM METHOD


print(marks.items())   
                            
                            
                              #Keys method


print(marks.keys())
                     
                     
                        #update method


marks.update({'ali': 26})
print(marks)
                         #GET method
print(marks.get('ali'))
print(marks.get('huehue'))          #Invalid name=None


 
print(marks.get('rays'))           #IT RETURNS None

# print(marks['dueh'])            #IT RETURNS ERROR
                                    

