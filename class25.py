# '''
# 문자열 "", ''
# - 연산자 : +(이어붙이기), *(곱하기)
# - 

# '''
# # 함수 vs 메서드
# # 문자열 내장메서드 사용금지 , 리스트 사용금지


# # 문제1) text변수에서 letter문자를 제외한 문자열을 출력해주세요.
# text = "abcdef"
# letter = "f"


# # (1) text에 letter있다면 => letter를 빼야합니다.
# # (2) 제거
# # - 찾아서 letter랑 동일하면 0으로 없애주기

# str=''
# if letter in text:
#     for t in range(len(text)):
#         print(text[t])
#         # 출력된 값이 letter와 같은지 
#         t_str=text[t]
#         if t_str != letter:
#             str+=t_str
#     print(str)


# # str1 안에 str2가 있다면 True을 없다면 False를 내보내주세요.
# str1="ab6CDE443fgh22iJKlmn1o"
# str2="6CD"

# # <조건표현식>
# # (1) 비교연사자
# # (2) 논리연산자
# # (3) 포함연산자


# print(str2 in str1)


# print(1+2)

# print(1<=2)

# # "안녕하세요" + "혜인님" 붙여서 출력해주세요.
# print("안녕하세요"+"혜인님")


# # 문제3) 아이스 아메리카노는 한잔에 5,500원입니다. money의 돈으로 구매할수 있는 잔수와 남은 돈을 출력하시오.
# money = 4500
# money2 = 20000

# ice=5500

# if money >= ice:
#     mm=money//ice
#     money%=ice
#     print("잔수",mm,"잔돈",money)
# else:
#     print("돈없음")

# if money2 >= ice:
#     mm2=money2//ice
#     money2 %= ice
#     print("잔수",mm2,"잔돈",money2)
# else:
#     print("돈없음")


# # 문제4) my_string에 들어있는 각 문자를 n만큼 반복한 문자열을 출력하시오.
# my_string = "hello"
# n = 3



print("문제1) input()으로 올해 년도를 입력받아 내년도 출력하기")
# 입력예제) 2025
x=int(input())
print(x+1)


print("\n문제2) 정수(integer), 실수, 문자(character), 문자열(string) 등 1개만 입력받아 한 줄로 공백을 두고 3번 출력해보자.")
# 입력예제) computer science
# 결과예제) computer science computer science computer science
n=input()

print((n+" ")*3)


print("\n문제 3) input()으로 시:분:초 형식으로 입력받아 분만 출력하기")
# 입력예제) 17:23:57

time=input().split(':')
print(time[1])


print("\n문제4) input()으로 한줄에 시와 분을 받아 1시간 뒤의 시간을 시:분 으로 출력하기")
# 입력예제) 23 59

s,m=map(int,input().split())

s=(s+1)%24

print(s,":",m)


print("\n문제5) 주민등록번호를 입력받는다. '-'를 제외한 주민번호 13자리를 모두 붙여 출력한다.")
# 입력예제) 110011-0000000 

num=input().replace('-','')
# print(num)

if len(num)!=13:
    print('민증번호가 잘못됨')
else:
    print(num)


print("\n문제6) '연도.월.일'을 입력받아 '일-월-연도' 순서로 바꿔 출력해보자.")
# 입력예제 ) 2020.3.4

day=input().split('.')

# print(day)

if len(day) != 3:
    print('X')
else:
    y=day[0]
    m=day[1]
    d=day[2]

    print(d,"-",m,"-",y)


print("\n문제7) 알파벳과 숫자로 이루어진 2개의 단어가 공백으로 구분되어 입력될때, 순서대루 붙여 출력해보자")
# 입력예제 ) hello world

char_num=input().replace(' ','')
print(char_num)


print("\n문제8) 정수 2개를 입력받아 합을 출력해보자")
# 입력예제) 123 -123

num=input().split()

if len(num)!=2:
    print("정수 2개 아님")
else:
    x=int(num[0])
    y=int(num[1])
    print(x+y)


print("\n문제 9) 두 정수(a, b)를 입력받아 a가 b보다 작으면 True 를, a가 b보다 크거나 같으면 False 를 출력하는 프로그램을 작성해보자.")
# 입력예제) 1 9

a,b=map(int,input().split())

if a<b:
    print('True')
else:
    print('False')


print("\n문제 10) 정수값이 입력될 때, 그 불 값을 반대로 출력하는 프로그램을 작성해보자.")
# 입력에제) 1

n=int(input())

if n:
    print('False')
else:
    print('True')


