# 리스트의 활용
num = [50, 60, 35, 22, 43, 99]

# 누적합계 방식
total = 0
for i in range(len(num)):
    total+=num[i]

# sum(리스트) : 리스트의 요소 전체 합계 구하는 함수
sum(num)
print(sum(num))

# 정렬 <= 간단
# (1) 리스트변수.sort() : 
# (2) sorted(리스트, reverse=True)  : 오름차순으로 정렬
#- reverse=True : 내림차순
# none : 존재하지않는다. (=null)
print(num.sort()) #(1) 원본을 정렬하는 함수
print(num)
print("----sorted() 정렬 --------")
# 원본은 존재, 정렬한 새로운 리스트를 반환
num = [50, 60, 35, 22, 43, 99]
print(sorted(num,reverse=True))
print(num)


# 길이순서대로 정렬하기
string = ["아메리카노","카페라떼","초코라떼","녹차","우유"]
sorted(string,key=len)
print(sorted(string,key=len))


# 리스트.count("찾는문자") : 리스트안에 요소가 몇개가 있는지 세서 갯수로 반환
# A가 몇개들어가있는가
lst = ['A','B','C','A',"A",'A']
print(lst.count("A"))

# 문자열.find("찾는무자") : 문자열 인덱스 찾기
# 리스트.index("찾는문자") : 리스트 인덱스 찾기

print(lst.index("C"))


# <중복을 제거하는 알고리즘>
# a라는 출석기록가있다. 출석인원은 몇명인가
a = ['짱구',"철수","유리","짱구","짱구","훈이","훈이","맹구","신형만"]
# (1) 출석명부를 작성할 리스트 : 중복 안되는 것만 넣기
lst=[]

# <조건 표현식>
# (1)비교연산자 == != > < >= <=
# (2) 논리연산자 and , or , not
# (3) 포함연산자 :  리스트(배열)에 포함되어 있는지 
# - "찾는문자" in 리스트 : 있으면 True 없으면 False
# - "찾는문자" not in 리스트  : 없으면 True 있으면 False

for i in range(len(a)):
    print(a[i]) 
    # 만약에 출력한 값이 출석명부에 포함되어 있지 않으면 / 출석명부에 추가해준다. 있으면 아무것도 안함
    if a[i] not in lst:
        lst.append(a[i])
print(lst) 

####################################
# 이차원배열(=이차원리스트)
# : 리스트안에 리스트 있는 데이터타입 (<= 리스트 )

['a','b','c','d','e']
a = [
    # 행의 요소 : 열(=칸)
    ['a','b','c','d','e'], # 내부리스트 (행 - 줄) 0행
    ['a','b','c','d','e'], # 1행
    ['a','b','c','d','e'], # 2행
    ['a','b','c','d','e'], # 3행
    ['a','b','c','d','e']  # 4행
    ]
# 행번호 열접근
# a[행번호][열번호]
print(len(a))

