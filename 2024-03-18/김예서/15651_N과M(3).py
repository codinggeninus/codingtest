import sys
input = sys.stdin.readline

n, m = map(int, input().split())
result = []
def back_tracking(i):

    # 수열의 길이가 m과 같다면 return
    if len(result) == m:
        print(' '.join(map(str, result)))
        return
    
    for i in range(1, n+1):
        result.append(i)
        back_tracking(i)
        result.pop()

back_tracking(1)
