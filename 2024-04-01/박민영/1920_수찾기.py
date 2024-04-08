N = int(input())
A = list(map(int, input().split()))
M = int(input())
test = list(map(int, input().split()))

A.sort()

def bs(test_num):
    s, e = 0, N-1
    while s <= e:
        mid = (s + e) // 2
        if A[mid] > test_num:
            e = mid - 1
        elif A[mid] < test_num:
            s = mid + 1
        else:
            return 1
    return 0

for i in test:
    print(bs(i))