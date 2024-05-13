import sys
input = sys.stdin.readline

'''
구현

남학생: 스위치 번호가 자기가 받은 수의 배수이면, 그 스위치의 상태를 바꾼다.
여학생: 여학생이 받은 스위치 번호를 중심으로 좌우가 대칭이면서 
        가장 많은 스위치를 포함하는 구간을 찾아서, 그 구간에 속한 스위치의 상태를 모두 바꾼다.
'''

num = int(input())  # 스위치 개수
switch = list(map(int, input().split())) # 스위치 상태
switch.insert(0, -1)
s = int(input()) # 학생수 

for _ in range(s):
    # 남자: 1, 여자: 2
    gender, s_num = map(int, input().split())
    if gender == 1:
        for i in range(s_num, len(switch), s_num):
            switch[i] = 1-switch[i]
    elif gender == 2:
        l = s_num-1
        r = s_num+1
        while(True):
            # 범위를 벗어나면 종료
            if l < 1 or r > num:
                break
            # 두 스위치가 비대칭이면 종료
            elif switch[l] != switch[r]:
                break
            l -= 1
            r += 1

        # 구간에 속한 스위치 모두 변경
        for j in range(l+1, r):
            switch[j] = 1-switch[j]      

# 20개씩 줄바꿈하며 스위치의 상태 출력
for i in range(1, len(switch)):
    if i-1 != 0 and (i-1)%20 == 0:
        print()
    print(switch[i], end=' ')