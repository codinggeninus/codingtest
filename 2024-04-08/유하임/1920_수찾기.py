import sys
N = int(sys.stdin.readline().strip())
array1 = list(map(int, sys.stdin.readline().strip().split()))
M = int(sys.stdin.readline().strip())
array2 = list(map(int, sys.stdin.readline().strip().split()))
array1.sort()
def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return 1
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return 0
answer = 0
for i in range(M):
    print(binary_search(array1, array2[i], 0, N-1))