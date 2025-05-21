# 최대최소, 함수
# 최소값 
num = [120,10,35,30,7]
# <함수>
# 기능 : 
# - (1) temp 임시변수 만들고 
# - (2) temp랑 리스트 안에있는 값이 비교해서 작은 값을 temp교체하는 방향으로   
#     - (2-1) 리스트의 값을 꺼내보기
#     - (2-2) 꺼낸값이랑 temp 조건 비교
        #     꺼낸값값이  temp 작으면, temp에 꺼낸 값을 저장하기
        #  
    # - (2-3) 최소값 temp 출력하기 
# 입력 : 숫자 리스트
# 결과 : 최소값(숫자탑입)


def min(num_lst):
    min_value=num_lst[0]  # 최소값을 내부에 있는 값으로 처음에는 임시지정
    # 어차피 다 비교한다.
    for i in range(len(num_lst)):
        print(num_lst[i])
        if min_value<num_lst[i]:
            min_value = min_value
        else:
            min_value=num_lst[i]
        print("최소값",min_value)

def max(num_lst):
    min_value=num_lst[0]  # 최소값을 내부에 있는 값으로 처음에는 임시지정
    # 어차피 다 비교한다.
    for i in range(len(num_lst)):
        print(num_lst[i])
        if min_value>num_lst[i]:
            min_value = min_value
        else:
            min_value=num_lst[i]
        print("최대값",min_value)

min(num)
max(num)
  
# <교체 알고리즘> => swap
a=5
b=10
# b=5 a=10 이 들어가고싶다.
temp = a
a=b
b=temp

# 리스트 내부 교체
# 0번값과 맨 뒤값을 교체 하시오.
num_lst = [1,2,3,4,5,6]

temp=num_lst[0]
num_lst[0]= num_lst[-1]
num_lst[-1]=temp

print(num_lst)

###### 좌우를 교체해보세요.



# 좌우 교체
# - 어떻게 교체했으면 좋겠는지 한국어로 작성할것.=> 로직 설계
# 넘버링 베스트
# 안되면 줄글이라도 자세하게
num_row = [0.0, 0.5, 0.1, 0.4, 0.2, 1.0, 1.0, 0.9]
# 예상결과 : [0.9 1.0 1.0 0.2 0.4 0.1 0.5 0.9]
# for i in range(len(num_list2)):
#     print(num_list2[i])
#     num_row=num_list2[i]
#     len()
#     for j in range(len):

# 사담제로 => 제가 질문금지, 서로 질문금지
# 사담 멈춰!


# (과제)
# 알고리즘 과제 

# // 좌우 교체
# 행 안에 들어있는 열을 반으로 쪼갠다.
# >>> ex= [1,2,3,4], [5,6,7,8]
#  1,8 첫번째 요소와 마지막 요소를 바꾸기
#  2,7 두번째 요소와 뒤에서 두번째 마지막 요소 바꾸기
#  이 방법을 리스트 중간까지 교체해주기








