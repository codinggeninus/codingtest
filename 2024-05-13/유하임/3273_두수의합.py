#딕셔너리 활용
import sys
n = int(input())
array = list(map(int, sys.stdin.readline().rstrip().split()))
x = int(input())

dic = {}
count = 0
for num in array:
    complement = x - num
    if complement in dic:
        count += 1
    dic[num] = True

print(count)

#투포인터
import sys
n = int(input())
array = list(map(int, sys.stdin.readline().rstrip().split()))
x = int(input())

array.sort()

left = 0
right = n - 1
count = 0

while left < right:
    current_sum = array[left] + array[right]
    if current_sum == x:
        count += 1
        left += 1
        right -= 1
    elif current_sum < x:
        left += 1
    else:
        right -= 1

print(count)