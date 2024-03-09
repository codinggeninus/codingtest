#######오늘 풀이
import sys
S = sys.stdin.readline().strip()
result1, result0 = 0, 0
for i in S.split('0'):
    if i:
        result1 += 1
for i in S.split('1'):
    if i:
        result0 += 1
print(min(result1, result0))


#######25일 전 풀이
import sys
N = sys.stdin.readline().strip()
one, zero = 0, 0
if N[0] == '1':
    one += 1
elif N[0] == '0':
    zero += 1
for i in range(len(N) - 1):
    if N[i] == '1' and N[i+1] == '0':
        zero += 1
    elif N[i] == '0' and N[i+1] == '1':
        one += 1

if zero >= one:
    print(one)
elif zero < one:
    print(zero)

#######다른 사람 풀이
c=input().count
print(max(c("01"),c("10")))
