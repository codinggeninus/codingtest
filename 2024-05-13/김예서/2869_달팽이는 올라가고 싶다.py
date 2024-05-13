import sys
input = sys.stdin.readline

'''
a: 낮에 올라갈 수 있는 길이
b: 밤에 미끄러지는 길이
v: 정상

낮에 올라가는 횟수: x
밤에 내려가는 횟수: x+1
v = ax- b(x-1)
x = (v-b)/(a-b)

'''
a, b, v = map(int, input().split())
day = (v-b)/(a-b)
if day == int(day):
    print(int(day))
else:
    print(int(day)+1)