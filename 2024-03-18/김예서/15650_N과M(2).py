import sys
input = sys.stdin.readline

n, m = map(int, input().split())

result = []
def back_tracking(i):
    if len(result) == m:
        print(' '.join(map(str, result)))
        return
    
    for i in range(i, n+1):
        result.append(i)
        back_tracking(i+1)
        result.pop()

back_tracking(1)