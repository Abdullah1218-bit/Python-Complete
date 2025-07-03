# 5!= 1 X 2 X 3 X 4 X 5        DEFINITION OF FACTORIAL

n=(int(input('Enter the number: ')))
p=1
for i in range(1,n+1):
    p=p*i
print({f"The factorial of {n} is {p}"})
