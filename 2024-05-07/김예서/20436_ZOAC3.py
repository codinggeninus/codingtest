import sys
input = sys.stdin.readline

l, r = input().split()
string = input().strip()
keyboard = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm'] 
r_key = 'yuiophjklbnm'

xl, xr, yl, yr = 0, 0, 0, 0

# a의 좌표가 (x1, y1), b의 좌표가 (x2, y2)라면 a->b로 이동하는 데 |x1-x2|+|y1-y2| 만큼의 시간이 걸린다.
# 왼쪽 손가락, 오른쪽 손가락 위치 계산
for i in range(3):
    if l in keyboard[i]:
        xl = i
        yl = keyboard[i].index(l)
    if r in keyboard[i]:
        xr = i
        yr = keyboard[i].index(r)

time = 0
for i in range(len(string)):
    time += 1
    # 현재 키의 좌표 계산
    for j in range(3):
        if string[i] in keyboard[j]:
            x = j
            y = keyboard[j].index(string[i])

    if string[i] in r_key:
        time += abs(xr-x) + abs(yr-y)
        xr = x
        yr = y
    else:
        time += abs(xl-x) + abs(yl-y)
        xl = x
        yl = y

print(time)