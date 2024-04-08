import sys
input = sys.stdin.readline

n, m = map(int, input().split())
lecture = list(map(int, input().split()))

start = max(lecture)
end = sum(lecture)
result = 0
while(start <= end):

    # 강의를 자를 길이
    mid = (start+end)//2
    total = 0
    cnt = 1
    for time in lecture:
        
        # 만약 현재 강의 시간을 더했을 때 강의 시간의 합이 mid를 넘어서는 경우 
        if total + time > mid:
            cnt += 1
            total = 0
        # 강의시간 누적
        total += time

    if cnt <= m:
        result = mid
        end = mid-1
    elif cnt > m:
        start = mid+1

print(result)
