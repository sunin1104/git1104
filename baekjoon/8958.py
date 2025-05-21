# OX퀴즈 https://www.acmicpc.net/problem/8958
# "OOXXOXXOOO"의 점수는 1+2+0+0+1+0+0+1+2+3 = 10점이다.


# 첫째 줄에 테스트 케이스의 개수가 주어진다. 각 테스트 케이스는 한 줄로 이루어져 있고, 
# 길이가 0보다 크고 80보다 작은 문자열이 주어진다. 문자열은 O와 X만으로 이루어져 있다.


# <동적입력>
# 첫째 줄에 테스트 케이스의 x개수가 주어진다. 
# 9 -> 1 9
x=input()
x=int(x)
for i in range(x):
    # 독립적으로 처리할 예정 -x-x-x-x-x-x-x-x-x-x-x-x-x-x-
    total=0  #>>> 총점
    y=input() #>>> "OOXXOXXOOO"
    # print(y)
    # 무조건 1점이 아니라
    # O가 나온 갯수만큼 해닫 문제의 배점이 늘어가는 형식

    score=0

    # 문자열도 반복문 가능하다. - 반복문 사용해서하나씩 출력해보자.
    for j in range(len(y)):
        # print(y[j])
        if y[j]=='O':
            # 총점에는 문제당 배점을 추가하기
            score+=1
            total+=score
            # print('맞음',score)
        else:
            score=0
            # print('틀림')
    print(total)



# a=int(input())
# b_arr=[]
# b_num=0
# for i in range(a):
#     b=input()
# # print(b)
    
#     b_arr.append(len(b))
#     if b_arr[i]=='O':
#         b_num+= 1


# print(b_arr)