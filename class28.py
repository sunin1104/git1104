'''
(4)


'''

# 문자열=> 리스트
dessert="케이크,마카롱,크로와상"

x=dessert.split(',')
print(x)

text ="abcd"

arr=[]
for i in range(len(text)):
    x=text[i]
    arr.append(x)
print(arr)


print(list(text))



# 한줄에 입력이 5개 정수가 들어온다. 세수의 합(sum)을 구하자.
# sum(데이터)

# map함수(함수이름,리스트(iterable객체)) :리스트의 모든 요소에 함수를 적용하고싶을때 
# 변수 다중 할당 :
# a,b,c =map(int,input().split())

# x=sum(a)
# print(x)


# month에 "월"을 추가해서 리스트로 만들어주세요.
month = [1,2,3,4,5,6,7,8,9,10,11,12]

arr=[]
for i in range(len(month)):
    z=str(month[i])+'월'
    arr.append(z)
print(arr)


# 함수
# : 숫자를 함수에 입력(매개변수)받고, 
# 그 숫자 문자열로 변경후에
# 
# "월"을 붙여서 
# 결과로 반환 함수

def inputm(n):
    n=str(n)
    z=n+'월'
    return z
print(inputm(1))
# 리스트의 모든 요소에 inputm을 적용하고싶다. 
# => list(map(함수이름, 리스트))
month = [1,2,3,4,5,6,7,8,9,10,11,12]

print(list(map(inputm,month)))

# 요소 각각의 글자수를 구해주세요.
strint = ["아메리카노","밀크티","아이스티","아포카토"]

for i in range(len(strint)):
    print(len(strint[i]))

print(list(map(len,strint)))



names = ["alice", "bob", "charlie"]
# 모두 대문자로 바꿔주세요. => 문자열변수.upper()
# => map


# for i in range(len(n)):
#     x=n[i].upper()
#     print(x)
        
def upp(n):
    x=n.upper()
    return x

print(list(map(upp,names)))
print(list(map(str.upper,names)))
print(list(map(lambda x: x.upper(),names)))


print("모든 숫자에 제곱하기")
nums = [1, 2, 3, 4, 5]

def dou(n):
    n=n**2
    return n

print(list(map(dou,nums)))

print(list(map(lambda n: n**2, nums)))























print("\n 문제11) 정수 2개(a, b) 를 입력받아 a를 b로 나눈 몫과 나머지를 출력해보자.")
# 입력예제) 10 3

print("\n 문제12) 실수 1개를 입력받아 소숫점 이하 두 번째 자리까지의 정확도로 반올림한 값을 출력해보자.")
# 입력에제) 3.141592

print("\n 문제13) 정수 3개를 입력받아 합과 평균을 출력해보자.")
# 입력예제) 1 2 3

print("\n 문제14) 3개의 정수(a, b, c)가 입력되었을 때, 짝(even)/홀(odd)을 출력해보자.")
# 입력예제)  1 2 8

print("\n 문제15) 0이 아니면 입력된 정수를 출력하고, 0이 입력되면 출력을 중단해보자.")


print("\n 문제16) 1, 2, 3 ... 을 계속 더해 나갈 때, 그 합이 입력한 정수(0 ~ 1000)보다 같거나 작을 때까지만 계속 더하는 프로그램을 작성해보자.")
# 입력예제) 55
# 예상출력) 10

print("\n 문제17) 정수를 입력받고 1부터 입력한 정수까지 3,6,9 게임을 진행해보자.")
# 만약 3, 6, 9 가 들어간 수를 자신이 불러야 하는 상황이라면, 수를 부르는 대신 "박수(X)" 를 쳐야 한다.
# 33과 같이 3,6,9가 두 번 들어간 수 일때, "짝짝"과 같이 박수를 두 번 치는 형태도 있다
# 입력예시) 9
# 예상결과) 1 2 X 4 5 X 7 8 X

print("\n 문제18) 정수를 입력받고,  1부터 입력한 정수까지 1씩 증가시켜 출력하는 프로그램을 작성하되, 3의 배수인 경우는 출력하지 않도록 만들어보자.")
# 입력예제) 10
# 예상출력) 1 2 4 5 7 8 10


print("\n 문제19) 문자열을 입력받고 모음(a, e, i, o, u )을 제거한 문자열을 만들어주세요.")
# 입력예제) "nice to meet you"
# 예상출력) "nc t mt y"