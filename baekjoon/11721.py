# https://www.acmicpc.net/problem/11721

# 입력으로 주어진 단어를 열 개씩 끊어서 한 줄에 하나씩 출력한다. 
# 단어의 길이가 10의 배수가 아닌 경우에는 마지막 줄에는 10개 미만의 글자만 출력할 수도 있다.

x=input()

y=''

for i in range(len(x)):
    y+=x[i]
    # print(y)
    if len(y)==10:
        print(y)
        y=''
print(y)






