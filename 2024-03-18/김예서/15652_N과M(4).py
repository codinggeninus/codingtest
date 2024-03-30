import sys
input = sys.stdin.readline

n, m = map(int, input().split())
result = []
def back_tracking(i):
    if len(result) == m:
        print(' '.join(map(str, result)))
        return
    
    for i in range(i, n+1):
        # i가 result의 요소보다 크거나 같을 경우에만 추가
        result.append(i)
        back_tracking(i)
        result.pop()

back_tracking(1)