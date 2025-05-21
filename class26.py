'''
문자열 "", ''
- 연산자 : +(이어붙이기), *(곱하기)
- 

'''
# 함수 vs 메서드
# 문자열 내장메서드 사용금지 , 리스트 사용금지


# 문제1) text변수에서 letter문자를 제외한 문자열을 출력해주세요.
text = "abcdef"
letter = "f"


# (1) text에 letter있다면 => letter를 빼야합니다.
# (2) 제거
# - 찾아서 letter랑 동일하면 0으로 없애주기

str=''
if letter in text:
    for t in range(len(text)):
        print(text[t])
        # 출력된 값이 letter와 같은지 
        t_str=text[t]
        if t_str != letter:
            str+=t_str
    print(str)


# str1 안에 str2가 있다면 True을 없다면 False를 내보내주세요.
str1="ab6CDE443fgh22iJKlmn1o"
str2="6CD"

# <조건표현식>
# (1) 비교연사자
# (2) 논리연산자
# (3) 포함연산자


print(str2 in str1)


print(1+2)

print(1<=2)

# "안녕하세요" + "혜인님" 붙여서 출력해주세요.
print("안녕하세요"+"혜인님")


# 문제3) 아이스 아메리카노는 한잔에 5,500원입니다. money의 돈으로 구매할수 있는 잔수와 남은 돈을 출력하시오.
money = 4500
money2 = 20000

ice=5500

if money >= ice:
    mm=money//ice
    money%=ice
    print("잔수",mm,"잔돈",money)
else:
    print("돈없음")

if money2 >= ice:
    mm2=money2//ice
    money2 %= ice
    print("잔수",mm2,"잔돈",money2)
else:
    print("돈없음")


# 문제4) my_string에 들어있는 각 문자를 n만큼 반복한 문자열을 출력하시오.
my_string = "hello"
n = 3










