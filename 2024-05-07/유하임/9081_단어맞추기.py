T = int(input())

def nextPermutation(S):
    for i in range(len(S) - 1, 0, -1):
        if S[i - 1] < S[i]:
            for j in range(len(S) - 1, i - 1, -1):
                if S[i - 1] < S[j]:
                    S[i - 1], S[j] = S[j], S[i - 1]
                    return (S[:i] + (S[i:][::-1]))

for _ in range(T):
    S = input()
    answer = nextPermutation(list(S))
    if answer:
        print(''.join(answer))
    else:
        print(S)