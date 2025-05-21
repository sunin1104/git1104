'''
<출력과 입력> 
(1) print(내용) : 콘솔에 한줄씩 출력하기
(2) input()    : 키보드로 한줄씩 입력받기
 변수 = input() # 키보드로 입력한 값을 왼쪽의 변수에 저장한다.
  - input()으로 입력받은 데이터는 항상 String 이다.
✅ 입력받은 데이터는 무조건 체크할것

<데이터타입 - 1. 숫자 Number>
: 숫자 형태로 이루어진 데이터타입

(1) 종류
- 정수형 int() : 데이터를 정수형으로 변환
- 소수형 float() : 데이터를 소수형으로 변환

(2) 연산자 : +,-,*,/(사칙연산), **(제곱), //(몫), %(나머지)

(3) 대입연산자 : +=, -=, *=, /=, //=, %=, **=
: 연산과 변수할당을 동시에


<데이터타입 - 2. 문자열 String>
: "", ''안에 문자와 단어 등으로 구성된 연속된 문자들로 이루어진 데이터타입
: 0~9, a~z, A~Z, !, @, #, {, [, <, ..., 띄어쓰기 등 '' 안에 있으면 문자열이다.

(1) 연산자 : +(이어붙이기), *(반복) , in(포함)

(2) len(데이터) : 문자열 길이 구하는 함수

(3) 문자열 인덱스
: 문자열은 여러개의 문자들로 이루어져 있어서 각 문자마다 순서(인덱스)가 존재한다.
: 순서를 인덱스(Index)라고 하며, 인덱스는 기본적으로 0부터 시작(역방향으로는 -1부터 시작)
- (3-1) 인덱싱 : 인덱스(Index)를 활용하여 문자를 추출하는 것
    문자열[index]
- (3-2) 슬라이싱 : 문자열의 범위를 지정하여 일부분을 추출하는 것
    문자열[start:end:step]      
    #(start: 시작인덱스 / end: 끝 인덱스 / (옵션)step: 슬라이싱 간격)

(4) str(데이터) : 데이터를 문자열로 변환하는 함수
  - 보통 숫자를 문자열로 변환

(5) .split(구분인자) : 문자열 쪼개기, 문자열 => 리스트 변환
문자열.split(separator, maxcnt)
- 문자열을 이용하여 구분인자(separator)을 기준으로 문자열을 분리시킨 후 리스트로 반환
- maxcnt는 최대로 나눌수 있는 횟수, 없으면 전체 나누기


'''

'''
<제어문>

반복문
1. for문  - 횟수반복

for 반복변수 in 반복조건(반복가능한 개체 iterable객체):
* iterable한 타입 : list, dict, set, str, bytes, tuple, range

(1) for i in range(횟수):
    # 횟수만큼 반복

(2) for i in range(len(리스트)): 
    # 리스트의 길이만큼 반복

(3) for i in 리스트: 




2. while문 - 조건반복


3. break문, continue문, pass


'''



number = [1,2,3,10,11,12,14]

#(1) range(숫자) : 0~숫자-1까지의 연속된 정수 반복
for i in range(len(number)):
    # 리스트의 갯수만큼 반복
    print("인덱스:",i,"/ 요소값:",number[i])


#(2) number 객체로 반복돌리기
for n in number:
    # 리스트로 반복
    print("요소값:",n)


#(3) enumerate(리스트)
print(list(enumerate(number)))
for i, v in enumerate(number):
    print("인덱스:",i,"/ 요소값:", v)




dictionary = {'key1':'value1', 'key2':'value2','key3':'value3','key4':'value4'}
for k in dictionary:
    print("키:",k,"/ 밸류값:", dictionary[k])

print(dictionary.items())
for k, v in dictionary.items():
    print("키:",k,"/ 밸류값:", v)


dictionary = {'key1':'value1', 'key2':'value2','key3':'value3','key4':'value4'}

# <조건문>  => 전체가 나오는게 아닌상황이면, 무조건 조건문 문제
# 1. if 조건==>True : ~ elif 조건: ~ else:

# <조견표현식 => True/False>
# (1) 비교연산자 == != > < >= <=
# (2) 논리연산자 조건 and 조건 조건 or 조건  not(!)
# (3) 포함연산자 in, not in
# (4) None, False, 0, "",[]를 제외한 숫자, 문자, 여러가지 데이터타입은 => True 체크한다.


# 2. 삼항연산자 :
# - 이항연산자: 숫자1+숫자2, -, *, /
# - 일항연산자 : not
# - 삼항연산자 : B ? A : C  => True if 조건 else False
a = 1+2 
a = "1일이크네" if 1>2 else "이게 정답"





# 문자열로 바꿔주세요.
lst = [1]
print(str(lst))


# text변수에 h가 포함되어 잇는가? 있으면 yes 아니면 no
text = "hello"
print('h' in text)


if 'h' in text:
    print('yes')
else:
    print('no')


# text변수의 모든 문자를 각각 출력해주세요.
for i in range(len(text)):
    print(text[i])





