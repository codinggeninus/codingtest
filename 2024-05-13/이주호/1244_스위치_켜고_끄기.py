import sys

input = sys.stdin.readline


def change(b):
  if arr[b] == 1:
    arr[b] = 0
  else:
    arr[b] = 1


n = int(input())
arr = [0] + list(map(int, input().split()))
m = int(input())
for i in range(m):
  a, b = map(int, input().split())

  """
  
  문제의 요구대로 남성이라면 해당문자의 배수만큼 넘어가며 숫자를 바꿔준다.
  여성이라면 범위를 벗어나지 않는한도내에서 대칭인 경우에 대해서 값을 변경해준다.
  또한 문제에서 반환하는 값에 대해서 20개씩 출력되도락하므로 추가적으로 조건문을 만들 수 있다.
  """
  if a == 1:
    for i in range(b, n + 1, b):
      change(i)
  else:
    change(b)
    for j in range(n//2):
      if b+j > n or b - j < 1 : break
      if arr[b+j] == arr[b-j]:
        change(b+j)
        change(b-j)
      else:
        break

for i in range(1,n+1):
  print(arr[i],end = " ")
  if i % 20 == 0:
    print()
