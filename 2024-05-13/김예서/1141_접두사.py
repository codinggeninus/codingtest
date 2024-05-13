import sys
input = sys.stdin.readline

'''
그리디 알고리즘

1. 단어의 길이 순으로 리스트를 정렬 
2. 자신보다 길이가 긴 문자열들을 확인하여 접두어로 사용되는지 확인
3. 만약 하나라도 접두어로 사용된다면 집합에서 제거
'''

n = int(input())
word = []
for _ in range(n):
    word.append(input().strip())

cnt = 0
word.sort(key=len)
for i in range(n):
    head = False
    for j in range(i+1, n):
        # 현재 단어가 접두어라면
        if word[i] == word[j][:len(word[i])]:
            head = True
            break
    
    if not head:
        cnt += 1

print(cnt)