
N = int(input())
times = list(map(int,input().split()))
times.sort()

sum = 0
for i in range(N):
    sum += times[i] * (N-i)
    
print(sum)
