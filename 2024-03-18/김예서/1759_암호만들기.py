import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

l, c = map(int, input().split())
alpha = list(input().split())
# 알파벳 오름차순 정렬
alpha.sort()

vowel = ['a', 'e', 'i', 'o', 'u']
result = []
vowel_cnt = 0
consonant_cnt = 0
def back_tracking(i):

    global vowel_cnt
    global consonant_cnt

    if len(result) == l:
        for j in range(l):
            # 모음, 자음 개수 카운트
            if result[j] in vowel:
                vowel_cnt += 1
            else:
                consonant_cnt += 1
        
        # 모음의 개수가 0이거나 자음의 개수가 2이하라면 출력 X
        if vowel_cnt == 0 or consonant_cnt < 2:
            consonant_cnt = 0
            return
        
        print(''.join(map(str, result)))
        vowel_cnt = 0
        consonant_cnt = 0
        return

    for i in range(i, c):
        # 이미 존재하는 문자일 경우 continue 
        if alpha[i] in result:
            continue

        result.append(alpha[i])
        back_tracking(i+1)
        result.pop()

back_tracking(0)