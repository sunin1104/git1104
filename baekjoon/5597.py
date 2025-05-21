# 과제 안내신분..?) https://www.acmicpc.net/problem/5597

# 입력) 
# 입력은 총 28줄로 각 제출자(학생)의 출석번호 n(1 ≤ n ≤ 30)가 한 줄에 하나씩 주어진다. 출






# 과제 1~30번 리스트 만듭니다. 
# - 연속된 정수범위 range(시작,끝+1)
# -list(range(시작,끝+1)
# list_r 미제출명단
list_r=list(range(1,31))

# (1) 입력을 총 28개 입력받고 리스트 저장
arr=[]
for i in range(28):
    num=int(input())
    arr.append(num)
arr=sorted(arr)


# 앞데이터와 뒤 데이터를 비교했을때 차이가 1나지 않는 숫자를 찾기
# 관리자 로그인 admin / 1234* => 예상결과 : 로그인
# (1)결과확인 => 예상결과랑 다르게 나오면 => 오답임을 인지로그인안된답니다.
# (2) 오답이 나오는 경우 생각해서 필요한 데이터이 실제로 어떻게 들어가고 나오는지를 체크

for i in range(len(arr)):
    # 제출한 사람은 미제출명단(list_r)에서 삭제 하기
    # print("과제를 제출한사람",arr[i])
    num = arr[i]
    # 리스트 요소 삭제 => 리스트.remove(찾는 값)
    # list_r[num-1] = "*"
    list_r.remove(num)


for i in range(len(list_r)):
    print(list_r[i])








#     # 현재데이터, 다음데이터 
#     now=arr[i]
#     next=arr[i+1]
#     print(now,next)
    
#     if now+1!=next:
#         # (1) 변수에 내가 예상하는 결과가 들어가 있는가
#         print(now,next)
#         # (2) 사이값 출력 1 4 => 오답 => 로직바꿔
#         n=[]


# # print(num2)

# arr2=[]

# for i in range(1,len(arr)-1):
#     today=arr[i]
#     future=arr[i+1]
#     if today+1!=future:
#         arr2.append(today+1)

# print(arr2)

# # ///////10,11,12 이렇게 뺴먹으면 11,12를 인식을 못함

