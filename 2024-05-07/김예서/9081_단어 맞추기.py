import sys
input = sys.stdin.readline

t = int(input())

# 단어의 순서가 가장 큰 건 앞으로, 작은 건 뒤로 
for _ in range(t):
    word = list(input().strip())
    
    # 뒤에서부터 탐색
    for i in range(len(word)-1, 0, -1):
        # 내림차순이 끊기는 곳 확인
        if word[i-1] < word[i]:
            for j in range(len(word)-1, i-1, -1):
                if word[i-1] < word[j]:
                    word[i-1], word[j] = word[j], word[i-1]
                    tmp = sorted(word[i:])
                    word[i:] = tmp
                    break
            break

    print(''.join(word), end='')
    print()