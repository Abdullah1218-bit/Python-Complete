#  #  if elif else LADDER

# a=(int(input('Enter you age: ')))
# if (a>=15):
#     print('you are allowed')
# elif(a<0):
#     print('You are an idiot')
# elif(a==0):
#     print('0 is invalid age')
# else:
#     print('You are not allowed') 

# a=(int(input('Enter total budget:  ')))
# b=(int(input('Enter price of gaming pc:  ')))

# if a - b >= 5000:
#     print('you can buy')

# elif 1 < a - b < 2500:
#     print('Buy at your own risk')

# elif a - b == 0:
#     print('Remains nothing')
    
# else:
#     print('you can`t buy')


                       #GREATEST NUMBER



# a1=(int(input('Enter a1: ')))
# a2=(int(input('Enter a2: ')))
# a3=(int(input('Enter a3: ')))
# a4=(int(input('Enter a4: ')))
# if (a1>a2 and a1>a3 and a1>a4):
#     print('a1 is greatest number:', a1)
# elif (a2>a1 and a2>a3 and a2>a4):
#     print('a2 is greatest number:', a2)
# elif (a3>a2 and a3>a1 and a3>a4):
#     print('a3 is greatest number:', a3)
# else:
#     print('a4 is the greatest number:',a4) 


                              # TOTAL MARKS 

# marks1=int(input('Enter marks1: '))
# marks2=int(input('Enter marks2: '))
# marks3=int(input('Enter marks3: '))
# marks4=int(input('Enter marks4: '))

# # Calculating total and percentage
# total_marks = marks1 + marks2 + marks3 + marks4
# total_percentage = (total_marks / 400) * 100

# # Checking pass conditions
# if   marks1 >= 33 and marks2 >= 33 and marks3 >= 33 and marks4 >= 33:
#     print('You\'re passed with', total_percentage, '%')
# else:
#     print('You\'re failed with', total_percentage, '%')


                                    #PRESNET OR ABESNT
# l=['Ali','Abdullah','Ahmed','Asim']
# a=(input('Enter your name: '))   
# if (a in l):
#     print('Name is correct')
# else:
#     print('Name is incorrect')

                             # CALCULATE GRADE
# marks= ( int(input('Enter your marks: '))) 

# if marks>=90 and marks<=100:
#     print('A+',marks)  

# elif marks>=80 and marks<=90:
#     print('A Grade',marks)  

# elif marks>=70 and marks<=80:
#     print('B+ Grade',marks) 

# elif marks>=60 and marks<=70:
#     print('B Grade',marks)  

# elif marks>=50 and marks<=60:
#     print('C Grade',marks) 

# elif marks<50:
#     print('Your marks is less then 50%')        

# else:
#     print('Your marks is incorrect')


                         # Given post is talking about you or not
post=(input('Write a post: '))
if ('Ali'.lower() and 'Ahmed'.lower() in post.lower()):
    print('Ali and Ahmed are in post')
else:
    print('Ali and Ahmed are not in given post')






    
