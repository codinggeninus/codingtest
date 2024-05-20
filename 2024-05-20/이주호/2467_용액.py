import sys
input = sys.stdin.readline
n=int(input())
arr = list(map(int,input().split()))
inf = float('inf')
l,r = 0,n-1

ansl=arr[l]
ansr=arr[r]

while l < r:
  tmp = arr[l]+arr[r]
  if abs(tmp)<abs(inf):
    ansl = arr[l]
    ansr = arr[r]
    inf = abs(tmp)

  if tmp==0:
    break
  elif tmp<0:
    l=l+1
  else:
    r=r-1

print(ansl,ansr)