t = int(input())
for _ in range(t):
    k = int(input())
    n = int(input())
    ground = [x for x in range(1, n+1)]
    for i in range(k):
        for j in range(1, n):
            ground[i] += ground[j-1]
    print(ground[-1])