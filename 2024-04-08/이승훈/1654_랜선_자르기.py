"""
1654. 랜선 자르기

이분 탐색/상한(upper bound) 이용

1. 0 ~ (막대의 최대 길이)+1 범위에 대한 이분 탐색을 진행한다.
    - '+1'을 하는 이유는 반례 때문 (e.g. K=2, N=2, [1,1] 일때, 이분 탐색 수행시 mid = (0+1)/2 = 0
    - 따라서 DivideByZero 에러 발생!
2. 현재 임의의 길이 m에 대해 주어진 막대기를 잘랐을 때 발생하는 총 막대기의 개수를 구한다.
3. 막대기의 개수에 따라 다음을 진행한다.
    A. 막대기의 개수가 N보다 크거나 같다면 N개를 만들 수 있음을 뜻한다. 최대 랜선 길이를 구하기 위해 더 높은 값의 범위로 좁힌다.
    B. 막대기의 개수가 N보다 작다면 현재 자른 길이인 m이 너무 크다는 뜻, 따라서 더 작은 범위로 좁힌다.
4. (low - 1) 을 반환한다.
    - 이분 탐색의 상한은 기준 값 X에 대해 처음으로 큰 값이 반환된다.
    - 따라서 -1을 뺀 값을 반환! (=> 랜선 길이 자연수, 항상 정수 길이만큼 자르기 때문에 성립됨)
"""
from sys import stdin

input = stdin.readline
k, n = map(int, input().split())
lines = [int(input()) for _ in range(k)]


def find(low, high):
    while low < high:
        mid = low + (high - low) // 2
        line_count = sum([line // mid for line in lines])

        if line_count >= n:
            low = mid + 1
        else:
            high = mid
    return low - 1


print(find(0, max(lines) + 1))
