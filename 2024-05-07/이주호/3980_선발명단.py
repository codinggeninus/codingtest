T= int(input())
def bt(cnt,sum):
  global result
  #백트래킹출력조건
  if cnt == 11:
    result = max(result, sum)
    return
  #백트래킹조건기입
  for i in range(11):
    # cnt = 멤버 i = 능력치 (포지션이 채워지거나
    # 능력치가 0 이면 다음 멤버 포지션 확인, 해당 포지션 탐색 처리 이후 능력치를 더해 다음 멤버탐색
    #한사이클 끝나면 이외의 열을 돌며 가능성을 판단 후 마저 탐색
    if members[i] or not arr[cnt][i]:
      continue
    members[i]=1
    print(members)
    #다음포지션가기전 능력치추가
    bt(cnt+1,sum+arr[cnt][i])
    print(members)
    #포지션 탐색 후 해당 포지션 초기화
    members[i]=0
    # 테스트 케이스에 대한 입력 및
    # 멤버 포지션 기입 표 초기화
    # 결과값 - 함수 진행 및 출력
for _ in range(T):
  arr=[list(map(int,input().split())) for _ in range(11)]
  members = [0 for _ in range(11)]
  result = 0
  bt(0,0)
  print(result)

  """모든 포지션의 선수를 채웠을 때, 능력치의 합의 최댓값"""