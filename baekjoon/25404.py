'''

영수증 https://www.acmicpc.net/problem/25304

문제)영수증에 적힌,

구매한 각 물건의 가격과 개수
구매한 물건들의 총 금액
을 보고, 구매한 물건의 가격과 개수로 계산한 총 금액이 영수증에 적힌 총 금액과 일치하는지 검사해보자.

입력)
첫째 줄에는 영수증에 적힌 총 금액 X가 주어진다.
둘째 줄에는 영수증에 적힌 구매한 물건의 종류의 수 N이 주어진다.
이후 N개의 줄에는 (각 물건의 가격 a와 개수 b가 공백을 사이에 두고) 주어진다.

'''
# 입력예제
# 260000  => 총금액 X
# 4       => 구매한 항목의 갯수 N
# 20000 5
# 30000 2
# 10000 6
# 5000 8


# x=int(input())
# n=int(input())

# # 이후 N개의 줄에는 (각 물건의 가격 a와 개수 b가 공백을 사이에 두고) 주어진다.
# # 입력데이터를 리스트에 저
# arr=[]

# for i in range(n):
#      # 20000 5
#      m=input().split(" ")
#      # 입력받은 데이터m를 빈리스트arr에 추가해주기
#      arr.append(m)
# print(arr)


# 문자열.split() : 문자열을 잘라서 리스트 방벙


# 리스트(=배열) []
# 리스트이름 = [요소,요소,요소]
# 추가 리스트.append()
# 삭제 리스트.pop()
# 수정 : 인덱싱 = 변경할값



############### map() ####################
# a = ['20000 5', '30000 2', '10000 6', '5000 8']
# a1= '20000 5'.split()
# print(int(a1))
# a1_num = int('20000')

# a_arr = ['20000', '5']
# print(a_arr)
#니즈 : 리스트안의있는 모든 요소에 int()
#map(함수이름,리스트) : 리스트의 모든 요소에 함수을 적용할때 사용하는 함수

# 반복이 가능한 map객체 : <map object at 0x0000026B8D1AAF50>
# print(list(map(int, a_arr)))

# b_arr = ['apple','mango','kiwi']
# 모든 과일이름의 길이를 출력해주세요. => 모든 요소에 대해서 len함수를 적용하기
# print(list(map(len,b_arr)))



# (1) 입력값이 반드시 숫자라면 int() 
# int(input()) 문자열 타입

# (2) 입력값이 한줄에 여러개 입력받는 경우, 입력받은 문자열을 리스트로 만들어주어야한다.
# input().split()

# (3) (1)과(2) 동시적용 
# 한줄에 여러개 입력을 받았는데, 반드시 숫자타입이라면, 모든 데이터(리스트)를 Int()적용시켜야한다.
# list(map(int,input().split()))

# a = a_arr[0]
# b = a_arr[1]

# a_arr = [20000, 5]
# b_arr = [5, 5, 4]
# (4)변수 다중할당 : 리스트의 갯수만큼 변수를 생성하고 싶을때
#- 리스트의 갯수와 생성할 변수의 갯수 같다
# a,b = a_arr 

# (1),(4),(5)
# a,b = list(map(int,input().split()))




n=int(input())

for i in range(n):
    print(" "*i+(n-i)*"*")
