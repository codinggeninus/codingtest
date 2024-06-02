t = int(input())
for _ in range(t):
    n, m = map(str, input().split())
    change = [0, 0]
    for i in range(len(n)):
        if n[i] != m[i]:
            change[int(n[i])] += 1
    print(max(change))