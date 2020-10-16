import sys

input = sys.stdin.readline

N, L, R = map(int, input().split())


def bfs(n, left, right):
    population = [list(map(int, input().split())) for _ in range(n)]
    x = [0, 1, 0, -1]
    y = [-1, 0, 1, 0]
    day = 0

    # day가 늘어나지 않을때까지 찾는다.
    while True:
        visited = [list(False for _ in range(n)) for _ in range(n)]
        move = False
        next_nation = [0, 0]
        counter, next_i, next_j, temp_i, temp_j = 0, 0, 0, 0, 0

        #더이상 union이 없을때까지 찾는다.
        while True:
            uni_pos = []
            uni_q = [[next_nation[0], next_nation[1]]]
            uni_pos.append([next_nation[0], next_nation[1]])
            num_nation = 1

            while uni_q:
                current = uni_q.pop(0)
                visited[current[0]][current[1]] = True
                counter += 1

                for i in range(4):
                    next_row = current[0] + x[i]
                    next_col = current[1] + y[i]
                    if 0 <= next_row < n \
                            and 0 <= next_col < n \
                            and not visited[next_row][next_col] \
                            and left <= abs(
                        population[current[0]][current[1]] - population[next_row][next_col]) <= right:
                        uni_q.append([next_row, next_col])
                        visited[next_row][next_col] = True
                        uni_pos.append([next_row, next_col])
                        num_nation += 1

            # 연합국 인구 분배
            if num_nation > 1:
                move = True
                uni_population = 0
                for nation in uni_pos:
                    uni_population += population[nation[0]][nation[1]]
                each_population = int(uni_population / num_nation)
                for nation in uni_pos:
                    population[nation[0]][nation[1]] = each_population

            # 다음 union search를 시작할 nation
            next_i, next_j = temp_i, temp_j
            for j in range(next_j, n):
                temp_j = j
                for i in range(next_i, n):
                    next_nation = [i, j]
                    temp_i = i


            if counter == n*n:
                break

        if move:
            day += 1
        else:
            break
    print(day)


bfs(N, L, R)