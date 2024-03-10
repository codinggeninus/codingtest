import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# A 오름차순 정렬
A.sort()
# B 내림차순 정렬
B.sort(reverse=True)

result = 0
for i in range(N):
    result += A[i]*B[i]

print(result)