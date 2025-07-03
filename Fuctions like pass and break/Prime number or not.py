a=int(input('Enter the number: '))
for r in range(2, a ):
    if(a%r) == 0:
        print('This is not a prime number')
        break
else:
        print('Number is prime')
