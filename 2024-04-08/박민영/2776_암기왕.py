T = int(input())

def bs(test_num, length):
    s, e = 0, length-1
    while s <= e:
        mid = (s + e) // 2
        if note_1[mid] > test_num:
            e = mid - 1
        elif note_1[mid] < test_num:
            s = mid + 1
        else:
            return 1
    return 0

for _ in range(T):
    N = int(input())
    note_1 = list(map(int, input().split()))
    M = int(input())
    note_2 = list(map(int, input().split()))

    note_1.sort()

    for i in note_2:
        print(bs(i, N))

