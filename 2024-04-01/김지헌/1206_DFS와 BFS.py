import sys
sys.stdin = open("1206.txt","r")


from collections import defaultdict, deque



def dfs(graph, start, visited):
    # 현재 정점을 방문한 것으로 표시
    visited[start] = True
    # 현재 정점 출력
    print(start, end=' ')
    # 현재 정점과 인접한 정점들을 탐색
    for next_node in sorted(graph[start]):
        # 인접한 정점 중 방문하지 않은 정점을 재귀적으로 탐색
        if not visited[next_node]:
            dfs(graph, next_node, visited)

def bfs(graph, start, visited):
    # 큐 생성 및 시작 정점 추가
    queue = deque([start])
    # 시작 정점을 방문한 것으로 표시
    visited[start] = True
    # BFS 시작
    while queue:
        # 큐에서 정점을 꺼내 방문하고 출력
        current_node = queue.popleft()
        print(current_node, end=' ')
        # 현재 정점과 인접한 정점들을 탐색
        for next_node in sorted(graph[current_node]):
            # 인접한 정점 중 방문하지 않은 정점을 큐에 추가하고 방문 처리
            if not visited[next_node]:
                queue.append(next_node)
                visited[next_node] = True

def main():
  N, M, V = map(int, input().split())
  graph = defaultdict(list)
  for _ in range(M):
    a, b = map(int, input().split())
    # 양방향 간선이므로 두 정점을 서로 연결
    graph[a].append(b)
    graph[b].append(a)
  # 각 정점 방문 여부 초기화
  visited = [False] * (N + 1)

  # DFS 실행
  dfs(graph, V, visited)
  print()  # 줄바꿈

  # 각 정점 방문 여부 초기화
  visited = [False] * (N + 1)

  # BFS 실행
  bfs(graph, V, visited)



main()
