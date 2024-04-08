from collections import deque

n,m,k = map(int,input().split())
graph =[[False]*(n+1) for _ in range(n+1)]
visit1 = [0]*(n+1)
visit2 = [0]*(n+1)

for i in range(m):
    a,b = map(int,input().split())
    graph[a][b]=True
    graph[b][a]=True

def dfs(k):
    visit1[k]=1
    print(k,end=" ")
    for i in range(1,n+1):
        if(graph[k][i]>0 and visit1[i]==0):
            dfs(i)

def bfs(k):
    q = deque([k])
    visit2[k]=1
    while q:
        k = q.popleft()
        print(k,end=" ")

        for i in range(1,n+1):
            if visit2[i]==0 and graph[k][i]>0:
                q.append(i)
                visit2[i]=True



dfs(k)
print()
bfs(k)
