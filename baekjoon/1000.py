'''
A+B https://www.acmicpc.net/problem/1000

입력)
첫째 줄에 A와 B가 주어진다. (0 < A, B < 10)
1 2

'''

# 입력함수 : 변수 = input() 
# - 한줄입력받습니다. enter 입력이 종료
# - input('가이드 내용') : 입력에 대한 가이드
# - 무조건 문자열타입

# 입력받은 것을 출력해보기
# x=input('id:')
# y=input('pw:')

# print(x)
# print(y)

y= input()
# type(데이터)
# print(type(y))

# split() : 문자열 -> 리스트
lst = y.split(" ")
# print(lst)

x=int(lst[0])
z=int(lst[1])

# print(x) # x=1 ['1']
# print(z) # z=2 []


sumnum=x+z
print(sumnum)




##### 정리

# 한줄에 여러개의 입력이 들어간다
y= input().split()

# 문제를 봤는데 무조건 숫자로만 사용이된다.
# int(y) <= 리스트는 int로 변형이 안됩니다.
a = int(y[0])
b = int(y[1])

# ValueError: not enough values to unpack (expected 2, got 1)
# ValueError: 압축을 풀 수 있는 값이 충분하지 않습니다(2개 예상, 1개 획득).



# 과제) 
# A-B https://www.acmicpc.net/problem/1001
# 두 수 비교하기https://www.acmicpc.net/problem/1330
# 나머지 https://www.acmicpc.net/problem/10430
# 별찍기-1 https://www.acmicpc.net/problem/2438

x=int(input())

for i in range(1,x+1):
    print(i*"*")








