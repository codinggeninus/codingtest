N,M = map(int,input().split())
count = [0] * M
info = [list(map(int,input().split()))[1:] for _ in range(N)]
for i in info:
    for j in i :
        count[j-1] += 1
for i in info:
    flag = True
    for j in i :
        if count[j-1] == 1 :
            flag = False
            break
    if flag :
        print(1)
        exit(0)
print(0)