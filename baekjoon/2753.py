'''
https://www.acmicpc.net/problem/2753
'''
year=int(input())

# 4의 배수 : 4로 나눴을때, 나머지가 0
if year%4==0 and year%100!=0:
    print("1")
# 100의 배수가 아니면서, 400의 배수가 아니면서
# 100의 배수 : 100으로 나눴을때 나머지가 0

# 4의 배수가 아니거나 100의 배수인 숫자가 내려온다.  
# 3
# 6
# 100
# 200


elif year%400==0:
    print("1")
    
# 400
else:
    print("0")



print("========= 답안 예시 ==============")

# 연도가 주어졌을 때, 윤년이면 1, 아니면 0을 출력하는 프로그램을 작성하시오.
# 윤년은 ( 연도가 4의 배수이면서,and 100의 배수가 아닐 때 ) 또는or (400의 배수)일 때이다.

if (year%4==0 and year%100!=0) or (year%400==0):
    print("1")
else:
    print("0")