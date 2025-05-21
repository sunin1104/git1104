# 시험점수 ) https://www.acmicpc.net/problem/5596

s=list(map(int,input().split()))
t=list(map(int,input().split()))

# 100

tot1=0
tot2=0

for i in range(len(s)):
    tot1+=s[i]
    avg1=tot1/len(s)

for i  in range(len(t)):
    tot2+=t[i]
    avg2=tot2/len(t)

if avg1>avg2:
    print(tot1)
elif avg1==avg2:
    print(tot1)
if avg2>avg1:
    print(tot2)
