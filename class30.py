# 알고리즘 하루에 2문제씩 풀어보기
# 잔디밭 
# - 1일 1커밋 => 프로젝트

# =============================================
# Calculator 클래스 과제
# ---------------------------------------------
# ✅ 클래스 이름: Calculator
#
# ✅ 속성 (Attributes):
# - current_value: 현재 계산된 값 (초기값은 0)
#
# ✅ 메서드 (Methods):
# - add(x): 현재 값에 x를 더함
# - subtract(x): 현재 값에서 x를 뺌
# - multiply(x): 현재 값에 x를 곱함
# - divide(x): 현재 값을 x로 나눔 (0으로 나누기 예외 처리)
# - clear(): 현재 값을 0으로 초기화
# - get_value(): 현재 값을 반환

class Calculator:
    def __init__(self):
        self.current_value=0
    
    def add(self,x):
        self.current_value+=x

    def subtract(self,x):
        self.current_value-=x
    
    def multiply(self,x):
        self.current_value*=x

    def divide(self,x):
        if x==0:
            print('error')
        else:
            self.current_value/=x

    def clear(self):
        self.current_value=0

    def get_value(self):
        return self.current_value

c=Calculator()
c.add(3)
c.subtract(5)
print(c.get_value())


# 
# https://www.acmicpc.net/problem/11720
# https://www.acmicpc.net/problem/11721


