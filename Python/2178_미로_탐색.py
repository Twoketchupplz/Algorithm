from collections import deque


# 카운터를 어떻게 만들것인가
# bfs
def bfs(maze: list, n: int, m: int):
    queue = deque()
    queue.append((0, 0))

    while queue:
        # 현재 노드 방문; ans++;
        row, col = queue.popleft()

        # 주변 탐색
        for i in range(4):
            nr, nc = row + dr[i], col + dc[i]
            if n > nr >= 0 and m > nc >= 0 and maze[nr][nc] == 1:
                maze[nr][nc] = maze[row][col] + 1
                queue.append((nr, nc))

    return maze[n - 1][m - 1]


dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

# 미로 크기 row, col line 입력; 미로 정보 입력
N, M = map(int, input().split())
Maze = [[int(cell) for cell in input()] for _ in range(N)]

print(bfs(Maze, N, M))
