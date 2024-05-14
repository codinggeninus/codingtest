import sys
input = sys.stdin.readline

def dfs(tmp):

    global result

    if len(e) == 2:
        if result < tmp:
            result = tmp
        return
    else:
        for i in range(1, len(e)-1):
            k = e[i]
            del e[i]
            dfs(tmp+e[i-1]*e[i])
            e.insert(i, k)

n = int(input())
e = list(map(int, input().split()))
result = 0
dfs(0)
print(result)