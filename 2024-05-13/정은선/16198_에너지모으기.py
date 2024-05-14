def dfs(arr, result):
        for i in range(1, len(arr)-1):
            e = arr[i-1] * arr[i+1]
            new_arr = arr[:i] + arr[i+1:]
            if len(new_arr) > 2:
                e += dfs(new_arr, 0)
            result = max(result, e)
        return result
            
n = int(input())
w = list(map(int, input().split()))
print(dfs(w, 0))