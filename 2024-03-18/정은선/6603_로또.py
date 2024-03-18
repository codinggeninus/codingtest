while True:
    s = list(map(int, input().split()))
    if s == [0]:
        break
    k = s.pop(0)
    arr = []
    
    def dfs(start):
        if len(arr) == 6:
            print(' '.join(map(str, arr)))
            return
        for i in range(start, k):
            if s[i] not in arr:
                arr.append(s[i])
                dfs(i+1)
                arr.pop()
            
    dfs(0)
    print('')