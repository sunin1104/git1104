'''
<데이터타입>
1. 문자열 string ""
- 연산자 : +(이어서붙이기), *(반복)
- len(문자열): 문자열의 길이, 크기, 갯수
- 순서(=인덱스)가 있습니다. 
- 인덱싱 : 변수이름[인덱스]
- 슬라이싱 :  변수이름[시작인덱스: 끝인덱스]
'''

# 예제) "환영함니다" "혜인님" 두 문자열을 붙여서 출력해주세요.
print("환영함니다"+"혜인님다"+" 혜인님")
text = "환영함니다"+"혜인님"

print("----text변수에서 '혜인' 잘라보고싶어요.")
# 예제) text변수에서 "혜인" 잘라보고싶어요.
# 슬라이싱 :  변수이름[시작인덱스: 끝인덱스]

# 슬라이싱
# 시작번호 : 5  / 끝번호: -1
s=text.find("혜인")

print(s)
print(text[s: s+len("혜인")])


# 문자열 -> 리스트
text = "hi python"

# 1.대문자로 변경 문자열.upper() / .lower()
print(text.upper())
# a = 97
# A = 65

# 2. 문자를 찾아서 바꾸기 : 문자열.replace("찾는문자","바꿀문자")
# 예제)text변수에서 "hi" -> "hello"로 바꿔주세요.
print(text.replace("hi","hello"))
# 예제) phone변수에서 "-" 없애기
phone = "010-12345-678"
print(phone.replace("-",""))


# 3. .count("찾는문자") : 문자 갯수 세기
text = "apple apple apple apple apple apple"
print(text.count("apple"))


# 4. ⭐ 문자열.split("구분인자") :  문자열을 구분인자로 쪼개서 리스트로 변환하는 방법 
menu = "아메리카노,카페라떼,밀크티,아이스티"
lst = menu.split(",")
print(lst) # ['아메리카노', '카페라떼', '밀크티', '아이스티']

# 리스트 List (=배열) [요소,요소,요소]
# : 여러가지 데이터(요소, 데이터타입전체)를 저장하나는 데이터타입

# 좋아하는 과일로 리스트 한번 만들어주세요. lst
lst = ["apple","banana","kiei"]



