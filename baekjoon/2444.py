# (과제)
# 별찍기-7 ) https://www.acmicpc.net/problem/2444

inp_num=int(input())

for i in range(1, inp_num+1):
    print(" "*(inp_num-i)+((i*2)-1)*"*")

for i in range(inp_num-1,0,-1):
    print(" "*(inp_num-i)+((i*2)-1)*"*")