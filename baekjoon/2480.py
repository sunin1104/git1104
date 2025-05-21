# 주사위 세개) https://www.acmicpc.net/problem/2480

import random

rand_lis=[random.randint(1,6) for _ in range(3)]

print(rand_lis)
ran_num=[]
ran_num2=[]

for i in range(len(rand_lis)):
    if rand_lis.count(rand_lis[i])>1:
        if rand_lis[i] not in ran_num:
            ran_num.append(rand_lis[i])
            if rand_lis.count(rand_lis[i])==2:
                ran_num2.append(rand_lis[i])

if len(ran_num)==1:
    prize=10000+ran_num[0]*1000
    print(prize)

elif len(ran_num2)==1:
    prize=1000+ran_num[0]*100
    print(prize)

else:
    prize=sorted(rand_lis, reverse=True)[0]*100
    print(prize)

