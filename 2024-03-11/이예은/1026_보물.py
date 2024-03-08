# 그리디, 실버4
# https://www.acmicpc.net/problem/1026

s = int(input())
a_list = list(map(int, input().split()))
b_list = list(map(int, input().split()))

a_list.sort()

answer = 0

for i in a_list:
    x = max(b_list)
    b_list.pop(b_list.index(x))  # 큰 값을 찾아서 계속 빼주기
    answer += i * x  # a.작은 값 * b.큰 값

print(answer)
