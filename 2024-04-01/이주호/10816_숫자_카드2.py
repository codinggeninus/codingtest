def bs(arr,target,lo,hi):
    if lo>hi:
        return 0
    mid = (lo+hi)//2
    if arr[mid]==target:
        return cnt.get(target)
    elif arr[mid]>target:
        return bs(arr,target,lo,mid-1)
    else:
        return bs(arr,target,mid+1,hi)

n = int(input())
arr1 = list(map(int,input().split()))
m = int(input())
arr2 = list(map(int,input().split()))
arr1.sort()

cnt={}
for i in arr1:
    if i in cnt:
        cnt[i]+=1
    else:
        cnt[i]=1

for i in arr2:
    print(bs(arr1,i,0,len(arr1)-1),end=' ')
'''
첫째 줄에 상근이가 가지고 있는 숫자 카드의 개수 N(1 ≤ N ≤ 500,000)이 주어진다. 
둘째 줄에는 숫자 카드에 적혀있는 정수가 주어진다. 
숫자 카드에 적혀있는 수는 -10,000,000보다 크거나 같고, 10,000,000보다 작거나 같다.

셋째 줄에는 M(1 ≤ M ≤ 500,000)이 주어진다. 
넷째 줄에는 상근이가 몇 개 가지고 있는 숫자 카드인지 구해야 할 M개의 정수가 주어지며, 이 수는 공백으로 구분되어져 있다. 
이 수도 -10,000,000보다 크거나 같고, 10,000,000보다 작거나 같다.

1.숫자 카드는 정수 하나가 적혀져 있는 카드이다. 
2.상근이는 숫자 카드 N개를 가지고 있다. 정수 M개가 주어졌을 때, 이 수가 적혀있는 숫자 카드를 상근이가 몇 개 가지고 있는지 구하는 프로그램을 작성하시오.

-> + 몇개 가지고 있는지에 대해서 정보가 필요함.

'''


