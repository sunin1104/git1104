'''
이차원리스트(=이차원배열)
: 배열안에 배열이 있는 타입
'''

# 5행 
number_list = [
    # 열(칸) : 내부리스트의 요소
    [1,2,3,4,5],            # 0행: 내부리스트
    [6,7,8,9,10],           # 1행
    [11,12,13,14,15,16],
    [17,18],
    [19,20,21,22,23]
    ]

# 행의 갯수를 출력해주세요.
# - 행도 number_list의 요소
b = [[],[],[],[],[]]
a = ['a','b','c','d','e']

# a의 요소 갯수 = len(a)
print(len(a))
# b의 요소의 갯수 =b 행의 갯수
print(len(b))

# number_list의 행의 갯수를 출력해주세요.
print(len(number_list))

# (1) number_list / 의 0번행 / 의 열의 갯수를 출력하고싶다. 
# - 열의 갯수 = 행의 길이
# number_list / 의 0번행 
x = number_list[0]
print(len(x))

'''
1. 지금 갖고있는 데이터가 무슨타입이고 뭐가 저장되어있는지 check
    => print()
    => 한줄 코드 한줄 프린트
    => 에러가 나면 정상 안나면 이상하다.

2. 내가 뭘해야할지 => 단계별로 설계
3. 설계를 바탕으로 코딩
    - 내가 갖고있는 데이터타입과 내가 해야하는 것이 미스매칭 => 데이터 타입 변화
    - type()
    - 메서드 검색 
'''

num1 ="1"
num2 = "2"

# 몇자리 숫자인가요? 4자리수
# 숫자 
num3 = 1879
print(len(str(num3)))
# 정렬 : 여러개중에서 순서를 세우는것
# sorted(num3)

# TypeError: object of type 'int' has no len()


# 이차원 리스트 => 배열, 리스트
number_list = [
    # 열(칸) : 내부리스트의 요소
    [1,2,3,4,5],            # 0행: 내부리스트
    [6,7,8,9,10],           # 1행
    [11,12,13,14,15,16],
    [17,18],
    [19,20,21,22,23]
    ]

# 15는 몇번째행 몇번째열 => 2행 / 4열 
# 인덱싱 해주세요.
# x=[11, 12, 13, 14, 15, 16]
x=number_list[2] # x는 리스트
print(x)
print(x[4])

# print(number_list[행][열])


# 18을 출력해주세요.
print(number_list[3][1])


print("\n#########################################")
# 워밍업 리스트의 모든값을 뽑아보세요.=> 인덱싱
x=[11, 12, 13, 14, 15, 16]

# 리스트의 모든값을 뽑아보세요. => 반복문 외워오기
for i in range(len(x)):
    print(x[i])

print("\n#########################################")
# 이차원리스트 뽑아보기
number_list = [
    [1,2,3,4,5],            # 0행: 내부리스트
    [6,7,8,9,10],           # 1행
    [11,12,13,14,15,16],
    [17,18],
    [19,20,21,22,23]
    ]

# 코딩 : 순차적으로 실행되는 구조 
# - 위에 Error 아래는 실행을 안합니다.
# - 위엑 정상 아래는 내가 할것하면 된다.

for i in range(len(number_list)):
    # 행이 출력된다. => 리스트
    x=number_list[i]
    print(x)
    # 확인해 => 예상한 결과가 맞아요 ok 아니야 수정 
    # x는 리스트 => 모든값을 뽑아보자.
    for j in range(len(x)):
        print(x[j])


print("\n################################")
for i in range(len(number_list)):
    # 행이 출력된다. => 리스트
    x=number_list[i]
    # 확인해 => 예상한 결과가 맞아요 ok 아니야 수정 
    # x는 리스트 => 모든값을 뽑아보자.
    for j in range(len(x)):
        print(x[j])



for i in range(len(number_list)):
    for j in range(len(number_list[i])):
        print(number_list[i][j])











 
