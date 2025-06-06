# 클린코드

# 1. 변수명 :
# (1) 의미가 있는 변수명을 작성해주기
# (2) 범위가 너무 넓으면 고생 - 세부정보를 넣어서 좁혀주기

# 선생님 스타일
# 용도_분류_타입


# 아무거나 적었을경우, 무슨값이 몰라요. print()
month_ = "11월"  # 12월
day_num = 12  # 12일




# ⭐ 반드시 외워야할것 ⭐
# 1. len(데이터) : 데이터의 길이, 갯수
# 2. 인덱스 : 순서
#     => 사용가능한 데이터타입 : 문자열, 리스트, 튜플
#     => 인덱싱, 슬라이싱
# 3. .split('구분인자') : '구분인자'를 기준으로 문자열을 쪼개서 리스트로 만들어주는 함수
# 4. "구분인자".join(리스트) : 리스트의 요소를 '구분인자'로 함쳐서 문자열로 만드는 함수
# - 보통 "구분인자"를 안쓰고 "".join(리스트)


# 💫자동으로 외워지는것💫
# - int() : 단일데이터(float, 문자열)를 정수타입
# - str() : 단일데이터(숫자) 문자열로 바꿔주는 함수
# - list() : 다중데이터(딕셔너리, 튜플, 집합) 리스트로 변경 할때 사용하는 함수