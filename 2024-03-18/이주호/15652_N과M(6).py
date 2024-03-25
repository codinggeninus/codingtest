n,m = map(int,input().split())

s = []
arr = list(map(int,input().split()))
arr.sort()
def dfs(start):
    if(len(s)==m):
        print(' '.join(map(str,s)))
        return

    for i in range(start,len(arr)):
        if(arr[i]in s):
            continue
        s.append(arr[i])
        dfs(i+1)
        s.pop()

dfs(0)