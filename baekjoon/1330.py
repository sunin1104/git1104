x=input()

y=x.split(" ")

a=int(y[0])
b=int(y[1])

if(a>b):
    print(">")
elif(a<b):
    print("<")
else:
    print("==")
    