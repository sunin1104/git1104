'''
방법론
- 객체지향 프로그래밍
- 함수형 프로그래밍



함수 : 코드 묶음 => 기능
=> 2번이상 재사용성 기능
=> 의미 부여하고 싶은 코드 

<(1) 함수 정의: 함수 만들기>
def 함수이름():
    코드묶음

<(2) 함수 호출 : 함수 사용>
함수이름()

# <(1) 함수 정의: 함수 만들기>
# def 함수이름(매개변수: 변수이름):
#     코드묶음

# 함수이름(인수: 넣는 데이터)


'''
# # 파이썬이 만든함수 내장함수 
# print() 
# len()

# 예제) 환영합니다~ 출력하는 hello() 함수만들기
a= "혜인님"

def hello():
    print("환영합니다~")

hello()

# <(1) 함수 정의: 함수 만들기>
# def 함수이름(매개변수: 변수이름):
#     코드묶음

# 함수이름(인수: 넣는 데이터)


# 예제) 이름을 입력 넣어서 환영합니다~OOO님 출력하는 hello2() 함수만들기



# 함수의 입력 != input()
# print() :  터미널에 출력하기
# input() : 터미널에서 키보드로 입력으 받는 행위

#   \  5(인수)  /
#  -            ------------
# |                         |
# | (매개변수) ㅁ +2 =         |
# |                         |
# -----------------
#                  /   5   \
# name1=input()
name1 = "혜인님"

def hello2(name): # 매개변수 입력을 위한 새로운 변수
    print("환영합니다~"+name)

hello2(name1)

# 예제3) 년도, 월, 일 각각 전달했을때, OOOO년 OO월 OO일 이라고 출력하는 함수를 만들어 보자
year = 2025
month = 3
day = 26

def newymd(y,m,d):
    print(f"{y}년 {m}월 {d}일")

newymd(year,month,day)



'''
- return : 결과값 내보내기 / 함수의 종료
def 함수이름(매개변수):
    코드묶음 => 연산
    return  결과값

함수(인수)

'''

# 1~n까지 출력하고 끝 이라는 결과 내보내는 함수
# 5이상 출력안하기

def num_n(n):
    for i in range(n):
        return 100 if i>5 else -100 #(계산)

print("결과",num_n(10))




# 함수 궁금하신부분 있으시면 언제든지 연락주세요~~!이번에는 기본 연습문제 위주로 드릴거에요!

# 과제1)
# 두팀씩 짝을 지어서 프로젝트 연구를 진행하기로 하였다. 
# 주어진 데이터는 각 프로젝트 참여 명단이다 
# - a_b_project은 a팀과 b팀이 같이 진행한 프로젝트 참여 명단이다.
# - b_d_project은 b팀과 d팀이 같이 진행한 프로젝트 참여 명단이다.
# - c_d_project은 c팀과 d팀이 같이 진행한 프로젝트 참여 명단이다.
# - d_project은 d팀이 진행한 프로젝트 명단이다.
# 각각의 팀 명단을 구해주세요.

a_b_project = ['oak', 'guitar', 'butter', 'clover', 'moon', 'notepad', 'bird', 'pineapple', 'grass','spider','ring', 'sun', 'bear','space']
b_d_project= ['clover', 'moon', 'notepad', 'bird', 'pineapple', 'grass','spider','boat', 'piano', 'seed', 'earth', 'melody', 'granate', 'mushroom', 'vase', 'bee']
c_d_project = ['boat', 'piano', 'seed', 'tumblr', 'popcorn', 'eagle', 'tank', 'cactus', 'fever', 'orange', 'papercup', 'earth', 'melody', 'granate', 'mushroom', 'vase', 'bee']
d_project = ['boat', 'piano', 'seed', 'earth', 'melody', 'granate', 'mushroom', 'vase', 'bee']


# 재사용성
# 일단 막 작성하되, 정답이 나오겠금 
# 나온다음-> 내코드를 보고 -> 이게 최선이까?
# 

