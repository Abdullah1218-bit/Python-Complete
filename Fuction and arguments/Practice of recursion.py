# '''
# sum(3)=1+2+3
# sum(5)=1+2+3+4+5
# '''

# def sum(n):
#     if n==1:
#         return 1
#     return sum (n-1)+n
# print(sum(5))


                    # 2nd

# def pattern(n):
#     if n==0:
#         return
#     print('*' * n)
#     pattern(n-1)
# n=int(input('Enter the stars: '))
# pattern(n)           
      
#                                3rd
# def inch_to_cms(inch):
#     return inch * 2.54
# n=float(input('Enter value in inches: '))
# print(f'{n} inches is equal to {inch_to_cms(n): .2f} centimetres.')






                                  #4th
def rem(list,word):
    n=[]
    for items in list:
        if not(items==word):
            n.append(items.strip(word))
    return n
list=['llalo','Tall' , 'Mall' , 'Hall' , 'Ball' ]

print(rem(list,'ll'))