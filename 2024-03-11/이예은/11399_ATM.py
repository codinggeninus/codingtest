# 그리디, 실버4
# https://www.acmicpc.net/problem/11399

s = int(input())
time_list = list(map(int, input().split()))
answer = [0] * (s+1)

time_list.sort()
answer[0] = time_list[0]

for i in range(1, s):
    answer[i] = answer[i-1] + time_list[i]

print(sum(answer))