# <전체적으로 보니깐>
# 연관 집합 2개 넣고
# 교집합을 구해서 차집합하면 => 결과
def a_project(a_b_pro, b_d_pro):
    b_pro=set(a_b_pro)&set(b_d_pro)
    a_pro=set(a_b_pro)-b_pro
    print("A team=",a_pro)

a_project(a_b_project,b_d_project)

def b_project(b_d_pro, d_pro):
    d=set(b_d_pro)&set(d_pro)
    b_pro=set(b_d_pro)-d
    print("B team=",b_pro)

b_project(b_d_project,d_project)

def c_project(c_d_pro,d_pro):
    d=set(c_d_pro)&set(d_pro)
    c_pro=set(c_d_pro)-d
    print("C team=",c_pro)

c_project(c_d_project,d_project)
print("D team=",d_project)


print("===모범 함수 답안 ======")
# # <전체적으로 보니깐>
# 연관 집합 2개 넣고
# 교집합을 구해서 차집합하면 => 결과


def new_project(x_y_pro, y_z_pro):
    y_pro=set(x_y_pro)&set(y_z_pro)
    x_pro=set(x_y_pro)-y_pro
    return x_pro

a_pro=new_project(a_b_project,b_d_project)
b_pro=new_project(b_d_project,d_project)
c_pro=new_project(c_d_project,d_project)
print("A=",a_pro,b_pro,c_pro)


# 과제2) 가격을 입력받아서 1000원 할인된 금액을 결과로 반환하는 sale_price() 함수를 만들어봐라.
price1 = 1000
price2 = 2400
price3 = 12000

price=int(input('가격을 입력하세요:'))

def sale_price1(pri,coupon):
    tot_sale=pri-coupon
    print(tot_sale)

print(sale_price1(price,1000) + 10000)
sale_price1(price,2400)
sale_price1(price,12000)

# cafe24 => 일로 => 귀찮아요.
# 쇼핑몰에서 장바구니 엄청 복잡 => 쇼핑몰 호스팅 업체 cafe24
# 무료로 쇼핑몰 오픈 => 돈을 결제를 붙여주기, 기능 뚫어준데
# 전체는 못만들어도 한페이지정도 가능하겠느데? 
# https://kmong.com/ 크몽


# 과제3)  리스트를 입력받아 모든 값를 더한 숫자를 결과로 반환하는 sum_num() 함수를 만들어봐라.
num_list1=[1, 3, 2, 10, 12, 11, 15]
num_list2=[1,3,5]

def sum_num(num_lis1,num_lis2):
    num_lis=num_lis1+num_lis2
    tot_sum=sum(num_lis)
    print(tot_sum)

sum_num(num_list1,num_list2)


# 과제4)  핸드폰 번호가 주어졌을때, 숫자만으로 이루어질 수 있도록 변환하는 함수를 만들어주세요.
phone="010-1234-5678"

def disit_phone(tel):
    tel_arr=[]
    if tel.isdigit()==False:
        for i in range(len(tel)):
            tel_num=tel[i]

            if tel_num.isdigit():
                tel_arr.append(tel_num)
    print("phone number:","".join(tel_arr))

disit_phone(phone)



# 과제4-2) 어떠한 형태든 숫자로만 이루어질 수 있도록 해주세요
phone1= "010/1234/5678"
phone2= "010-1234-5678"
phone3= "010.1234.5678"
phone4= "01012345678 "

def only_num(tel):
    if tel.isdigit()==False:
        tel_arr=[]
        for i in range(len(tel)):
            tel_num=tel[i]

            if tel_num.isdigit():
                tel_arr.append(tel_num)
        print("".join(tel_arr))
    else:
        print(tel)

only_num(phone1)
only_num(phone2)
only_num(phone3)
only_num(phone4)

# 과제5) 중복 제거하는 함수를 만들어주세요.
num_list = [1, 2, 2, 3, 4, 4, 5]

def set_numlst(numlst):
    return list(set(numlst))

print(set_numlst(num_list))