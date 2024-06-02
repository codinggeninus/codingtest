N = int(input())
M = int(input())
X = list(map(int,input().split()))
answer = X[0]

prev = 0
for x in X :
    require = (x-prev+1)//2
    answer = max(answer,require)
    prev = x
answer = max(answer,N-X[-1])
print(answer)