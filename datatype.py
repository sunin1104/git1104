# 첫번째 단기 : 이틀
# 


# 과제)
# 정리 - 데이터타입변환 정리해오기.
# - 코드 써서 실행까지 예시 작성해오기. (숫자,문자열,불, 리스트,딕셔너리,튜플,집합)

# 1. 숫자 타입
# (1) 정수형 int
# (2) 실수형 float

# 연산자: +,-,/,*,%,//,** 가능
# 대입연산자: +=,-=,*=,/=,%=,//=,**= 가능


# 2. 문자열 타입
# (1) "",'' 안에 문자와 숫자 상관없이 구성된 데이터 타입

# 연산자: +,*

# len(): 문자열 길이 구하는 함수

# str(): 데이터를 문자열로 변환해주는 함수수
# 문자열은 순서가 존재한다. >> 인덱스 가능 >> 인덱싱, 슬라이싱 가능 => 반복문

# ex)
num= '1,2,3,4,5'

# 인덱싱
print(num[0])

# 슬라이싱
print(num[2:])

# .repalce() 특정 문자 수정해주는 메서드
print(num.replace(',','-'))

# .split() 특정 문자 기준으로 리스트 생성
print(num.split('-'))

# 3. bool 타입          => 조건문
True
print(bool(1+3))

False
print(bool(0))
print(bool([]))
print(bool(''))

# 4. 리스트 타입
# 여러개의 데이터(모든 데이터) 저장 가능

# len(): 리스트의 길이 구하는 함수

# 인덱스, 인덱싱, 슬라이싱 가능

# list() : 튜플, 각각의문자들로 리스트만들때, 딕셔너리의 key값만 리스트
# = tuple()
# = set()  

print("===================")
str1='a,b,c,d,e,f,g'
dict1={'int':1,'str':'hi'}
print(list(dict1))          # ['int', 'str']

int1=2

print(list(str1))
print(int1)
# print(list(int1))

# print(int(['1','2']))
lst=[1,2,3,4,5]

# 인덱싱
print(lst[0])

# 슬라이싱
print(lst[2:])

# 추가, 수정, 삭제 가능
# 추가 .append() / append는 리스트를 수정하지만 return 값이 없어서 바로 print를 사용하면 none이 출력 됨.
lst.append('!')
print(lst)

# 수정 =
lst[-1]='?'
print(lst)

# 삭제 .pop()
lst.pop()
print(lst)

# 정렬 .sort() / sorted()
# 내림차순
lst.sort(reverse=True)
print(lst)
# 오름차순
lst.sort()
print(lst)

# 찾는 요소가 몇 개인지 갯수 .count()
x=lst.count(5)
print(x)

# 5. 딕셔너리
dict={'name': 'Alice', 'age': 25}
print(dict['name'])

# 6. 튜플
t=(1, 2, 3, 4, 5)
print(t[3])


# 7. 집합
s = set([1, 2, 2, 3, 4, 5])
print(s) # >> 중복 제거 됨.





# <모든타입에 대해서 적용해보기>
# 변환합수 : int.float, str, list, tuple,dict,set,
# 변환내장메서드 : 문자열.split(), "".join(리스트) 

# (1) 숫자(정수, 실수)를 문자, 불, 리스트,튜플, 딕셔너리,집합으로 변환해보기
num = 1234
print("숫자 타입변환 =========")
print("정수로 변환 =>",int(num))
print("실수로 변환 =>",float(num))
print("문자열로 변환 =>",str(num))
print("불로 변환 =>",bool(num))
print("리스트, 튜플, 딕셔너리, 집합으로 변환 불가!")

# 숫자타입: list(), tuple() dict() set() 안된다. => 반복객체가 아니라서
# TypeError: 'int' object is not iterable
# print(list(num))
# print(tuple(num))

# 예제) num = 1234가 있을때, [1,2,3,4]로 만들고 싶다.
num=str(num)
arr=[]
for i in range(len(num)):
    arr.append(num[i])
print(arr)




# (3) 문자열(숫자가 들어가있는경우)를 숫자, 리스트,튜플, 딕셔너리,불, 집합으로 변환해보기
print("문자열(숫자) 타입변환 =========")
text_num = "567"
# (3-1) 정수로 바꾸기
print(int(text_num))

# (3-2) 실수로 바꾸기
print(float(text_num))

# (3-3) 리스트로 바꾸기🔥🔥🔥🔥🔥
print(list(text_num))       # >>> ['5', '6', '7']
print(text_num.split())     # >>> ['567'] 

# (3-4) 튜플로 바꾸기
print(tuple(text_num))

# (3-4) 집합로 바꾸기
print(set(text_num))
#=> 리스트,튜플, 집합은 같은 매커니즘으로 동작한다.


# (4) 문자열(일반 문자)를 숫자, 리스트,튜플, 딕셔너리,불, 집합으로 변환해보기
text= "python javascript"
# (4-3) 리스트로 바꾸기🔥🔥🔥🔥🔥
print(text.split()) # >> ['python', 'javascript']
print(list(text))   # ['p', 'y', 't', 'h', 'o', 'n', ' ', 'j', 'a', 'v', 'a', 's', 'c', 'r', 'i', 'p', 't']

# (5) 리스트를 숫자, 문자열 리스트,튜플, 딕셔너리,불, 집합으로 변환해보기
num_list=['1','2','3','4','5']
# (5-1)num_list 리스트를 숫자타입으로 변경하세요. => 없습니다.
# print(int(num_list), "절대 안돼요.")

# (5-2)num_list 요소를 숫자타입으로 변경하세요. => 리스트타입
print(list(map(int,num_list)))

# (5-3)num_list 리스트의 요소를 합쳐서 12345 숫자로 만들시오.
str1=''
for i in range(len(num_list)):
    str1+=num_list[i]
print(int(str1))


# (5-4)num_list 리스트를 문자열타입으로 변환하시오.

str2=''
for i in range(len(num_list)):
    str2+=num_list[i]
print(str2)

print("".join(num_list))


num = ["1",'2',3,'4',5]
# (5-5)num_list 리스트 요소를 모두 문자열로 변환해주세요.
print(list(map(str,num)))

num_list2 = [1,2,3,4,5]
# (5-6)을 합쳐서 문자열로 표현해주세요 '12345'
# (1)
str2=''
for i in range(len(num_list2)):
    str2+=str(num_list2[i])
print(str2)

# (2)
num_list2=list(map(str,num_list2))
print("".join(num_list2))





