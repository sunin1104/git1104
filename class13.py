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
    - 문자열 메서드 : .replace("찾는문자","바꿀문자"), isalpha(), isdigit(), .count('찾는문자'), .find(str), .strip()
     (.함수() ~의)
    - 문자열 뒤집기 : 문자열변수[::-1]

3. Bool 타입 : True/False
- False : 0 / True : 0빼고다
- bool()
    

4. 리스트, 배열(List) [요소,요소,요소]
: 여러개의 데이터(모든데이터타입 다 가능)를 저장하는 데이터타입

- ⭐len(데이터) : 리스트 길이, 리스트 요소의 갯수 구하는 함수
- ⭐순서(=인덱스,0번부터 시작) 
    => ⭐변수[인덱스]  : 인덱싱(인덱스를 사용해서 값 뽑기)
    => 변수[start:end:step] : 슬라이싱(인덱스를 사용해서 구간 자르기)

- 데이터의 추가(.append()),수정(=),삭제(.pop(인덱스), .remove(요소))
- 리스트의 메서드 : 
    (1) sorted(데이터) / 리스트.sort()
        - 옵션 reverse=True 추가하면 내림차순 정렬이 가능합니다.
    (2) reversed(데이터) : 리스트를 있는 그대로 뒤집기
    (3) .count("찾는문자") : 찾는 요소가 몇개인지


5. 딕셔너리 Dictionary {key:value} => DB
    - key-value쌍으로 갖는다.
    - key(=인덱스와 유사, "문자열",숫자) : 데이터의 값을 뽑을 때 Key뽑기
    - value : 모든 데이터타입
    - 데이터 접근 : 데이터 뽑기
        - 딕셔너리변수[key] : 항목 (key) 고정되는 경우 <- 은행, 회원가입정보
        - 딕셔너리변수.get(key)
    - 데이터 추가,수정(=),삭제(.pop(key))
    - 딕셔너리.keys() : 키들만 모아서 리스트 바꿔주기
    - 딕셔너리.values() : value 들만 모아서 리스트 바꿔주기
    - 딕셔너리.items() : key-value 묶어서 리스트로 바꿔주기
    
6. 튜플 Tuple ()
'''

# 편의점 과자 딕셔너리 5개
# key : 과자 이름 value: 가격을 넣어보기 
# 
dic={"고래밥":1200,"새우깡":1500,"칸쵸":1000,"홈런볼":1100,"포카칩":1400}
# 고래밥의 가격을 한번 출력해주세요.
# 고래바을 2개 구매했을때 가격을 출력해주세요.
print(dic["고래밥"]*2)

# "스윙칩"의 가격을 출력해주세요.
# print(dic["스윙칩"])
print(dic.get("스윙칩"))


# 스윙칩이 없으면, dic 스윙칩을 2100 추가하기

dic["스윙칩"]=2100
# dic.get("스윙칩")=2100 #안됨.
print(dic)

dic["새우깡"]=1800
print(dic["새우깡"])

print(dic.pop("칸쵸"))
print(dic)

# 과자 목록(=리스트)을 보고싶어요.
print(list(dic.keys()))
# 과자 1개씩 구매했을때, 총 합계를 구하고 싶다.
# => value


print(list(dic.values()))

num_dic=list(dic.values())
sum(num_dic)
print(sum(num_dic))

print(dic.items())


'''
# <반복문>
(1) range() : 인덱스를 활용
for i in range(횟수):
for i in range(len(리스트)):

(2) 리스트를 반복 돌리기
for 반복변수 in 반복조건 :


