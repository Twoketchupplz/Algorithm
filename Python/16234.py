import sys

input = sys.stdin.readline

N, L, R = map(int, input().split())


def bfs(n, left, right):
    population = [list(map(int, input().split())) for _ in range(n)]
    union = [list(False for _ in range(n)) for _ in range(n)]
    x = [0, 1, 0, -1]
    y = [-1, 0, 1, 0]
    total_move = 0
    while True:
        visited = [list(False for _ in range(n)) for _ in range(n)]
        move = False
        for col in range(n):
            for row in range(n):
                if not visited[row][col]:
                    queue = [[row, col]]
                    visited[row][col] = True
                    union[row][col] = True
                    union_p = population[row][col]
                    num_nation = 1
                    while queue:
                        current = queue.pop(0)
                        for i in range(4):
                            next_row = current[0] + x[i]
                            next_col = current[1] + y[i]
                            if 0 <= next_row < n and 0 <= next_col < n and not visited[next_row][next_col] and left <= abs(population[current[0]][current[1]] - population[next_row][next_col]) <= right:
                                queue.append([next_row, next_col])
                                visited[next_row][next_col] = True
                                union[next_row][next_col] = True
                                union_p += population[next_row][next_col]
                                num_nation += 1
                                move = True
                                print(move)
                    for m_col in range(n):
                        for m_row in range(n):
                            if union[m_row][m_col]:
                                population[m_row][m_col] = int(union_p / num_nation)
                                union[m_row][m_col] = False
        if move:
            total_move += 1
        else:
            break
    print(total_move)


bfs(N, L, R)