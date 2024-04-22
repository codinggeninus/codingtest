n = int(input())
stair = [0] + [int(input()) for _ in range(n)]

if n < 2:
    print(stair[n])
else:
    score = [0] * (n+1)
    score[1] =stair[1]
    score[2] = score[1] + stair[2]
    for i in range(3, n+1):
        score[i] = max(score[i-3]+stair[i-1], score[i-2])+stair[i]

    print(score[n])