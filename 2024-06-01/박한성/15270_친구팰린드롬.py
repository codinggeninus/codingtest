N,M = map(int,input().split())
friend = [[] for _ in range(N)]
for _ in range(M):
    a,b = map(int,input().split())
    friend[a-1].append(b-1)
    friend[b-1].append(a-1)

used = [False] * N
answer = 0
current = 0
def dfs(start) :
    global answer,used,current
    for i in range(start,N) :
        if used[i] :
            continue
        for j in friend[i] :
            if j < i or used[j] :
                continue
            #match i to j
            used[i] = True
            used[j] = True
            current += 2
            dfs(i+1)
            current -= 2
            used[i] = False
            used[j] = False
    answer = max(answer,current)
    
dfs(0)
if answer < N :
    answer += 1
print(answer)
