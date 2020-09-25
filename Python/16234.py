import sys

input = sys.stdin.readline

N, L, R = map(int, input().split())


def bfs(n, left, right):
    population = [list(map(int, input().split())) for _ in range(n)]
    x = [0, 1, 0, -1]
    y = [-1, 0, 1, 0]
    total_move = 0

    while True:
        visited = [list(False for _ in range(n)) for _ in range(n)]
        visited[0][0] = True
        move = False
        next_nation = [0, 0]
        yet = True
        while yet:
            row = next_nation[0]
            col = next_nation[1]
            uni_pos = []
            queue = [[row, col]]
            visited[row][col] = True
            uni_pos.append([row, col])
            num_nation = 1

            while queue:
                current = queue.pop(0)
                for i in range(4):
                    next_row = current[0] + x[i]
                    next_col = current[1] + y[i]
                    if 0 <= next_row < n \
                            and 0 <= next_col < n \
                            and not visited[next_row][next_col] \
                            and left <= abs(
                        population[current[0]][current[1]] - population[next_row][next_col]) <= right:
                        queue.append([next_row, next_col])
                        visited[next_row][next_col] = True
                        uni_pos.append([next_row, next_col])
                        num_nation += 1

            if num_nation > 1:
                move = True
                uni_population = 0
                for nation in uni_pos:
                    uni_population += population[nation[0]][nation[1]]
                each_population = int(uni_population / num_nation)
                for nation in uni_pos:
                    population[nation[0]][nation[1]] = each_population

            yet = False
            for j in range(n):
                for i in range(n):
                    if not visited[i][j]:
                        next_nation[0] = i
                        next_nation[1] = j
                        yet = True
                        break

        if move:
            total_move += 1
        else:
            break
    print(total_move)



bfs(N, L, R)
