'''
오븐시계  https://www.acmicpc.net/problem/2525
'''

starta,startb=list(map(int,input().split()))

need=int(input())

# print(starta,startb)
# print(need)

time1=startb+need

if(time1>=60):
    starta=(starta+(time1//60))%24
    time1=time1%60

    print(starta,time1)
else:
    print(starta,time1)