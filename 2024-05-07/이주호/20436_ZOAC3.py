left, right = input().split()
word = list(input())

keyboard = ['qwertyuiop','asdfghjkl','zxcvbnm']
mo='yuiophjklbnm'
xl,yl,xr,yr = None,None,None,None
"""
이차원 배열 초기화
키보드 배열중에서 존재하는지 찾아서 배열안에서의 위치 까지 저장.
키한번 누르는데 1초 + 이동시간도 더해주기(x1-x2절대값 + y1+y2절대값
단어만큼 반복
"""
for i in range(len(keyboard)):
  if left in keyboard[i]:
    xl = i
    yl = keyboard[i].index(left)
  if right in keyboard[i]:
    xr= i
    yr = keyboard[i].index(right)
time = 0
for string in word:
  time+=1
  if string in mo:
    for i in range(len(keyboard)):
      if string in keyboard[i]:
        nx = i
        ny = keyboard[i].index(string)
        time += abs(nx-xr)+abs(ny-yr)
        xr= nx
        yr=ny
        break
  else:
    for i in range(len(keyboard)):
      if string in keyboard[i]:
        nx = i
        ny = keyboard[i].index(string)
        time+=abs(nx-xl)+abs(ny-yl)
        xl =nx
        yl=ny
        break
print(time)