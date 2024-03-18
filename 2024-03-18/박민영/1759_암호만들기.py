# 서로 다른 L개의 알파벳으로 구성된 암호
# 암호로 사용했을 법한 문자의 종류 C가지
# 최소 한 개의 모음, 최소 두 개의 자음

import sys

L, C = map(int, sys.stdin.readline().split())
alpha = sys.stdin.readline().strip().split()
alpha.sort()
vowel_list = ['a', 'e', 'i', 'o', 'u']
res = []

def back(start):
    if len(res) == L:
        constant = list(set(res) - set(vowel_list))
        if 2 <= len(constant) <= (L-1):
            print(''.join(res))
        return
    for i in range(start, C):
        res.append(alpha[i])
        back(i+1)
        res.pop()

back(0)