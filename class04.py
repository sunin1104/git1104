
'''
<데이터타입>
1. 숫자타입 Number
2. 문자열타입 String ""
- 인덱스(순서, 0번, -1)
- 인덱싱, 슬라이싱
- .replace("찾는문자","바꿀문자")
- .split("구분인자") : 구분인자를 기준으로 문자열을 나눠서 리스트로 만들어주는 함수

3. bool타입 : True / False => 조건문

4. 리스트 List [요소,요소,요소,요소] (=배열)
: 여러가지 데이터(7가지 데이터타입 모두 가능한다) 를 저장하는 데이터타입
- 순서, 인덱스 => 인덱싱, 슬라이싱


(1) 데이터를 추가,수정,삭제
- 추가 : 리스트.append(추가할데이터) 맨뒤에 추가하는 함수
- 수정 : 인덱싱 데이터를 추출 '=' 덮어쓰기 
- 삭제 : .pop() : 맨 뒤의 값을 제거하는 함수
'''
# 달(month) 1~6월까지만 리스트에 저장해주세요.
month= [1,2,3,4,5,6]
month.append(7)
print(month)

# month 2번째값을 8로 변경해주세요.
month[1]=8
print(month)

print(month.pop())
print(month)


############################################
#  프로그래밍 흐름을 제어하는 제어문 
#  반복문(for문, while문) , 조건문
#  - for문 : 횟수기반으로 반복
#  - while문 : 조건기반으로 반복
# 
#  조건문 : 만약에~~~한다면 A하겠어. 아니면 B하겠어.
############################################
'''''
< 조건문 if~elif~else >
if 조건 :
    (라인틀리면 오류)
    # 조건을 만족했을때 하고싶은 코드
elif 두번째조건 :
    # 첫번째조건이 아니면서, 두번째조건을 만족할때 실행할 코드 
else:
   # 조건이 만족하지 않았을때, 작성할 코드


<조건>
1. 비교연산자 : == != > < >= <=
2. 논리연산자 : 조건 and 조건 (=&&) , 조건 or 조건(=||)

'''


age = 19
# 만약에 20살이상이라면 "성인이다."출력하기
# 만약에 17살이상이라면 "고등학생"이다 출력하기 
# 아니라면 미성년자 이다라고 출력하기
# IndentationError: unexpected indent
if age >= 20:
    print("20살 이상이다.")
elif age >= 17: 
    print("고등학생이다.")
else :
    print("미성년자이다.")  


# 조건 적을때 tip
# age가 20미만 17이상  
# age<20 && age>=17
print(20>age>=17)


'''
반복문for문
: 횟수반복할때 사용하게 될예정입니다.

for 반복변수 in 반복조건:
    # 반복조건이 반복하면서 나오는 데이터를 반복변수에 저장하면서 반복



(1) 기본 형태
for i in range(횟수):
    #반복할 코드

- range(s,e,step) : s~(e-1)까지 step간격의 연속된 자연수를 내보낸다.
'''

# "안녕하세요" 10번정도 반복해서 출력하기

for i in range(10):
    print(i)
    print("안녕하세요")

# range(n) : 0~(n-1) 연속된 자연수를 내보낸다.
# range(0, 10)
print(list(range(10)))



# 0~9까지의 숫자를 출력해보기 (10번)
# 1~10까지 숫자를 출력해주세요.(10번)
# 0,2,4,6,8 두칸씩 건너뛰면서 출력해주세요. 
for i in range(10):
    print(i+1)


# range(시작,끝,스탭)

# 20~99까지의 숫자를 두칸씩 띄워서 출력해주세요. 출력해주세요.
for i in range(20,99,2):
    print(i)

print("====")
# 반복문과 조건을 같이 쓸겁니다.
# 1~30까지의 숫자중에서 /  10이상인 숫자만 출력해주세요.
for i in range(30):
    # print(i+1)
    if i+1>=10:
        # 숫자 출력하기
        print(i+1)



month= ["1월","2월","3월","4월","5월","6월"]

print(month[0])
print(month[1])
print(month[2])
print(month[3])
print(month[4])
print(month[5])

# 리스트의 모든 값을 추출할때 반복문을 사용하기
# 6번 = month의 길이 만큼 len(데이터)
for i in range(len(month)):
    print(month[i])



# 과제1) 반복문을 사용해서 'Hi" 3번출력하기
# 과제2) 1~30까지 숫자를 프린트해주세요.
# 과제3) 0~50까지 숫자중에서 30이상인 숫자만 출력해주세요.
# 과제4) 1~10까지 숫자중에서 짝수인 숫자만 출력해주세요. => 조건문 사용하기

# 과제5) 저녁메뉴를 리스트로 5개이상으로 만들어주세요.
# 과제6) 저녁메뉴에 "족발"을 추가해주세요.
# 과제7) 저녁메뉴에서 3번째값을 "피자"로 바꿔주세요.
# 과제8) 저녁메뉴 마지막 값을 삭제헤주세요.
# 과제9) 저녁메뉴를 전부 출력해주세요.

# 2025.02.10 과제
# 과제1
for i in range(3):
    print("Hi")

# 과제2
for i in range(30):
    print(i+1) 

print("@@@@@@@@@@")
# 과제3
for i in range(51):
    if i>=30:
        print(i)

# 과제4
for i in range(10):
    if (i+1)%2==0:
        print(i+1)
    
# 과제5
dinnermenu=["포케","브리또","카레","라면","치킨"]
print(dinnermenu)   

# 과제6
dinnermenu.append("족발")
print(dinnermenu)

# 과제7 3번쨰 값 카레를 피자로 수정
dinnermenu[2]="피자"
print(dinnermenu)

# 과제8
dinnermenu.pop()
print(dinnermenu)

# 과제9
for i in range(len(dinnermenu)):
    print(dinnermenu[i])