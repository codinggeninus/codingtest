"""
17393. 다이나믹 룰러

멩미가 i 번째 타일 위에 서 있을 때, 다음 조건에 만족하는 칸을 칠할 수 있다.

1. 현재 위치 보다 오른쪽
2. 점도 지수(Bi) <= 현재 위치의 잉크 지수(Ai)

[아이디어]
주어진 N의 최대 범위는 5 × 10^5, 시간 제한은 2초이므로, O(NlogN) 이하로 풀어야 한다.

현재 위치에서 위 조건에 만족하는 값의 개수를 구하려면 이분 탐색의 상한 탐색을 수행한다.
예를 들어, [10, 15, 15, 17, 20]과 같은 점도 지수가 주어졌을 때, 현재 잉크 지수[=A[1]]가 [15]일 경우,
조건에 만족하는 칸은 총 1칸이므로, 답을 구하려면 상한으로 탐색을 수행해야 한다.
위 예시에서 상한 탐색의 결과는 [3]이며, 이때 자기 자신인 경우를 제외하고 1을 빼면 조건에 만족하는 칸의 개수를 구할 수 있다.

- sol[i] = upper_bound(A[i]) - i - 1
"""
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

for i in range(N):
    start, end = i, N

    while start < end:
        mid = start + (end - start) // 2

        if B[mid] <= A[i]:
            start = mid + 1
        else:
            end = mid

    print(start - i - 1, end=' ')
