"""
2343. 기타 레슨

- 조건에 맞는 블루레이 크기를 이분 탐색을 통해 찾는 것이 핵심
- 주어진 조건 (블루레이 개수 == m)을 만족하는 크기에 대해 이분탐색을 하한 기준으로 진행하면 가능한 블루 레이의 크기 중 최소가 된다.

1. (주어진 강의 중 최대 재생 길이 ~ 전체 강의 재생 길이) 만큼 이분 탐색 진행
2. 현재 블루레이 크기(mid)에 대해 블루레이 개수를 구한다.
3. 블루레이 개수에 따라 다음을 진행한다.
    A. 블루레이 개수 <= m: 블루레이 크기가 너무 큼, 범위 감소
    B. 블루레이 개수 > m: 블루레이 크기가 너무 작음 -> 범위 증가
"""
from sys import stdin

input = stdin.readline
n, m = map(int, input().split())
lectures = list(map(int, input().split()))
max_lecture = max(lectures)
total_time = sum(lectures)

start, end = max_lecture, total_time
answer = 0

while start < end:
    mid = (start + end) // 2
    blueray_count = 1
    play_time = 0

    for lecture in lectures:
        play_time += lecture

        if mid < play_time:
            blueray_count += 1
            play_time = lecture

    if blueray_count > m:
        start = mid + 1
    else:
        end = mid

print(start)
