n = int(input())
p = list(map(int, input().split()))

#인출 시간 오름차순 정렬
p.sort()
time = 0

#처음~자기자신까지 더한 값을 time에 더함
for i in range(n):
    time += sum(p[:i+1])
    
print(time)