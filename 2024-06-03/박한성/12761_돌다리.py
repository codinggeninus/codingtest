import queue

A,B,N,M = map(int,input().split())
dist = [-1] * 100001
dist[N] = 0
if N == M :
    print(0)
    exit(0)
q = queue.Queue()
q.put(N)
while not q.empty() :
    cur = q.get()
    nexts = set([cur+1,cur-1,cur+A,cur-A,cur+B,cur-B,cur*A,cur*B])
    for next in nexts:
        if 0 <= next <= 100000 and dist[next]==-1:
            dist[next] = dist[cur] + 1
            if next == M:
                print(dist[next])
                exit(0)
            q.put(next)