t = int(input())
for _ in range(t):
    n = int(input())
    arr = set(map(int, input().split()))
    m = int(input())
    num = list(map(int, input().split()))
    
    for i in num:
        answer = 0
        start = 0
        end = n-1
        while (start <= end):
            mid = (start + end)//2
            if arr[mid] == i:
                answer = 1
                break
            elif arr[mid] > i:
                end = mid - 1
            else:
                start = mid + 1
        print(answer)