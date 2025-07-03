# def function():
#     a=int(input('Enter the number of a : '))
#     b=int(input('Enter the number of b : '))
#     c=int(input('Enter the number of c : '))
#     if a>b and a>c:
#         print(a,'is the greatest number') 
#     elif b>a and b>c:
#         print(b,'is the greatest number') 
#     else:
#         print(c,'is the greatest number') 
# function()



#                            #2nd 
# def f_to_c(f):
#     return   (5/9) * (f - 32)
# f=int(input('Enter the temperature Farenheit : '))
# c=f_to_c(f)
# print(f'{round(c,2)} °C')



                          #3rd
def table():
    a=int(input('Enter the number: '))
    for i in range(1,11):
        print(f'{a} X  {i} = {a*i}')
table()
