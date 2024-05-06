n, m = map(int,input().split())
arr = [0] + list(map(int,input().split()))
"""
배열 쉽게 적어 넣기 위한 설정
"""
"""
문제의 조건에 맞게 입력하기.
1->조건에 맞게 가운데 번호 전구 변경
2 l~r까지 상태 변경
3 l~r 전구 끄기
4 l~r 전구 켜기
"""
for _ in range(m):
  a, b, c = map(int, input().split())

  if (a == 1):
    arr[b] = c
  elif (a == 2):
    for i in range(b, c + 1):
      if arr[i] == 1:
        arr[i] = 0
      else:
        arr[i] = 1
  elif (a == 3):
    for i in range(b, c + 1):
      arr[i] = 0
  else:
    for i in range(b, c + 1):
      arr[i] = 1
for i in range(1,n+1):
  print(arr[i], end=" ")
