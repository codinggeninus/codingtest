import sys
input = sys.stdin.readline

n = int(input())
rope = []
# 로프의 정보 차례대로 입력 받기
for i in range(n):
    rope.append(int(input()))

# 로프를 중량이 큰 것부터 내림차순 정렬
rope.sort(reverse=True)

# n번 반복하여 최대 중량 계산
result = []
for i in range(n):
    result.append((i+1) * rope[i]) # 현재 중량 계산

# 계산된 중량 중 가장 큰 값 출력
print(max(result))