'''
https://www.acmicpc.net/problem/25304
'''
x=int(input())
n=int(input())

a=[]
b=[]

for i in range(n):
    price,count=list(map(int,input().split(" ")))
    a.append(price)
    b.append(count)

tot=0
for i in range(n):
    avg=a[i]*b[i]
    tot+=avg

if (tot==x):
    print("Yes")
else:
    print("No")

