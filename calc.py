import math
# 제곱
def pow2_def(p2_a,p2_b):
    p=math.pow(p2_a,p2_b)
    return p

# 세제곱
def pow3_def(p3):
    num=3
    p=math.pow(p3,num)
    return p

# 나누기
def divi_def(a,b):
    if b==0:
        return 'error'
    return a/b

# 1부터 n까지의 정수를 곱하는 팩토리얼 만들기

def fac_def(n):
    f=math.factorial(n)
    return f

pow2_def(2,3)
pow3_def(2)
divi_def(18,3)
fac_def(3)