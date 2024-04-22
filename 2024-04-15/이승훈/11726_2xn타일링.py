"""
11726. 2xn 타일링
"""
from sys import stdin


def sol(n):
    a = b = 1
    for _ in range(n):
        a, b = b, a + b
    return a % 10007


print(sol(int(stdin.readline())))
