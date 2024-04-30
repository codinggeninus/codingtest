def command(x, y, z):
    if x == 1: #1번 명령어
        s[y-1] = z
    elif x == 2: #2번 명령어
        for i in range(y-1, z):
            if s[i] == 1:
                s[i] = 0
            else:
                s[i] = 1
    elif x == 3: #3번 명령어
        for i in range(y-1, z):
            s[i] = 0
    elif x == 4: #4번 명령어
        for i in range(y-1, z):
            s[i] = 1

#입력
n, m = map(int, input().split())
s = list(map(int, input().split()))
arr = []
#입력 받으면서 command 함수 실행
for i in range(m):
    a, b, c = map(int, input().split())
    command(a, b, c)
print(' '.join(map(str, s))) #출력