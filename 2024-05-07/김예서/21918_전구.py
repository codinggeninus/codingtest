import sys
input = sys.stdin.readline

# 전구의 개수, 입력되는 명령어의 개수
n, m = map(int, input().split())
# 현재 전구의 상태 (0 켜짐 1 꺼짐)
light = list(map(int, input().split()))

for _ in range(m):
    a, b, c = map(int, input().split())
    
    if a == 1:
        # light의 b번째 상태를 c로 변경
        light[b-1] = c 
    # a가 2일 경우 l번째부터 r번째까지의 전구의 상태를 변경(켜져있는 전구는 끄고, 꺼져있는 전구는 킨다.)
    elif a == 2:
        for i in range(b-1, c):
            light[i] =  1 - light[i]
    elif a == 3:
        for i in range(b-1, c):
            light[i] = 0
    elif a == 4:
          for i in range(b-1, c):
            light[i] = 1

for i in range(n):
    print(light[i], end=' ')