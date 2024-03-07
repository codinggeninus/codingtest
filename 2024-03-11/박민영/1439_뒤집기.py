# 문자열 S
# 뒤집어야 하는 최소 횟수 

# 풀이1, 나의 풀이) 문자열 split() 활용

S = input()

lst_0 = S.split('1') # 연속된 0을 남긴 리스트
lst_1 = S.split('0') # 연속된 1을 남긴 리스트
cnt_0 = 0 # 0을 뒤집는 횟수
cnt_1 = 0 # 1을 뒤집는 횟수

for i in lst_0:
    if '0' in i:
        cnt_0 += 1

for j in lst_1:
    if '1' in j:
        cnt_1 += 1

print(min(cnt_0, cnt_1)) 

# 풀이2) 현재 수와 다음 수 비교해 뒤집기

S = input()
cnt = 0

for i in range(len(S)-1):
    if S[i] != S[i+1]:
        cnt += 1

print((cnt+1)//2) # 하나의 수만 뒤집으면 되니까 반으로 나눔
