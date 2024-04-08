#옛날 풀이
T = int(input())
for i in range(T):
    note1 = int(input())
    array1 = map(int, input().split())
    note2 = int(input())
    array2 = list(map(int, input().split()))
    dic1 = {}
    for i in array1:
        dic1[i] = 1
    for i in array2:
        if i not in dic1:
            print(0)
        else:
            print(1)

#오늘 풀이
T = int(input())
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
for i in range(T):
    note1 = int(input())
    array1 = list(map(int, input().split()))
    note2 = int(input())
    array2 = list(map(int, input().split()))
    array1.sort()
    for j in array2:
        print(binary_search(array1, j, 0, len(array1) - 1))


#다른 사람 풀이
for _ in range(int(input())):

    a = int(input())
    su1 = set(map(int, input().split()))
    
    b = int(input())
    su2 = list(map(int, input().split()))
    
    for n in su2:
        print(1 if n in su1 else 0)
