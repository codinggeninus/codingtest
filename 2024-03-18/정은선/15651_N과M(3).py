#중복허용
n, m = map(int, input().split())
s = []

def dfs(start):
    if len(s) == m:
        print(' '.join(map(str, s)))
        return
    for i in range(1, n+1):
        s.append(i)
        dfs(i+1)
        s.pop()
            
dfs(1)