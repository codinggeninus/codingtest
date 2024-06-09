N,M = map(int,input().split())
A = list(map(int,input().split()))
right = ((M // N) + 1) * max(A)
left = 0
while left < right :
    mid = (left+right)//2
    count = 0
    for a in A:
        count += mid//a
    if count < M :
        left = mid+1
    else :
        right = mid
print(left)