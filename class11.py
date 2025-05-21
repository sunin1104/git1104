# <알고리즘>
# 2480
# 5597


'''
<변수> 
=> 변수이름 잘 정하기
=> 분류_세부적내용_타입


<데이터타입>
1. 숫자 Number
    - 종류 : 정수 int() / 실수,소수 float()             => 심화) 부동소수점의 오류
    - 연산자 : +,-,/,*,%(나머지),//(몫),**(제곱)


2. 문자열 String '', ""
    - 연산자 : +(이어서 붙이기), *(반복해서 이어 붙이기)
    - ⭐ len(데이터) : 문자열 길이, 문자의 갯수 구하는 함수
    - ⭐ 순서(=인덱스,0번부터 시작) 
      => ⭐변수[인덱스]  : 인덱싱(인덱스를 사용해서 값 뽑기)
      => 변수[start:end:step] : 슬라이싱(인덱스를 사용해서 구간 자르기)
    - ⭐.split(구분인자) : 문자열 나누기 → 리스트변환(문자열을 구분인자로 쪼개서 리스트로 만들기)
    - f-string : f''
    - 문자열 메서드 : .replace("찾는문자","바꿀문자"), isalpha(), isdigit()  .count('찾는문자'), .find(str), .strip()
     (.함수() ~의)
    - 문자열 뒤집기 : 문자열변수[::-1]








'''
# 예제1) "안녕하세요"를 다섯번 이어서 붙여주세요.
# 안녕하세요 5번 이어서 출력하기
# 예상결과) "안녕하세요안녕하세요안녕하세요안녕하세요안녕하세요"
x="안녕하세요"
y=x*5
print(y)

y =""
for i in range(len(x)):
    y += x
print(y)     # <= 터미널에서 결과랑 달라요.

# print(, end="") : 뒤쪽에 줄바꿈을 제어할수있습니다.
for i in range(len(x)):
    print(x,end='')

#--------
print("")
f = "banana"
# 예제3) f에 a가 몇개 있을까요?        => .count(str)
f_cnt = f.count("a")
print(f_cnt)

# 예제4) f를 대문자로 바꿔주세요.       => .upper(), .lower()
f_up=f.upper()
print(f_up)

# 예제5) f에서 b를 대문자로 바꿔주세요.
f_re=f.replace("b","B")
print(f_re)

# 예제6) f가 영어로만 이루어져있는가? => .isalpha() 영어만 잇으면 True / 아니면 False
f="banana12"
print(f.isalpha())

text = "adeafgce"
print(text[::-1])



print("=예제6=========")
# 예제6) phone가 숫자로로만 이루어져있는가? => .isdigit() 영어만 잇으면 True / 아니면 False
# 핸드폰번호가 숫자로만 적히을 수있도록 해주세요.
# -> 숫자가 아닌게 잇으면 제거

phone="010-1234-5678"
phone_=phone.isdigit()
phone_str=""

if phone_==False:
    #print(phone_)

    # 
    for i in range(len(phone)):
        #print(phone[i])  # 무조건

        # 예시 : 0

        '''
        str : 문자열
        text : 문장
        word : 단어
        char : 문자1개 c chr
        '''

        # <전체>가아니면 무조건 조건
        # 숫자가 아니면 - print("숫자다")
        # 숫자가 인것만 - print("숫자아님")
        # 하고싶은거 : 숫자만 찾고싶어요.
        phone_char=phone[i]

        if phone_char.isdigit()==True:
            #print("int")
            phone_str+=phone_char
print(phone_str)



print("///// 과제 /////////")
# 연습 예제) 주어진 문자열에서 알파벳문자만 포함된 단어를 찾아서 문자열 만들어주세요.
text = "hello 123 world python! programming 456"

print(len(text))
# 알파벳 찾기
text_alpha=text.isalpha()
text_alpha_list=[]

# <순서정리> : 파이썬 코드를 위에서아래로 왼쪽에서 오른쪽으로
# 1. 전체 확인
if text_alpha==False:
    # 2. 문자열 하나씩 체크
    for i in range(len(text)):
        print(text[i],end='')
        text_char=text[i]
        
        if text_char.isalpha()==True:
            text_alpha_list.append(text_char)
print("")
print("".join(text_alpha_list))


# -----다른 답안 --------
text = text.split() # ()안쓰면 기본적으로 공백 구분할 수 있다.

result = ''
for i in range(len(text)):
    if not text[i].isdigit():
        for j in range(len(text[i])):
            if text[i][j].isalpha():
                result += text[i][j]

print(result)

