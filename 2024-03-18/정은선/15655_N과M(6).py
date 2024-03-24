#중복 X, N개 중 M개 선택

n, m = map(int, input().split())
num = list(map(int, input().split()))
num.sort()
s = []

def dfs(start):
    if len(s) == m:
        print(' '.join(map(str, s)))
        return
    for i in range(start, n):
        if num[i] not in s:
            s.append(num[i])
            if i < n+1:
                dfs(i+1)
                s.pop()
            
dfs(0)