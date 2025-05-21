# https://www.acmicpc.net/problem/10808


s=input()

alpha='abcdefghijklmnopqrstuvwxyz'
# 0이 알파벳의 갯수만큼 준비

lst=[]
for i in range(26):
    lst.append(0)
# print(lst)

for i in range(len(s)):
    # 문제) 내가 입력받은 문자(1개)가 알파벳 순서에서는 몇번째인지를 알고싶다.
    for j in range(len(alpha)):
        # print(j,alpha[j])
        if alpha[j]==s[i]:
            # print(j)
            lst[j]+=1

# 오류: lst안의 요소가 문자열이 아니면 join 불가능합니다.
# (1) map
print(" ".join(map(str,lst)))

# (2) 반복문으로 lst안의 요소를 문자열로 바꾸면 해결완료
for i in range(len(lst)):
    lst[i]=str(lst[i])
print(" ".join(lst))


# (3) join 안쓰기
text = ""
for i in range(len(lst)):
    text += str(lst[i])+" "
print(text.strip())
"1 1 0 0 1 0 0 0 0 1 1 0 0 1 2 0 0 0 0 0 0 0 0 0 0 0 "


