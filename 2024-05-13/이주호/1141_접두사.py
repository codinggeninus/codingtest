import sys
input = sys.stdin.readline
n=int(input())
arr=[input().rstrip() for _ in range(n)]

"""
짧은것 순으로 정렬해서 짧은게 긴 문자열의 접두사가 될 수 있는지 검사한다.

앞에서부터 접두사일 수 있는지 확인하고 a가 접두사라면 넘어가고 
접두사가 아니라면 카운트를 올려서 반환

++ 문자열은 rstrip을 통해 개행문자를 없애준다.
"""
arr.sort(key = len)
count = 0
for i in range(n):
  a = False
  for j in range(i+1, n):
    if arr[i] == arr[j][0:len(arr[i])]:
      a = True
      break
  if not a:
    count+=1
print(count)



