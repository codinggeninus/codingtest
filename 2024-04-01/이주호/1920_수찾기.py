n = int(input())
arr1 = list(map(int,input().split()))
m = int(input())
arr2 = list(map(int,input().split()))
arr1.sort()
'''
첫째 줄에 자연수 N(1 ≤ N ≤ 100,000)이 주어진다. 
다음 줄에는 N개의 정수 A[1], A[2], …, A[N]이 주어진다. 
다음 줄에는 M(1 ≤ M ≤ 100,000)이 주어진다. 
다음 줄에는 M개의 수들이 주어지는데, 

이 수들이 A안에 존재하는지 알아내면 된다.
->이 수들 하나하나에 대해서 이진탐색. 
모든 정수의 범위는 -2e31 보다 크거나 같고 2e31보다 작다.
'''
for i in arr2:
    lo,hi = 0,n-1
    count=False

    while lo<=hi:
        mid=(lo+hi)//2
        if i == arr1[mid]:
            count=True
            print(1)
            break
        elif i>arr1[mid]:
            lo=mid+1
        else:
            hi=mid-1
    if not count:
        print(0)