(3) 딕셔너리에 대한 반복
for 반복변수 in 딕셔너리 :
'''

# for value in 리스트 : 

lst = ['돼지','토끼','돼지','양','염소','돼지','돼지','돼지']

for value in lst:
    print(value)

# (3) 딕셔너리에 대한 반복
for k, v in dic.items():
    print(k, v)


# <권한 - 삭제(비활성화)>
# set~~~~~() : 수정, 설정권한
# get~~~~~() : 읽기 권한





# <오답이랑 Error>
# 1. 오답 : 답이 나왔는데 나온 답이 틀린것   컴퓨터기준 : 성공 / 사람 : 실패
# - 풀이(로직- 조건문 반복문)

# 2. Error(오류) : 답이 못나온것         컴퓨터기준 : 실패 / 사람 : 실패
# - 문법 Error 컴퓨터가 못알아듣는것 (데이터타입이 뭔가 이상한 경우)




print("========================================")
# 과제1) 신라면에 대한 정보를 담은 딕셔너리를 만들어보세요.
#  브랜드, 가격, 칼로리, 스코빌 지수

# (1) 
sin_data={"브랜드":"농심","가격":"950원","칼로리":"500kcal","스코빌 지수":"7,500SHU"}

# (2) 
sin_ramen={"신라면":["농심","950원","500kcal","7,500SHU"]}


# 과제2) 여러가지 라면에 대해서 아래 항목이 있는 데이터로 만들어보세요.
# 라면의 종류는 3개이상 신라면, 진라면, 틈새라면
# #  브랜드, 가격, 칼로리, 매운정도

# (2-1)
ramen = [
    {"브랜드":"농심","가격":"950원","칼로리":"500kcal","스코빌 지수":"7,500SHU"},
    {"브랜드":"오뚜기","가격":"900원","칼로리":"500kcal","스코빌 지수":"2,000SHU"},
    {"브랜드":"팔도도","가격":"1500원","칼로리":"500kcal","스코빌 지수":"9,413SHU"}
]
# sin_data={"브랜드":"농심","가격":"950원","칼로리":"500kcal","스코빌 지수":"7,500SHU"}
# jin_data={"브랜드":"오뚜기","가격":"900원","칼로리":"500kcal","스코빌 지수":"2,000SHU"}
# tightspace_data={"브랜드":"팔도도","가격":"1500원","칼로리":"500kcal","스코빌 지수":"9,413SHU"}


# (2-2)
sin_ramen={"신라면":["농심","950원","500kcal","7,500SHU"]}
jin_ramen={"신라면":["오뚜기기","900원","500kcal","2,000SHU"]}
tightspace_ramen={"신라면":["팔도도","1500원","500kcal","9,413SHU"]}


# 과제3) 아이스크림 가격과 객수가 적혀진 딕셔너리입니다.
icecream2 = {"미니 메로나":[1200,2],
             "탱크보이":[1800,3],
          "빠삐코": [800,12],
             "요맘때":[1500,10]}
# (1) 미니 메로나 가격을 출력해라

merona=icecream2["미니 메로나"]

print(merona[0])

# (2) 탱크보이의 구매한 갯수를 출력해라

tankboy=icecream2['탱크보이']

print(tankboy[1], icecream2['탱크보이'][1])

# (3) 빠비코의 총 구매 가격을 출력해라
bbabbico1=icecream2['빠삐코'][0]
bbabbico2=icecream2['빠삐코'][1]

int(bbabbico1),int(bbabbico2)

bbabbico=bbabbico2*bbabbico1
print(bbabbico)


# (4) 모든 아이스크림의 총 구매 가격을 출력해라

tot=0
for v in icecream2.values():
    # print(v[0])
    # // 가격 수량 곱하기
    tot+=v[0]*v[1]
print(tot)


# 과제4) 여기서 거래종류의 종류가 'trade'인 것만 골라보기
# 증권거래데이터가 주어진다. 
log = [
    {'time':'1014','ip':'89.149.233.0','type':'trade','item':'wiz asset','price':40000,'id':'502yo4'},
{'time':'1016','ip':'89.149.233.1','type':'download','item':'None','price':0,'id':'rtw1517'},
{'time':'1305','ip':'89.149.233.3','type':'trade','item':'star asset','price':10000,'id':'eop00'},
{'time':'1315','ip':'89.149.233.6','type':'trade','item':'q energy','price':10000,'id':'versit808'},
{'time':'1253','ip':'89.149.233.9','type':'trade','item':'ms ent','price':2700,'id':'vsf7'},
{'time':'1400','ip':'89.149.233.12','type':'trade','item':'wiz asset','price':10000,'id':'ge3298'},
{'time':'1253','ip':'89.149.233.10','type':'trade','item':'ms ent','price':2700,'id':'hdus8'},
{'time':'1253','ip':'89.149.233.17','type':'trade','item':'ms ent','price':2700,'id':'tau200'},
{'time':'1508','ip':'89.149.233.20','type':'trade','item':'wiz asset','price':45000,'id':'haha160'},
{'time':'1510','ip':'89.149.233.26','type':'download','item':'None','price':0,'id':'bus328'},
{'time':'1500','ip':'89.149.233.30','type':'trade','item':'wiz asset','price':5000,'id':'son1257'},
{'time':'1144','ip':'89.149.233.20','type':'trade','item':'q energy','price':10000,'id':'fury01'},
{'time':'1400','ip':'89.149.233.32','type':'download','item':'ms ent','price':9000,'id':'bew02'},
{'time':'1400','ip':'89.149.233.39','type':'trade','item':'wiz asset','price':10000,'id':'fightclub'},
{'time':'1122','ip':'89.149.233.42','type':'download','item':'None','price':0,'id':'young0'},
{'time':'1300','ip':'89.149.233.43','type':'trade','item':'q energy','price':10000,'id':'kywu1'},
{'time':'1020','ip':'89.149.233.45','type':'trade','item':'ms ent','price':2700,'id':'wyue1'},
{'time':'1400','ip':'89.149.233.42','type':'download','item':'None','price':0,'id':'terra133'},
{'time':'1300','ip':'89.149.233.55','type':'download','item':'None','price':0,'id':'sdyt2387'},
{'time':'1046','ip':'89.149.233.48','type':'trade','item':'star asset','price':1800,'id':'sdk547'},
{'time':'1000','ip':'89.149.233.52','type':'trade','item':'q energy','price':10000,'id':'jjkw4'},
{'time':'1048','ip':'89.149.233.3','type':'trade','item':'wiz asset','price':5000,'id':'wyre97'},
{'time':'1210','ip':'89.149.233.54','type':'trade','item':'star asset','price':40000,'id':'jaeh3'},
{'time':'1055','ip':'89.149.233.13','type':'trade','item':'ms ent','price':2700,'id':'tool2345'},
{'time':'1353','ip':'89.149.233.48','type':'trade','item':'wiz asset','price':5000,'id':'lala20'},
{'time':'1400','ip':'89.149.233.2','type':'download','item':'None','price':0,'id':'vnv379'}]

# //type 찾기

trade_arr=[]

for t in log:
    # print(t['type'])
    type_dic=t['type']
    
    if type_dic=='trade':
        trade_arr.append(type_dic)

trade_cou=trade_arr.count("trade")
print(f"거래 시스템에서 {trade_cou}개 매매 되었습니다.")


# 과제5) 과제4 결과값에서 여기서 거래 종목 'star asset'인 것만 골라보기

star_arr=[]

for i in log:
    # print(i['item'])
    item_dic=i['item']

    if item_dic=='star asset':
        star_arr.append(item_dic)

star_cou=star_arr.count("star asset")
print(f"star asset이 {star_cou}개 만큼 거래 되었습니다.")


# 과제6) 과제5 결과값에 이어서 거래 금액이 40000원 초과  10000미만 데이터를 골라주세요.

big_price=[]

for p in log:
    p_dic=p['price']

    if p_dic>40000 or p_dic<10000:
        big_price.append(p_dic)

print(big_price)