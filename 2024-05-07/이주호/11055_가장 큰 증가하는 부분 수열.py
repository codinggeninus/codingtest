n=int(input())
arr=list(map(int,input().split()))
dp=[0]*(n)

dp[0]=arr[0]
for i in range(n):
  for j in range(i):
    if arr[i]>arr[j]:
      dp[i]=max(dp[i],dp[j]+arr[i])
    else:
      dp[i]=max(dp[i],arr[i])
print(max(dp))
"""앞에서부터 오름차순으로 가장 큰 숫자가 무엇일까
입력 , 계속적 확인이 필요하므로 다이나믹프로그래밍
맨 앞은 배열 맨 앞에꺼
"""

"""
뒷 배열이 더 크다면 디피값과 해당 디피값+해당배열의 값을 더한 값중 더 큰 값을 저장
디피 값과 해당 배열값 중 큰 값 저장
"""