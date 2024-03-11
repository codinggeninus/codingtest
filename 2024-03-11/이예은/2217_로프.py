# 그리디, 실버4
# https://www.acmicpc.net/problem/2217

n = int(input())
k_list = [int(input()) for _ in range(n)]
k_list.sort(reverse=True)
result = []

for i in range(n):
    result.append((i+1) * k_list[i])

print(max(result))