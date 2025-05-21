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
    
'''
print("<문자열 -> 리스트 변환>------------\n")
# (1) .split("구분인자"):  구분인자을 기준으로  문자열을 리스트로 바꾸기 
# (2) list(여러개있는것) :  문자를 하개씩 필요할때
text = "adeafgce"
print(text.split(" "))
print(list("adeafgce"))
text = "010-1234-5678"

print("<bool 타입변환 >------------\n")
num = -1
print(bool(num))
text = "hi"
print(bool(text))
text = ""
print(bool(text))
lst=[]
print(bool(lst))



print("-------------------")
list_a = [1,2, 3,['Life', 'is'],'too']
lst=list_a[3]  # 
lst2 = lst[1].replace("i",'e')
# print((lst[1].replace("i",'e')).upper())  # 금지
print(lst2.upper()) 


print("-------------------")
num_lst = [3, 1, 9, 4, 2, 8]
# 예제1. 오름차순 정렬
print(sorted(num_lst))

# 예제2. 내림차순 정렬
print(sorted(num_lst,reverse=True))

# 뒤집기 reversed(데이터) : 있는 그대로 뒤집기 => reversed객체 <list_reverseiterator>
print(list(reversed(num_lst)))


print(".count(요소) -------------------")
# 찾는것
list = ['돼지','토끼','돼지','양','염소','돼지','돼지','돼지']

print(list.count("돼지"))

# .index("찾는문자") : 찾는문자가 리스트에서 몇번째인지  #  
# 토끼
print(list.index("토끼"))
lst_text=list.index("토끼")
print(list[lst_text])



print("<리스트 -> 문자열로 변환>------------\n")
# (1)"".join(리스트): 리스트를 문자열로 합치기
# (2) str(숫자) : 숫자를 문자열로 바꾸는 용도 


text = ['H','e','l','l','o']
print(str(text))




'''
<데이터타입 변환>
- int() : 실수나 문자열을 정수로 변환
- float() : 정수나 문자열을 실수로 변환
- str() : 숫자를 문자열로 변환
- list() : 튜플, 집합 등을 리스트로 변환

# <문자열에서>
# (1) .split("구분인자"):  구분인자을 기준으로  문자열을 리스트로 바꾸기 
# (2) list(여러개있는것) :  문자를 하개씩 필요할때

# <리스트에서>
# (1)"".join(리스트): 리스트를 문자열로 합치기
# (2)str(숫자) : 숫자를 문자열로 바꾸는 용도 
'''



# 과제 ---------------------------------
print("< 과제1 >------------")
# 문제 1) 정수가 담긴 리스트 num_list가 주어질 때, num_list의 원소 중 짝수와 홀수의 개수를 담은 배열을 출력해보세요.
num_list1 = [1, 2, 3, 4, 5]
num_list2 = [1, 3, 5, 7]

even=[]
odd=[]

for i in range(len(num_list1)):
    if num_list1[i]%2==0:
        even.append(num_list1[i])
    else:
        odd.append(num_list1[i])

# print(even,odd) // num_list1 짝수, 홀수 구분

for i in range(len(num_list2)):
    if num_list2[i]%2==0:
        even.append(num_list2[i])
    else:
        odd.append(num_list2[i])
# print(even,odd) // num_list2 짝수, 홀수 구분

sort_even=sorted(even)
sort_odd=sorted(odd)
# print(sort_even,sort_odd) // 짝수, 홀수 정렬

re_even=[]
re_odd=[]

for i in range(len(sort_even)):
    if sort_even[i] not in re_even:
        re_even.append(sort_even[i])
# // 짝수 중복 제거

for i in range(len(sort_odd)):
    if sort_odd[i] not in re_odd:
        re_odd.append(sort_odd[i])
# // 홀수 중복 제거

print(re_even, re_odd) # //짝수와 홀수의 개수를 담은 배열을 출력



# print("< 과제2 >------------")
# # 문제 2) 문자열 my_string이  my_string에서 중복된 문자를 제거하고 하나의 문자만 남긴 문자열을 출력해보세요
# my_string1= "people"
# my_string2="We are the world"

# list_str1=list(my_string1)
# list_str2=list(my_string2)

# re_str1=[]
# re_str2=[]

# for i in range(len(list_str1)):
#     if list_str1[i] not in re_str1:
#         re_str1.append(list_str1[i])
# # // my_string1 중복 제거

# for i in range(len(list_str2)):
#     if list_str2[i] not in re_str2:
#         re_str2.append(list_str2[i])
# # // my_string2 중복 제거

# # print(re_str1, re_str2) // list() 형태로 중복 제거 출력

# # // 문자열로 출력
# print("".join(re_str1),"".join(re_str2), sep='\n')


# 문제 3) 문자열 my_string이 매개변수로 주어질 때, my_string 안에 있는 숫자만 골라 오름차순 정렬한 리스트를 출력해보세요
my_list1 = "hi12392"
my_list2 = "p2o4i8gj2"
my_list3 = "abcde0"

'''예제 1'''
# my_list1 숫자만 고르기기

arr_num1=[]

str1_dig=my_list1.isdigit()

if str1_dig==False: # // 숫자와 문자열이 섞여 있을 경우
    for i in range(len(my_list1)):
        lst1=my_list1[i]

        if lst1.isdigit()==True:
            arr_num1.append(lst1)
    # print(arr_num1) // 숫자만 골라서 출력

    # 오름차순 == 정렬하기

    print(sorted(arr_num1))

else:
    list(my_list1)
    print(sorted(my_list1))
# // 숫자만 있을 경우


'''''예제 2,3'''''

my_list2 = "p2o4i8gj2"
my_list3 = "abcde0"

# 숫자만 있는지 확인하기

arr_num2=[]
arr_num3=[]

str2_dig=my_list2.isdigit()
str3_dig=my_list3.isdigit()

if str2_dig==False: # // 숫자와 문자열이 섞여 있을 경우
    for i in range(len(my_list2)):
        lst2=my_list2[i]

        if lst2.isdigit()==True:
            arr_num2.append(lst2)
    # print(arr_num2)
    print(sorted(arr_num2)) # //정렬한 값

else:
    list(my_list2)
    print(sorted(my_list2))
# // 숫자만 있을 경우


if str3_dig==False: # // 숫자와 문자열이 섞여 있을 경우
    for i in range(len(my_list3)):
        lst3=my_list3[i]

        if lst3.isdigit()==True:
            arr_num3.append(lst3)
    # print(arr_num3)
    print(sorted(arr_num3)) # //정렬한 값

else:
    list(my_list3)
    print(sorted(my_list3))
# // 숫자만 있을 경우


