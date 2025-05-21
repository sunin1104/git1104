# 나머지) https://www.acmicpc.net/problem/3052

'''
(문제)
수 10개를 입력받은 뒤, 이를 42로 나눈 나머지를 구한다. 
그 다음 서로 다른 값이 몇 개 있는지 출력하는 프로그램을 작성하시오.

'''




b=42
# 입력리스트 arr1 
arr1=[]
arr2=[]

# 10번 반복하기
for i in range(10):
    # a : 입력받은 값 (숫자) - 숫자는 인덱스 X
    num=int(input())
    divi=num%b
    arr1.append(divi)
# print(arr1)

# 중복제거 알고리즘
for i in range(len(arr1)):
    if arr1[i] not in arr2:
        arr2.append(arr1[i])
print(len(arr2))


# len() : 길이, 리스트 갯수
# 리스트.count("찾는문자") : 그문자가 리스트 안에 몇개가 있는지





