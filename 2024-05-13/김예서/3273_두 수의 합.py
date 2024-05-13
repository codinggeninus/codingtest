import sys
input = sys.stdin.readline

'''
투 포인터
'''

n = int(input())
array = list(map(int, input().split()))
x = int(input())

array.sort()
i = 0
j = n-1
cnt = 0
while(i < j):
    if array[i] + array[j] == x:
        cnt += 1
        i += 1
    elif array[i] + array[j] < x:
        i += 1
    elif array[i] + array[j] > x:
        j -=1
    
print(cnt)