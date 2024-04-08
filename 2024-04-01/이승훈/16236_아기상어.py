"""
16236. 아기 상어
"""
from collections import deque
from sys import stdin

input = stdin.readline


class Fish:
    def __init__(self, x, y, dist):
        self.x = x
        self.y = y
        self.dist = dist


class Shark:
    def __init__(self, x=0, y=0, size=2):
        self.x = x
        self.y = y
        self.size = size
        self.dist = 0
        self.eat_count = 0

    def eat(self, fish):
        self.move_to(fish.x, fish.y)
        self.add_dist(fish.dist)
        self.increase_eat_count()

    def move_to(self, x, y):
        self.x = x
        self.y = y

    def add_dist(self, dist):
        self.dist += dist

    def increase_eat_count(self):
        self.eat_count += 1

        if self.eat_count == self.size:
            self.eat_count = 0
            self.size += 1


def find_shark():
    for i in range(n):
        for j in range(n):
            if space[i][j] == 9:
                return Shark(i, j)


def find_fish():
    """
    bfs 탐색을 통해 먹을 수 있는 물고기를 탐색합니다.
    조건에 만족하는 물고기가 1개 이상 존재할 경우
    (1.거리 -> 2.위 -> 3.왼쪽)을 기준으로 오름차 순 정렬 후 첫 번째 요소를 반환합니다.
    """
    fishes = []
    queue = deque()
    visited = [[False] * n for _ in range(n)]

    queue.append((shark.x, shark.y, 0))
    visited[shark.x][shark.y] = True

    while queue:
        i, j, cnt = queue.popleft()

        for dir_x, dir_y in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            x = i + dir_x
            y = j + dir_y

            if x < 0 or x > n - 1 or y < 0 or y > n - 1:
                continue

            if not visited[x][y] and space[x][y] <= shark.size:
                visited[x][y] = True
                queue.append((x, y, cnt + 1))

                if 0 < space[x][y] < shark.size:
                    fishes.append(Fish(x, y, cnt + 1))

    if not fishes:
        return []

    fish = sorted(fishes, key=lambda fish: (fish.dist, fish.x, fish.y))[0]
    space[shark.x][shark.y] = 0
    space[fish.x][fish.y] = 0
    return fish


n = int(input())
space = [list(map(int, input().strip().split())) for _ in range(n)]
shark = find_shark()

while fish := find_fish():
    shark.eat(fish)

print(shark.dist)
