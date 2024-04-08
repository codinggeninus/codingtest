N = int(input())
card = list(map(int, input().split()))
M = int(input())
test = list(map(int, input().split()))

card.sort()

def bs(test_num):
    s, e = 0, N-1
    while True:
        if s > e:
            return 0
        mid = (s + e) // 2
        if card[mid] > test_num:
            e = mid - 1
        elif card[mid] < test_num:
            s = mid + 1
        else:
            return cnt[card[mid]]

cnt = {}
for i in card:
    if i in cnt:
        cnt[i] += 1
    else:
        cnt[i] = 1

for i in test:
    print(bs(i), end = ' ')