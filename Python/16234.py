import sys
import math

input = sys.stdin.readline

N, L, R = map(int, input().split())


def bfs(n, left, right):
    continent = [list(map(int, input().split())) for _ in range(n)]
    visited = [list(False for _ in range(n)) for _ in range(n)]
    x = [0, 1, 1, 1, 0, -1, -1, -1]
    y = [1, 1, 0, -1, -1, -1, 0, 1]
    population = 0
    ans = 0
    #시작위치
    queue = [[0, 0]]
    visited[0, 0] = True
    while queue: #하나의 연합이 끝날때까지
        currentPos = queue.pop(0)
        for i in range(8):
            next_x = currentPos[0] + x[i]
            next_y = currentPos[1] + y[i]
            if 0 > next_x >= n \
                    and 0 > next_y >= n \
                    and not visited[next_x][next_y]\
                    and left <= abs(continent[currentPos[0]][currentPos[1]] - continent[next_x][next_y]) <= right:
                queue.append([next_x, next_y])
                visited[next_x][next_y] = True

    cnt = 0
    for i in visited[i]:
        for j in visited[i][j]:
            if j:
                cnt += 1
                population += continent[i][j]

    population = math.floor(population / cnt)
    for i in visited[i]:
        for j in visited[i][j]:
            if j:
                continent[i][j] = population
    #다음 연합으로 가야해..