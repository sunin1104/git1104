'''
4. 리스트 []
5. 딕셔너리 {}
6. 튜플 Tuple ()
- 리스트 거의 유사하다.
- 추가 , 수정,삭제 안됩니다.

7. 집합

'''
# ["농심","950원","500kcal","7,500SHU"]

tu=("농심","950","500kcal","7500SHU")
tu2 = ("오뚜기기","900원","500kcal","2,000SHU")
print(tu)

# tu.append("신라면")
# print(tu)
# tu 0번째를 오뚜기로 바꿔보기
# tu[0]="오뚜기"
print(tu+tu2)
print(tu)



# 튜플은 보통 개인적으로 사용할일은 없고, 파이썬에서 처리한 결과 들이 튜플이 나온다.
dict1= {'time':'1014','ip':'89.149.233.0','type':'trade','item':'wiz asset','price':40000,'id':'502yo4'}

key_dic=dict1.keys()
print(key_dic)

value_dic=dict1.values()
print(value_dic)

item_dic=dict1.items()
print(list(item_dic))

[('time', '1014'), ('ip', '89.149.233.0'), ('type', 'trade'), ('item', 'wiz asset'), ('price', 40000), ('id', '502yo4')]

# (1) zip(데이터, 데이터) : 동일한 갯수 두 데이터를 묶어서 하나의 데이터로 만든다.
a = ['a','b','c','d']
b = ['A',"B","c"]
print(list(zip(a,b)))
for v in zip(a,b):
    print(v)


# (2) map(함수이름, 데이터) : 주어진 리스트의 모든 요소 동일함 함수를 적용하고 싶은 경우
num_list =  ['111111','2222','33','4','5']
num_list_2 = []
for i in range(len(num_list)):
    num_list_2.append(int(num_list[i]) )

print(num_list_2)
print(list(map(int,num_list)))


#####################################3
# 리스트 [요소,요소,요소] 
# 튜플 (요소,요소,요소)
# 딕셔너리 {key:value, key:value}
# 집합 {요소,요소,요소}


# 7. 집합 set {} => set([])
# : 서로 다른 데이터 모음 (중복 허용 X)
# list()
# set()
alphabet = ['a','a','a','a','b','b','c','d','e']
print(set(alphabet))

# - 합집합 | , 교집합 &, 차집합 -
# - 부분집합 issubset()
# - 서로소 isdisjoint()




# (과제) 모스부호를 해석하는 딕셔너리 만들기
morse_code = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', '-.-', '.-..', '--', '-.', '---', '.--.', '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..']
alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
morse_list = ['...','---',"..."]

# (과제) 
print('///////////////////')

# // zip 함수로 morse_code와 alphabet 합치기
morse_alp_zip=zip(morse_code,alphabet)

# // zip형태는 tuple이어서 dictionary 형태로 변경
morse_dic=dict(morse_alp_zip)

print(morse_dic)
for m in morse_list:
    print(morse_dic[m])


