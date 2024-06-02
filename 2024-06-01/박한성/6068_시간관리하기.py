N = int(input())
work = [tuple(map(int,input().split())) for _ in range(N)]
work = sorted(work,key=lambda x : x[1],reverse=True)
T = work[0][1]

for w in work :
    T = min(T,w[1]) - w[0]
    
if T < 0 :
    print(-1)
else :
    print(T)