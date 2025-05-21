# 객체지향프로그래밍 (Object-Oriented Programming, OOP)
# 프로그래밍 설계론

# 절차절프로그래밍 = 함수형프로그래밍
# 현실과 비슷하게 프로그래밍 설계를 하자 : 오프라인 -> 온라인


# 객체(Object) : 속성(데이터, 변수)와 메서드(기능, 함수) 동시에 갖는 개념
# - class : 설계, 틀, 레시피
# - instance 인스턴스 : 실물 객체, 제조한 음료


# 사람
# : (데이터)이름, 나이도, 주민등록번호
# : (기능)코딩수업, 프로젝트 합

# 핸드폰
# : (데이터)기종, 생산년도
# : (기능) 전화, 문자,

# 음료
# : 이름, 양 제조날짜, 제질
# : (기능) 마시다.


# hj_name = ""
# hj_age = 00
# hj_phone=


'''
- 클래스이름규칙 : 앞대문자(PascalCase)
class 클래스이름:
    # 생성자(__init__메서드) : 생성할때 실행할 코드
    # '_'(언더스코어)가 맨 앞에 있을때, private : 외부에서 접근하지 못하게할것.
    # self : 메서드 맨앞에 무조건 적는다. (자신의 ~~~~~)
    
    def __init__(self):
        sef.속성이름 = 데이터

'''

# User객체를 만들어보기
# - 속성:  아이디
#        pw
#        이메일
#        핸드폰번호
#- 메서드 : 로그인하기
#         비밀번호 찾기

class User:
    def __init__(self,id,pw,tel,email):
        self.id=id
        self.pw=pw
        self.tel=tel
        self.email=email

    # __str__ : 객체를 비공식적으로 문자열로 출력하게 하는 (사람대상) => print()
    def __str__(self):
        # "회원: id님"
        return f"회원:{self.id}님"

    # __repr__ : 디버깅과 개발할때 시스템적, 공식적 명시하기 위해서 표현하는 
    def __repr__(self):
        # 내용 : "객체이름(속성="데이터",)"
        return f"User(id={self.id},pw={self.pw})"


    # 기능1)로그인하기
    # - 아이디랑 pw를 외부에서 가져오고
    # - 내 아이디랑 내 pw랑 맞으면 "로그인" 안맞으면 "계정을 확인해주세요."출력하는 기능
     
    def login(self,iid,ipw):
        # 없으며 만들고 있으면 덮어쓰기(수정)

        if iid==self.id and ipw==self.pw:
            print("로그인")
        else:
            print("계정을 확인해주세요.")




'''
인스턴스 = 실물객체 
- 클래스명()
- 클래스명(입수,인수,인수)

인스턴스.속성명


get~~~~~(): 가져오는 함수
set~~~~~(): 변경하는, 할당하는 함수
'''
user=User("hyein","1234","010124345678","@@@")
print(user.id)
user2=User("hye2","3456","010987654433","@@")
print(user2.id)
print(user.id, user.pw)

# user를 로그인시켜보기
# 인스턴스명.메서드() : user의 로그인하기
# 문자열.split(): 문자열의 리스트 변환하기


user.login("hyein","1234")
user.login("hyein","12345")
user2.login("hyein","12345")






