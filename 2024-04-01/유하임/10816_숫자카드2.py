import sys
from collections import Counter
N = int(sys.stdin.readline().strip())
cardNum = list(map(int, sys.stdin.readline().strip().split()))
M = int(sys.stdin.readline().strip())
sangNum = list(map(int, sys.stdin.readline().strip().split()))
count = Counter(cardNum)
for i in sangNum:
    print(count[i], end=" ")