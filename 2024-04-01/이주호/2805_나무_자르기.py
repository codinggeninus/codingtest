n,m = map(int,input().split())
arr1 = list(map(int,input().split()))
'''
첫째 줄에 나무의 수 N과 
상근이가 집으로 가져가려고 하는 나무의 길이 M이 주어진다. (1 ≤ N ≤ 1,000,000, 1 ≤ M ≤ 2,000,000,000)

둘째 줄에는 나무의 높이가 주어진다. 
나무의 높이의 합은 항상 M보다 크거나 같기 때문에, 
상근이는 집에 필요한 나무를 항상 가져갈 수 있다. 높이는 1,000,000,000보다 작거나 같은 양의 정수 또는 0이다.
'''
lo,hi = 1,max(arr1)
while lo<=hi:
    count=0
    mid=(lo+hi)//2
    for i in arr1:
        if i >= mid:
            count+=i-mid
    if count>=m:
        lo=mid+1
    else:
        hi=mid-1
print(hi)





