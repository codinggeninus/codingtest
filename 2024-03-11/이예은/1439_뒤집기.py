# 그리디, 실버5
# https://www.acmicpc.net/workbook/view/7320

s = input()
cnt = 0

for i in range(len(s) - 1):
    if s[i] != s[i+1]:
        cnt += 1
print((cnt + 1) // 2)
