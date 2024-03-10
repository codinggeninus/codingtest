import sys
input = sys.stdin.readline

s = input().strip()

zero_cnt = 0
one_cnt = 0

# 맨 끝에 0또는 1이 있는 경우 미리 체크
if len(s) > 1 and s[len(s)-1] == '0':
    zero_cnt += 1
elif len(s) > 1 and s[len(s)-1] == '1':
    one_cnt += 1 

# 현재 수와 다음 수를 비교하여 다르면 이전까지는 연속된 수이므로 1 증가
for i in range(len(s)-1):
    if s[i] != s[i+1]:
        if s[i] == '0':
            zero_cnt += 1
        else:
            one_cnt += 1

# 둘 중 더 작은 값 출력
print(min(zero_cnt, one_cnt))