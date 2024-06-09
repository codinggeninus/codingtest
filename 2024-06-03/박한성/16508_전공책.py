T = input()

target = [0] * 26
for t in T:
    target[ord(t) - ord('A')]+=1
N = int(input())

books = []
answer = 1600007
for _ in range(N) :
    using = [0]*26
    cost, s = input().split()
    for c in s :
        using[ord(c)-ord('A')] += 1
    books.append((int(cost),using))



maxbit = 1<<N
for bit in range(1,maxbit) :
    cost = 0
    using = [0]*26
    for i in range(N) :
        if (bit & (1<<i)) != 0:
            cost += books[i][0]
            for j in range(26) :
                using[j] += books[i][1][j]
    flag = True
    for j in range(26) :
        if using[j] < target[j] :
            flag = False
            break
    if(flag) :
        answer = min(answer,cost)
        
if answer == 1600007:
    print(-1)
else :
    print(answer)