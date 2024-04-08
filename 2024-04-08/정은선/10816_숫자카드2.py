import sys
input = sys.stdin.readline

def left(i):
    start = 0
    end = n - 1
    while start <= end:
        mid = (start + end) // 2
        if card[mid] >= i:
            end = mid - 1
        else:
            start = mid + 1
    return start

def right(i):
    start = 0
    end = n - 1
    while start <= end:
        mid = (start + end) // 2
        if card[mid] <= i:
            start = mid + 1
        else:
            end = mid - 1
    return end

            
n = int(input())
card = list(map(int, input().split()))
m = int(input())
arr = list(map(int, input().split()))
card.sort()

result = []

for i in arr:
    start = left(i)
    end = right(i)
    result.append(end - start + 1)
print(" ".join(map(str, result)))