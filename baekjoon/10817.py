# https://www.acmicpc.net/problem/10817

a,b,c=map(int, input().split())

abc_lst=[a,b,c]

abc_sort=sorted(abc_lst)

print(abc_sort[1])
