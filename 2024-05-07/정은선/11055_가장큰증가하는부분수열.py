import sys
input = sys.stdin.readline

#입력
n = int(input())
A = list(map(int, input().split()))
d = [0] * n #dp 초기화
d[0] = A[0] #첫 번째까지의 합
#2~n번째까지 각각 합계 max 구하기
for i in range(1, n):
    #현재 인덱스까지 모든 수 확인
    for j in range(i):
        #현재 인덱스의 값이 큰 경우 j를 더했을 때와 비교하여 max값 갱신
        if A[j] < A[i]: 
            d[i] = max(d[i], d[j]+A[i])
        #아닌 경우는 j를 더하지 않고 max값 갱신
        else:
            d[i] = max(d[i], A[i])
#출력
print(max(d))