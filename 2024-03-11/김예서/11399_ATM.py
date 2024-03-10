import sys
input = sys.stdin.readline

n = int(input())
p = list(map(int, input().split()))

# 인출 시간을 오름차순으로 정렬
p.sort()

result = 0
sum = 0
for i in p:
    sum += i
    result += sum

print(result)