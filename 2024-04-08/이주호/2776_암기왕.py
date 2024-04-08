T=int(input())
n = int(input())
arr1 = list(map(int,input().split()))
m = int(input())
arr2 = list(map(int,input().split()))
arr1.sort()
'''
첫째 줄에 테스트케이스의 개수 T가 들어온다. 
다음 줄에는 ‘수첩 1’에 적어 놓은 정수의 개수 N(1 ≤ N ≤ 1,000,000)이 입력으로 들어온다. 
그 다음 줄에  ‘수첩 1’에 적혀 있는 정수들이 N개 들어온다. 
그 다음 줄에는 ‘수첩 2’에 적어 놓은 정수의 개수 M(1 ≤ M ≤ 1,000,000) 이 주어지고,
다음 줄에 ‘수첩 2’에 적어 놓은 정수들이 입력으로 M개 들어온다. 
모든 정수들의 범위는 int 로 한다.
'''
for i in range(T):
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


