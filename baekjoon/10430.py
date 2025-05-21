x=input('2<=A,B,C<=10000')

y=x.split(" ")

a=int(y[0])
b=int(y[1])
c=int(y[2])

a1=(a+b)%c
a2= ((a%c) + (b%c))%c
b1= (a*b)%c
b2=((a%c) * (b%c))%c

print(a1)
print(a2)
print(b1)
print(b2)