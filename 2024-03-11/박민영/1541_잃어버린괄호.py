# 식 formu
# 괄호 친 후 식의 최소값 res

import sys

formu = sys.stdin.readline().strip()
formu = formu.split('-') # '-'보다 '+' 연산을 먼저 해주어야 함
res = sum(map(int, formu[0].split('+'))) # 연산식의 첫 값 저장

for i in formu[1:]:
    res -= sum(map(int, i.split('+')))

print(res)
