n,m = map(int,input().split())
arr1=[]
for i in range(n):
    arr1.append(int(input()))
'''
첫째 줄에는 오영식이 이미 가지고 있는 랜선의 개수 K, 그리고 필요한 랜선의 개수 N이 입력된다. 
K는 1이상 10,000이하의 정수이고, N은 1이상 1,000,000이하의 정수이다. 그리고 항상 K ≦ N 이다. 
그 후 K줄에 걸쳐 이미 가지고 있는 각 랜선의 길이가 센티미터 단위의 정수로 입력된다. 랜선의 길이는 2e31-1보다 작거나 같은 자연수이다.
'''
lo,hi = 1,max(arr1)
while lo<=hi:
    count=0
    mid=(lo+hi)//2
    for i in arr1:
        if i >= mid:
            count+=i//mid
    if count>=m:
        lo=mid+1
    else:
        hi=mid-1
print(hi)





